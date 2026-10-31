#!/usr/bin/env bash
# Synthetic re-run checks for scripts/install.sh and scripts/install-collection.sh.
# Uses only a mktemp sandbox; HOME is redirected so the default target is never touched.
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SB="$(mktemp -d)"; trap 'rm -rf "$SB"' EXIT
export HOME="$SB/home"; mkdir -p "$HOME"
pass=0; fail=0
ok()  { echo "PASS: $*"; pass=$((pass+1)); }
bad() { echo "FAIL: $*"; fail=$((fail+1)); }
snap() { (cd "$1" && find . -type f -print0 | sort -z | xargs -0 sha256sum); }

# 1. default target + idempotent re-run
"$ROOT/scripts/install.sh" >/dev/null && a="$(snap "$HOME/.hermes/skills")"
"$ROOT/scripts/install.sh" >/dev/null && b="$(snap "$HOME/.hermes/skills")"
[[ "$a" == "$b" && -n "$a" ]] && ok "install.sh re-run is byte-identical" || bad "install.sh re-run differs"
diff <(cd "$ROOT/skills" && find . -type f | sort) <(cd "$HOME/.hermes/skills" && find . -type f | sort) >/dev/null \
  && ok "install.sh copies exactly the repo skill tree" || bad "installed tree != repo tree"

# 2. every collection installs twice into a path with spaces, same layout as full install
for c in $(python3 -I -c 'import json,sys;print(" ".join(json.load(open(sys.argv[1]))["collections"]))' "$ROOT/catalog.json"); do
  T="$SB/col dir/$c"
  "$ROOT/scripts/install-collection.sh" "$c" "$T" >/dev/null && x="$(snap "$T")"
  "$ROOT/scripts/install-collection.sh" "$c" "$T" >/dev/null && y="$(snap "$T")"
  [[ "$x" == "$y" && -n "$x" ]] || { bad "collection $c re-run differs"; continue; }
  (cd "$T" && find . -name SKILL.md | while read -r s; do cmp -s "$s" "$ROOT/skills/$s" || echo "$s"; done) | grep -q . \
    && bad "collection $c path layout differs from install.sh" || ok "collection $c idempotent, layout matches"
done

# 3. user-edited and stale files on re-run (documented overwrite behaviour)
T="$SB/edit"; "$ROOT/scripts/install.sh" "$T" >/dev/null
echo "local note" >> "$T/gstack-safe/gstack-spec/SKILL.md"
echo stale > "$T/gstack-safe/gstack-spec/removed-upstream.md"
"$ROOT/scripts/install.sh" "$T" >/dev/null
grep -q "local note" "$T/gstack-safe/gstack-spec/SKILL.md" && bad "edit kept?" || echo "INFO: local edit to SKILL.md silently overwritten on re-run (README warns)"
[[ -f "$T/gstack-safe/gstack-spec/removed-upstream.md" ]] && echo "INFO: stale file from earlier install is kept (cp -R never prunes)"

# 4. unknown collection / missing arg must not create anything
T="$SB/unknown"; "$ROOT/scripts/install-collection.sh" nope "$T" 2>/dev/null; rc=$?
[[ $rc -eq 2 ]] && ok "unknown collection exits 2" || bad "unknown collection rc=$rc"
[[ -d "$T" ]] && echo "INFO: unknown collection still created empty target dir $T (mkdir runs before case)"
"$ROOT/scripts/install-collection.sh" >/dev/null 2>&1; [[ $? -eq 2 ]] && ok "missing arg exits 2" || bad "missing arg"

# 5. target == source tree
(cd "$SB" && cp -R "$ROOT" repo && ./repo/scripts/install.sh "$SB/repo/skills" >/dev/null 2>"$SB/err"); rc=$?
echo "INFO: install.sh into its own skills/ dir rc=$rc: $(head -c 160 "$SB/err")"

echo "summary: $pass passed, $fail failed"
[[ $fail -eq 0 ]]
