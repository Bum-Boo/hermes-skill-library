# hermes-skill-library 독립 읽기 전용 리뷰 (2026-10-31)

- 대상: `main` 기준 커밋 `ca587e6` (Add grounded citation workflow)
- 범위: 스킬 메타데이터 일관성, 내부 링크/경로, 설치 스크립트의 파괴적 동작과 재실행 동작, 중복·모순 지침, `grounded-citations/scripts/sources.py` 실행 경로
- 제품 코드, 워크플로, 매니페스트, `catalog.json`은 수정하지 않았습니다. 추가한 것은 이 보고서와 `review/` 아래의 합성(synthetic) 재현 스크립트뿐입니다.
- 모든 재현은 `mktemp`/`tempfile` 임시 디렉터리와 `example.*` 가짜 URL만 사용했습니다. 네트워크 호출, 실제 계정, 실제 `~/.hermes`는 사용하지 않았습니다(`HOME`을 임시 경로로 바꿔 실행).

## 기존 테스트

저장소에는 테스트, CI 워크플로(`.github/`), 기여 지침 파일(CONTRIBUTING)이 없습니다. 실행할 기존 테스트는 0개입니다. 그래서 아래 리뷰용 테스트를 새로 작성해 실행했습니다.

| 명령 | 결과 |
|---|---|
| `python3 -I review/check_consistency.py` | 5건 탐지(아래 F5–F7), exit 1 |
| `bash review/test_install_rerun.sh` | 21 통과 / 0 실패 (+INFO 4건) |
| `python3 -m unittest discover -s review -p "test_*.py" -v` | 9개 실행, 9 통과 (Covered 3, Defects 6) |

`test_defect_*` 테스트는 **현재의 결함 동작**을 단언하므로 지금은 통과합니다. 수정 후에는 해당 단언을 뒤집으면 회귀 테스트가 됩니다.

## 요약

| ID | 분류 | 심각도 | 내용 |
|---|---|---|---|
| F1 | 검증된 결함 | P2 (사용자 문서 손실) | `render --replace-in`이 마지막 `Sources` 제목 뒤의 모든 내용을 삭제 |
| F2 | 검증된 결함 | P2 | 코드 펜스 안의 `Sources:` 줄에서 초안이 잘림 |
| F3 | 검증된 결함 | P2 | `--style footnotes/bibtex --replace-in`이 멱등이 아님(블록 누적) |
| F4 | 검증된 결함 | P2 | 괄호가 있는 URL은 자기 자신이 렌더링한 블록의 `verify`에 실패 |
| F5 | 검증된 결함 | P3 | 번역 README 3종에 컬렉션 2개 누락 |
| F6 | 검증된 결함 | P3 | `catalog.json`의 저장소 URL 계정명 불일치 |
| F7 | 정적 위험 | P3 | 지침 상호 모순·외부 스킬 참조·고정 경로 |
| F8 | 검증된 결함 | P3 | 잠금(lock) 타임아웃 시 살아 있는 보유자의 잠금을 탈취 |
| F9 | 검증된 결함 | P3 | `--only 1-` 같은 잘못된 범위에서 traceback |
| F10 | 정적 위험 | P2 (미검증) | 전체 설치가 Hermes 번들 스킬을 같은 경로에서 덮어쓸 가능성 |
| — | 이미 문서화 / 문제 아님 | — | 설치 재실행, 덮어쓰기, 오래된 파일 잔존 등(아래 참고) |

P1(데이터 손실/보안)에 해당하는 설치 스크립트 문제는 찾지 못했습니다. 설치 스크립트는 `cp -R`만 사용하며 삭제·이동·권한 변경·네트워크 호출이 없습니다.

---

## 상세

### F1. `render --replace-in`이 Sources 블록 뒤 내용을 삭제 — 검증된 결함, P2

- 위치: `skills/research/grounded-citations/scripts/sources.py:368-382` (`_strip_sources_block`), 호출부 `:644-648`
- 트리거: `## Sources` 블록 뒤에 `## Appendix` 등 다른 섹션이 있는 초안에 `render --replace-in draft.md` 실행
- 관찰: 마지막 Sources 제목부터 파일 끝까지 전부 잘라낸 뒤 새 블록을 붙이고 파일을 제자리에서 덮어씀. Appendix 내용이 백업 없이 사라짐
- 기대: Sources 블록(제목 + `[n] url` 줄)만 교체하고 나머지는 보존. SKILL.md:203-204는 "idempotent — safe to re-run"이라고 안내하고, :244-245는 직접 편집 대신 이 명령을 쓰라고 권장함
- 재현: `review/test_sources_review.py::Defects::test_defect_replace_in_deletes_content_after_sources_block`
- 수정 방향: 제목 다음의 연속된 `_SOURCE_LINE_RE`/빈 줄/인용(`    > `) 줄까지만 블록으로 보고 그 범위만 교체. 또는 블록 뒤에 비(非)블록 내용이 있으면 쓰기를 거부

### F2. 코드 펜스 안의 `Sources:` 줄에서 초안 절단 — 검증된 결함, P2

- 위치: `sources.py:342-346`, `:375-379` (제목 탐색이 펜스를 무시하지 않음. 펜스 처리는 :357-364의 본문 단계에만 있음)
- 트리거: 본문의 ```` ```text ```` 블록 안에 `Sources:` 한 줄이 있는 초안에 `render --replace-in`
- 관찰: 펜스 안의 줄을 "마지막 Sources 제목"으로 인식해 그 뒤 본문(`Later body text…`)을 삭제. `verify`도 같은 위치에서 본문/블록을 잘못 나눔
- 기대: 펜스 안의 줄은 제목 후보에서 제외
- 재현: `test_defect_sources_line_in_code_fence_truncates_draft`
- 수정 방향: 제목 탐색 루프에서 `_FENCE_RE` 상태를 추적해 펜스 내부를 건너뜀(두 함수가 공유하는 헬퍼 하나로 정리)

### F3. footnotes/bibtex 스타일의 `--replace-in`이 멱등이 아님 — 검증된 결함, P2

- 위치: `sources.py:302-315` (해당 스타일은 `Sources` 제목을 출력하지 않음), `:368-382`
- 트리거: `render --style footnotes --replace-in draft.md`를 3번 실행
- 관찰: `[^1]: https://example.com/a` 줄이 3번 누적됨. bibtex도 같은 구조
- 기대: SKILL.md:203-204의 "idempotent" 설명대로 1회만 존재
- 재현: `test_defect_footnotes_replace_in_not_idempotent`
- 수정 방향: 제목이 없는 스타일과 `--replace-in` 조합을 거부하거나, 블록을 감지 가능한 마커로 감싸기

### F4. 괄호 포함 URL이 자체 렌더 결과의 `verify`에 실패 — 검증된 결함, P2

- 위치: `sources.py:54` (`_URL_IN_TEXT_RE`가 `)`를 제외), `:352-353`, `:441-445`
- 트리거: `add https://en.example.org/wiki/Python_(language)` → `render --replace-in` → `verify`
- 관찰: 블록 URL이 `...Python_(language`로 잘려 `FAIL: Sources block URL for [1] does not match the ledger`, exit 1
- 기대: 도구가 직접 렌더링한 블록은 항상 검증 통과(위키백과형 URL은 흔함)
- 재현: `test_defect_url_with_parentheses_fails_own_render`
- 수정 방향: 블록 줄에서는 `_SOURCE_LINE_RE`의 `(\S+)` 그룹을 우선 사용하거나, 괄호 균형을 맞춘 URL 정규식 사용

### F5. 번역 README의 컬렉션 표 누락 — 검증된 결함, P3

- 위치: `README.ko.md:11-25`, `README.ja.md:11-25`, `README.zh-CN.md:11-25` (영문 `README.md:25,27`에는 있음)
- 트리거/관찰: `durable-operations`, `local-audio-transcription`이 한/일/중 README 표에 없음. 각 README는 "위 표의 이름을 사용"하라고 안내함
- 기대: `catalog.json`의 17개 컬렉션과 일치
- 재현: `python3 -I review/check_consistency.py`
- 수정 방향: 표 두 줄 추가. 체크 스크립트를 CI나 기여 절차에 넣으면 재발 방지

### F6. `catalog.json` 저장소 URL 불일치 — 검증된 결함, P3

- 위치: `catalog.json:3` `https://github.com/bumboo/hermes-skill-library`
- 관찰: README 4종의 clone URL과 저작자 표기는 `Bum-Boo/hermes-skill-library`. GitHub 계정명에서 `bumboo`와 `bum-boo`는 서로 다른 이름이므로 기계 판독 소비자가 다른(또는 미래에 선점될 수 있는) 계정으로 안내될 수 있음
- 수정 방향: `https://github.com/Bum-Boo/hermes-skill-library`로 통일. 스킬 `author` 필드의 `bumboo`는 표기 문제일 뿐이라 선택 사항

### F7. 지침 모순·외부 참조·고정 경로 — 정적 위험, P3

1. `skills/research/grounded-citations/SKILL.md:28-30`은 학술 논문에 "`arxiv` 스킬"을 쓰라고 하지만, `references/citation-formats.md:54-59`는 "`grounded-citations` 스킬로 넘기라"고 하며 자기 자신을 가리킴(순환·모순). 한쪽으로 통일 필요.
2. `related_skills: [arxiv, pdf, reddit-reading, rss-feeds, youtube-content]` (SKILL.md:12)와 본문의 `latex-pdf-report`, `docx`, `powerpoint`, `llm-wiki`, `xurl`은 이 라이브러리에 없음. Hermes 공식 스킬이 설치되지 않은 환경에서는 존재하지 않는 스킬을 안내함. "선택적 외부 스킬"이라고 명시하는 것을 권장.
3. SKILL.md:59 `S=~/.hermes/skills/research/grounded-citations/scripts/sources.py`는 기본 대상만 가정함. README가 안내하는 프로필별 설치(`~/.hermes/profiles/<profile>/skills`)에서는 이 경로가 없거나, 더 나쁜 경우 다른(오래된) 사본을 실행함. 스킬 디렉터리 기준 상대 경로 사용을 권장.
4. 메타데이터 형식 불균일(동작 영향 없음): `local-artifact-recovery`, `local-audio-transcription`, `collaborative-visual-editor-architecture`는 `metadata.hermes.category`를 쓰고 `related_skills`가 없으며, description이 다른 스킬과 달리 "Use when…"으로 시작하지 않음. 자동 스킬 선택 품질에 영향을 줄 수 있음.

### F8. 잠금 타임아웃 시 살아 있는 보유자의 잠금 탈취 — 검증된 결함, P3

- 위치: `sources.py:129-135`, `:144-147`
- 트리거: 한 프로세스가 잠금을 잡고 있는 동안, 다른 프로세스가 5초(테스트에서는 0.1초) 이상 대기
- 관찰: 잠금 파일을 "stale"로 간주해 삭제하고 획득함. 두 쓰기 주체가 동시에 진행하면 `add_sources`의 `len(sources)+1`(:185)이 같은 id를 줄 수 있음. 또 `unlink` 실패 경로(:133-134)는 잠금 없이 진행한 뒤 `__exit__`에서 남의 잠금을 지움
- 기대: 주석(:108-114)이 "best-effort"라고 밝히고 있어 의도된 절충이지만, SKILL.md:233-235는 병렬 서브에이전트에 같은 ledger를 공유하라고 권장함
- 재현: `test_defect_lock_stolen_from_live_holder`
- 수정 방향: 잠금 파일에 PID/시각을 기록하고 mtime이 충분히 오래됐을 때만 제거. POSIX에서는 `fcntl.flock` 사용

### F9. `render --only 1-`에서 traceback — 검증된 결함, P3

- 위치: `sources.py:511-513`
- 관찰: `ValueError: invalid literal for int()` traceback
- 수정 방향: `argparse` 오류로 변환해 exit 2

### F10. 전체 설치가 번들 스킬을 덮어쓸 가능성 — 정적 위험, P2 (미검증)

- 위치: `scripts/install.sh:8`, `skills/research/grounded-citations/SKILL.md:5` (`author: Hermes Agent + Teknium`, `version: 1.2.0`)
- 추론: 이 스킬은 Hermes Agent 공식 스킬을 가져온 것으로 보임. 대상 `~/.hermes/skills/research/grounded-citations/`에 공식 번들 사본이 있다면 `install.sh`가 확인 없이 덮어쓰고, 이후 공식 업데이트와 버전이 엇갈릴 수 있음. 네트워크/실제 Hermes 설치 없이 진행한 리뷰라 Hermes가 번들 스킬을 이 경로에 배치하는지는 확인하지 않았음
- 수정 방향: 설치 전 대상에 같은 이름의 `SKILL.md`가 있고 내용이 다르면 경고하거나 `--force`를 요구. 또는 이 스킬을 공식 스킬 설치 명령으로 안내

---

## 이미 다뤄졌거나 문제 아님

- **설치 재실행(문제 아님)**: `install.sh`와 17개 컬렉션 모두 2회 연속 실행 시 결과 바이트가 동일하고, 컬렉션 설치 경로 구조가 전체 설치와 같음(공백이 들어간 대상 경로 포함). 재현: `test_install_rerun.sh`.
- **사용자 수정 파일 덮어쓰기(이미 문서화)**: 재실행하면 로컬에서 수정한 `SKILL.md`를 조용히 덮어씀. README 4종의 경고문(예: `README.ko.md` "설치 스크립트는 … 덮어쓸 수 있습니다")이 다루고 있음.
- **오래된 파일 잔존(P3, 참고)**: `cp -R`은 정리하지 않으므로 이전 버전에서 삭제된 파일이 남음. Hermes는 `SKILL.md`를 읽으므로 영향이 작지만, 스크립트가 이름을 바꾸면 옛 스크립트가 남을 수 있음.
- **알 수 없는 컬렉션(P3, 참고)**: exit 2로 정상 실패하지만, `scripts/install-collection.sh:14`의 `mkdir -p`가 `case`보다 먼저 실행되어 빈 대상 디렉터리를 만듦. `mkdir`을 각 분기 뒤로 옮기면 해결됨.
- **대상 = 저장소 `skills/`(문제 아님)**: `cp`가 "same file" 오류로 exit 1, 손상 없음.
- **메타데이터 기본 검사(통과)**: 28개 스킬 모두 frontmatter가 YAML로 파싱되고 `name` == 디렉터리명이며 이름 중복이 없음. catalog ↔ 설치 스크립트 `case`/사용법 문자열 ↔ `collections/` 디렉터리 ↔ 각 컬렉션 README 스킬 목록이 모두 일치하고, 어느 컬렉션에도 속하지 않은 스킬이 없음. 저장소 내부 상대 링크 중 깨진 링크가 없음.
- **비밀값/개인 경로(통과)**: `skills/`, `collections/`에서 `rm -rf`, `reset --hard`, 강제 push, `/home/<user>`, `/Users/<user>`, 토큰 형태 문자열을 grep한 결과 0건.
- **`render --replace-in`의 markdown 스타일 멱등성, `add` 정규화, `quote`의 의역 거부(이미 동작)**: `Covered` 테스트 3개 통과.
- **`__pycache__`(문제 아님)**: 저장소 안에서 `sources.py`를 실행하면 `scripts/__pycache__`가 생기고 다음 설치 때 함께 복사되지만 `.gitignore`에 포함돼 있고 무해함.

## 사용한 정확한 명령

```bash
cd hermes-skill-library
git log --oneline | head -5
python3 -I review/check_consistency.py            # 메타데이터/카탈로그/링크
bash review/test_install_rerun.sh                  # HOME을 mktemp로 격리한 설치 재실행 검사
python3 -m unittest discover -s review -p "test_*.py" -v
grep -rnE 'rm -rf|rm -r |--force|git push -f|reset --hard|/home/[a-z]|/Users/[A-Za-z]|ghp_|sk-[A-Za-z0-9]{10}|chat_id' skills collections
```

환경: Linux, Python 3.13.18, PyYAML 6.0.3, GNU coreutils `cp`.
