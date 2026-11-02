#!/bin/bash
#
# Checks aiActivity.cs -i activityReport and -i sessionRootCheck (activityModel_csu) on a
# scratch tree: a root, a homogeneous and a heterogeneous sub, a nested root, a sub without a
# root, a plain directory. Prints PASS/FAIL per check; exit 1 when any fails. Writes only in mktemp.

t=$(mktemp -d) || exit 1
trap 'rm -rf "$t"' EXIT
t=$(cd "$t" && pwd -P)

mkRoot() { mkdir -p "$1/.claude/skills.real" && touch "$1/CLAUDE.md" "$1/AI-WORKFLOW.org" \
               && ln -s skills.real "$1/.claude/skills"; }
mkSub()  { mkdir -p "$1" && touch "$1/CLAUDE.md"; }

mkRoot "$t/repoA"
mkSub  "$t/repoA/subHomo"
mkSub  "$t/repoA/subHetero" && mkdir -p "$t/other/skills" "$t/repoA/subHetero/.claude" \
    && ln -s "$t/other/skills" "$t/repoA/subHetero/.claude/skills"
mkRoot "$t/repoA/nestedRoot"
mkRoot "$t/repoB"
mkSub  "$t/orphanSub"
mkdir -p "$t/plain"

fails=0
check() {   # check <description> <expected regexp> <command...>
    local what="$1" expect="$2"; shift 2
    local out; out=$("$@" 2>&1)
    if grep -Eq -- "$expect" <<< "$out"; then echo "PASS: $what"
    else echo "FAIL: $what"; echo "  expected: $expect"; echo "$out" | sed 's/^/  got: /'; fails=$((fails+1)); fi
}
rep() { aiActivity.cs -i activityReport "$@"; }
chk() { aiActivity.cs -i sessionRootCheck "$@"; }

check "root is root"                 '^kind: +root'          rep "$t/repoA"
check "root is native to itself"     '^relation: +native'    rep --sessionRoot="$t/repoA" "$t/repoA"
check "plain subdir: its root"       "^aiActivity: +$t/repoA\$" rep "$t/repoA/.claude"
check "homogeneous sub"              '^homogeneity: +homogeneous' rep "$t/repoA/subHomo"
check "heterogeneous sub"            '^homogeneity: +heterogeneous' rep "$t/repoA/subHetero"
check "sub native under its root"    '^relation: +native'    rep --sessionRoot="$t/repoA" "$t/repoA/subHomo"
check "sub foreign from repoB"       '^relation: +foreign'   rep --sessionRoot="$t/repoB" "$t/repoA/subHomo"
check "nested root: its own home"    "^home: +$t/repoA/nestedRoot\$" rep "$t/repoA/nestedRoot"
check "nested root: nestedIn"        "^nestedIn: +$t/repoA\$" rep "$t/repoA/nestedRoot"
check "nested root: foreign, warned" 'foreign although under the Session-Root' \
                                     rep --sessionRoot="$t/repoA" "$t/repoA/nestedRoot"
check "sub without a root: warned"   'no AI-Activity Root above the sub' rep "$t/orphanSub"
check "plain dir: kind none"         '^kind: +none'          rep "$t/plain"
check "invalid Session-Root warned"  'is not an AI-Activity Root' rep --sessionRoot="$t/repoA/subHomo" "$t/repoA"
check "no nested warning for an invalid root" "^relation: +foreign\$" rep --sessionRoot="$t" "$t/repoA"
check "json output"                  '"relation": "foreign"' rep --format=json --sessionRoot="$t/repoB" "$t/repoA"
check "rule 1: root OK"              '^OK: '                 chk "$t/repoA"
check "rule 1: sub refused, names root" "^REFUSED: .* sub-AI-Activity; the nearest AI-Activity Root above is $t/repoA\$" \
                                     chk "$t/repoA/subHomo"
check "rule 1: plain dir refused"    '^REFUSED: .* not an AI-Activity; no AI-Activity Root above it' chk "$t/plain"
check "rule 1: not a directory"      '^REFUSED: not a directory' chk "$t/missing"

echo "$fails failed"
[ "$fails" -eq 0 ]
