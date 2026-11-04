> Sumber: GitHub Docs, "About code owners" — https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
> Catatan: Dipakai saat menetapkan kepemilikan kontrak API, adapter tiap versi, gateway, dan CI agar review otomatis berjalan.
# .github/CODEOWNERS — pola TERAKHIR yang cocok menang; path case-sensitive
*                                  @{{ORG}}/{{TIM_PLATFORM}}
/.github/                          @{{ORG}}/{{TIM_PLATFORM}}
/.github/CODEOWNERS                @{{ORG}}/{{TIM_PLATFORM}}
/docs/api/                         @{{ORG}}/{{TIM_API}} @{{ORG}}/{{TIM_DOC}}
/docs/api/v1/                      @{{ORG}}/{{TIM_API_LEGACY}}
/docs/api/v2/                      @{{ORG}}/{{TIM_API}}
/docs/api/v3/                      @{{ORG}}/{{TIM_API}}
/docs/api/lifecycle/               @{{ORG}}/{{TIM_API}} @{{ORG}}/{{TIM_SRE}}
/packages/contracts/               @{{ORG}}/{{TIM_API}}
/apps/backend/{{NAMA_API}}/src/interface/http/v1/  @{{ORG}}/{{TIM_API_LEGACY}}
/apps/backend/{{NAMA_API}}/src/interface/http/v2/  @{{ORG}}/{{TIM_API}}
/apps/backend/{{NAMA_API}}/src/interface/http/v3/  @{{ORG}}/{{TIM_API}}
/infra/gateway/                    @{{ORG}}/{{TIM_SRE}}
/infra/observability/              @{{ORG}}/{{TIM_SRE}}
/scripts/                          @{{ORG}}/{{TIM_SRE}} @{{ORG}}/{{TIM_DATA}}
