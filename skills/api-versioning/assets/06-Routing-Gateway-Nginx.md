> Sumber: NGINX Documentation — Reverse Proxy & Split Clients Modules — https://nginx.org/en/docs/http/ngx_http_proxy_module.html ; https://nginx.org/en/docs/http/ngx_http_split_clients_module.html
> Catatan: Dipakai saat menyusun konfigurasi gateway untuk /api/v1, /api/v2, dan /api/v3 beserta canary V3 (weighted split + header override) dan SSL/TLS.
# infra/gateway/api-versions.conf — Konfigurasi gateway multi-versi zero downtime

upstream {{UPSTREAM_STABLE}} {
    server {{HOST_STABLE}}:{{PORT}} max_fails=3 fail_timeout=10s;
}

upstream {{UPSTREAM_CANARY_V3}} {
    server {{HOST_CANARY_V3}}:{{PORT}} max_fails=3 fail_timeout=10s;
}

# Pembagian traffic berbobot (weighted canary) berdasarkan IP klien atau request ID
split_clients "${remote_addr}${http_user_agent}" $canary_v3_weight {
    {{CANARY_PERCENTAGE}}%   {{UPSTREAM_CANARY_V3}};
    *                        {{UPSTREAM_STABLE}};
}

# Header override eksplisit (misal: X-Canary-V3: 1) mendahului pembagian berbobot
map $http_x_canary_v3 $target_v3 {
    "1"     {{UPSTREAM_CANARY_V3}};
    "0"     {{UPSTREAM_STABLE}};
    default $canary_v3_weight;
}

server {
    listen {{PORT_TLS}} ssl http2;
    server_name {{API_HOST}};

    # Konfigurasi sertifikat SSL/TLS
    ssl_certificate {{SSL_CERTIFICATE_PATH}};
    ssl_certificate_key {{SSL_CERTIFICATE_KEY_PATH}};
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # /api/v1: Status deprecated dengan header RFC 9745 Deprecation & RFC 8594 Sunset
    location /api/v1/ {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-API-Version "V1";
        proxy_set_header X-Request-ID $request_id;

        # Lifecycle headers: RFC 9745 Deprecation (timestamp Unix/Date) dan RFC 8594 Sunset (HTTP-Date)
        add_header Deprecation "@{{UNIX_TIMESTAMP_DEPRECATION_V1}}" always;
        add_header Sunset "{{HTTP_DATE_SUNSET_V1}}" always;
        add_header Link "<https://{{HOST_DOCS}}/api/lifecycle/deprecation>; rel=\"deprecation\"" always;
        add_header Link "<https://{{HOST_DOCS}}/api/lifecycle/sunset>; rel=\"sunset\"" always;

        proxy_pass http://{{UPSTREAM_STABLE}};
    }

    # /api/v2: Versi aktif stabil saat ini
    location /api/v2/ {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-API-Version "V2";
        proxy_set_header X-Request-ID $request_id;

        # Opsional: Jika V2 mulai didepresiasi untuk persiapan V3:
        # add_header Deprecation "@{{UNIX_TIMESTAMP_DEPRECATION_V2}}" always;
        # add_header Sunset "{{HTTP_DATE_SUNSET_V2}}" always;

        proxy_pass http://{{UPSTREAM_STABLE}};
    }

    # /api/v3: Versi rilis bertahap (canary split + header override)
    location /api/v3/ {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-API-Version "V3";
        proxy_set_header X-Request-ID $request_id;

        proxy_pass http://$target_v3;
    }

    # Variasi representasi content negotiation (jika format header dipakai bersamaan)
    add_header Vary "Accept, X-API-Version" always;
}
