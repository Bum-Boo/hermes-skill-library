# Hermes Skill Library

[English](README.md) | **한국어** | [日本語](README.ja.md) | [中文](README.zh-CN.md)

Hermes Agent 계열 어시스턴트를 위한 재사용 가능 스킬 모음입니다. 단일 목적 패키지가 아니며, 전체 라이브러리 또는 목적별 컬렉션 하나를 설치하실 수 있습니다.

## 컬렉션

| 컬렉션 | 용도 |
|---|---|
| [`gstack-safe`](collections/gstack-safe/) | 근거 중심 명세·검토·조사 |
| [`agent-engineering`](collections/agent-engineering/) | 코딩 에이전트 CLI에 범위가 정해진 작업 위임 |
| [`research-workflows`](collections/research-workflows/) | 자료 수집·모니터링·ML 실험·평가 근거 관리 |
| [`comfyui-image-workflows`](collections/comfyui-image-workflows/) | ComfyUI 생성·배치·검증·문제 해결 |
| [`wsl-operator`](collections/wsl-operator/) | Windows/WSL 경로와 GUI 실행기 |
| [`oauth-browser-handoff`](collections/oauth-browser-handoff/) | 헤드리스·WSL·원격 환경의 사용자 OAuth 브라우저 완료 |
| [`profile-context-diet`](collections/profile-context-diet/) | 오래되거나 과도한 Hermes 프로필 컨텍스트 정리 |
| [`hermes-profile-operations`](collections/hermes-profile-operations/) | 다중 프로필 설정·저장 공간·컨텍스트 관리 |
| [`local-development-safety`](collections/local-development-safety/) | 범위가 좁은 로컬 변경과 최신 완료 근거 |
| [`github-publishing`](collections/github-publishing/) | WSL 환경 게시와 원격 상태 검증 |
| [`telegram-operator`](collections/telegram-operator/) | 간결하고 사실에 근거한 Telegram 진행·결과 보고 |
| [`computer-use-safety`](collections/computer-use-safety/) | 백그라운드 우선 데스크톱 제어와 안전한 단계 상승 |
| [`web-interface-verification`](collections/web-interface-verification/) | 반응형·터치·호버·태블릿 너비 검증 |
| [`repository-maintenance`](collections/repository-maintenance/) | 포크·미러·벤더 스냅샷·다운스트림 감사 |
| [`artifact-recovery`](collections/artifact-recovery/) | 모호한 이전 로컬 파일의 근거 기반 복구와 안전한 전달 |

각 컬렉션 페이지에서 포함 스킬과 사용 안내를 확인하실 수 있습니다. 기계 판독용 목록은 [`catalog.json`](catalog.json)에 있습니다.

## 전체 설치

```bash
git clone https://github.com/Bum-Boo/hermes-skill-library.git
cd hermes-skill-library
./scripts/install.sh
hermes skills list
```

```bash
# Install for one profile
./scripts/install.sh ~/.hermes/profiles/<profile>/skills
hermes --profile <profile> skills list
```

기본 대상은 `~/.hermes/skills`입니다. Hermes CLI가 `skills list`의 `--profile` 옵션을 지원하지 않으면 해당 프로필로 대화를 시작한 뒤 설치된 스킬을 나열하거나 불러오도록 요청해 주세요.

> 설치 스크립트는 라이브러리를 대상에 복사하며 같은 경로의 파일을 덮어쓸 수 있습니다. 실행 전에 소스를 검토하고 올바른 대상을 지정해 주세요.

## 컬렉션 하나만 설치

```bash
./scripts/install-collection.sh <collection-name>
./scripts/install-collection.sh comfyui-image-workflows ~/.hermes/profiles/<profile>/skills
```

위 표의 컬렉션 이름을 사용해 주세요. [`scripts/install-collection.sh`](scripts/install-collection.sh)에 구현되지 않은 이름은 오류로 종료됩니다.

## 저장소 구조

```text
skills/<category>/<skill-name>/SKILL.md  설치 가능한 스킬
collections/<collection>/README.md      목적별 안내
scripts/install.sh                      전체 스킬 설치
scripts/install-collection.sh           컬렉션 하나 설치
catalog.json                            컬렉션 목록
SECURITY.md                             보안 정책
LICENSE                                 MIT 라이선스
```

## 안전한 기여

스킬을 `skills/<category>/<skill-name>/SKILL.md`에 유효한 Hermes frontmatter와 함께 추가하고, 컬렉션 문서와 `catalog.json`을 갱신해 주세요. 공유 전에는 임시 디렉터리에 설치를 시험하고 자격 증명, 개인 경로, 계정 식별자, 브라우저 프로필, 고객 데이터가 없는지 확인해 주세요. 실제 비밀 값은 커밋하지 마세요. [`SECURITY.md`](SECURITY.md)를 참고해 주세요.

## 출처 표기 부탁

라이브러리나 파생 작업을 공개하실 때에는 가능하면 **@Bum-Boo**와 [원본 저장소](https://github.com/Bum-Boo/hermes-skill-library)를 언급해 주시면 감사하겠습니다. 이는 감사의 뜻으로 드리는 요청이며 라이선스 조건을 추가하거나 변경하지 않습니다.

## 라이선스

MIT입니다. [`LICENSE`](LICENSE)를 확인해 주세요.
