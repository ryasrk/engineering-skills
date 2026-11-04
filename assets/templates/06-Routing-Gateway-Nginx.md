> Sumber: catatan riset internal (lihat research_notes/...)
> Catatan: Dipakai saat menyusun konfigurasi gateway untuk /api/v1, /api/v2, dan /api/v3 beserta canary V3.
# infra/gateway/api-versions.conf — ILUSTRASI, sesuaikan dengan gateway Anda
upstream {{UPSTREAM_STABLE}} { server {{HOST_STABLE}}:{{PORT}}; }
upstream {{UPSTREAM_CANARY_V3}} { server {{HOST_CANARY_V3}}:{{PORT}}; }

map $http_x_canary_v3 $target_v3 {
    default {{UPSTREAM_STABLE}};
    "1"     {{UPSTREAM_CANARY_V3}};
}

server {
    listen {{PORT_TLS}} ssl;
    server_name {{API_HOST}};

    location /api/v1/ {
        proxy_set_header X-API-Version "V1";
        proxy_set_header X-Request-ID $request_id;
        add_header Deprecation "@{{UNIX_TIMESTAMP_DEPRECATION_V1}}" always;
        add_header Sunset "{{HTTP_DATE_SUNSET_V1}}" always;
        add_header Link "<https://{{HOST_DOCS}}/api/lifecycle/deprecation>; rel=\"deprecation\"" always;
        add_header Link "<https://{{HOST_DOCS}}/api/lifecycle/sunset>; rel=\"sunset\"" always;
        proxy_pass http://{{UPSTREAM_STABLE}};
    }

    location /api/v2/ {
        proxy_set_header X-API-Version "V2";
        proxy_set_header X-Request-ID $request_id;
        add_header Deprecation "@{{UNIX_TIMESTAMP_DEPRECATION_V2}}" always;
        add_header Sunset "{{HTTP_DATE_SUNSET_V2}}" always;
        proxy_pass http://{{UPSTREAM_STABLE}};
    }

    location /api/v3/ {
        proxy_set_header X-API-Version "V3";
        proxy_set_header X-Request-ID $request_id;
        proxy_pass http://$target_v3;
    }

    # Jika custom header ikut menentukan representasi, jangan lupa:
    # add_header Vary "Accept, API-Version" always;
}
