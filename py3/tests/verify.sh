#!/bin/bash -i
#

# Safety check: must run from a directory named "tests" — the cleanup step
# rm -rf's AI-collaboration files, which would destroy real work if run
# from a non-tests directory by mistake.
if [[ "$(basename "$PWD")" != "tests" ]]; then
    echo "ERROR: verify.sh must be run from a directory named 'tests'." >&2
    echo "  Current PWD: $PWD" >&2
    echo "  The initial cleanup step would delete AI-collaboration files." >&2
    exit 1
fi

# Start from a known-clean state (silent — matches may be absent).
# Also wipe cwdConfig (.aiActivity.cs/) so bare-invocation tests
# can distinguish "activity persisted this run" from "leftover from
# earlier run."
lpDo eval rm -rf .claude AI-*.org CLAUDE.md AI-*.dormant CLAUDE.md.dormant .aiActivity.cs 2\>/dev/null

lpDo ls -a -C -F

lpDo aiActivity.cs -i userConfig_set --parName="templates" --parValue="/bisos/apps/defaults/ai-templates"           # BISOS DEFAULT
lpDo aiActivity.cs -i userConfig_get --parName="templates"
lpDo aiActivity.cs -i initiate --activity="xu-single"           # Install xu-single templates (auto-persists activity to cwdConfig)
lpDo ls -a -C -F
lpDo readlink AI-Outputs.org           # EXPECT: mother/AI-Outputs.org (installed by initiate)
lpDo cat .aiActivity.cs/fps/activity/value           # EXPECT: xu-single (auto-persisted)
lpDo aiActivity.cs -i deClaudify           # Remove AI files from current directory
lpDo ls -a -C -F           # EXPECT: AI-Outputs.org removed
# Bare initiate — activity resolved from cwdConfig (no --activity flag).
lpDo aiActivity.cs -i initiate           # EXPECT: uses activity=xu-single from cwdConfig
lpDo ls -a -C -F
lpDo readlink AI-Outputs.org           # EXPECT: mother/AI-Outputs.org (reinstalled by bare initiate)

# refresh coverage — backfill: simulate a project initiated before
# AI-Outputs.org existed in templates (unlink it), then refresh should
# recreate the symlink without touching anything else.
lpDo eval rm -f AI-Outputs.org
lpDo aiActivity.cs -i refresh           # EXPECT: SYMLINKED (backfilled): .../AI-Outputs.org
lpDo readlink AI-Outputs.org           # EXPECT: mother/AI-Outputs.org (backfilled by refresh)

# refresh coverage — base mode: normal re-copy of an already-safe-copied CLAUDE.md
lpDo aiActivity.cs -i refresh           # EXPECT: REFRESHED CLAUDE.md
lpDo ls -a -C -F

# refresh coverage — legacy symlink upgrade: replace CLAUDE.md with a symlink,
# then refresh should unlink and safe-copy (UPGRADED).
lpDo eval rm -f CLAUDE.md
lpDo ln -s /bisos/apps/defaults/ai-templates/mother/CLAUDE.md CLAUDE.md
lpDo ls -a -C -F
lpDo aiActivity.cs -i refresh           # EXPECT: UPGRADED (legacy symlink -> safe-copy)
lpDo ls -a -C -F

lpDo aiActivity.cs -i deClaudify           # Remove AI files from current directory
lpDo ls -a -C -F
lpDo aiActivity.cs -i initiateSub --activity="xu-single"
lpDo readlink AI-Outputs.org           # EXPECT: mother/AI-Outputs.org (installed by initiateSub)
lpDo ls -a -C -F           # EXPECT: AI-Outputs.org IS here (symlinked) — unlike AI-WORKFLOW.org it is not @-imported, so walk-up won't find a parent's

# refresh coverage — sub mode: parent walk-up should detect sub, re-copy from
# mother/initiateSub/CLAUDE.md.
lpDo aiActivity.cs -i refresh           # EXPECT: MODE: sub; REFRESHED CLAUDE.md
lpDo ls -a -C -F

lpDo aiActivity.cs -i deClaudify           # Remove AI files from current directory
lpDo ls -a -C -F

# Negative-case tests for initiateSub — should refuse cleanly.
# 1. No initiated parent: run in a fresh /tmp dir outside the BISOS tree.
TMPDIR=$(mktemp -d)
lpDo pushd "$TMPDIR"
lpDo ls -a -C -F
lpDo aiActivity.cs -i initiateSub --activity="xu-single"           # EXPECT REFUSAL: No initiated parent found
lpDo ls -a -C -F
lpDo popd
lpDo eval rm -rf "$TMPDIR"

# Homogeneous repo: a sub follows its initiated ancestor's templates base, even
# when userConfig names a different tree (e.g. a fork).
lpDo aiActivity.cs -i userConfig_set --parName="templates" --parValue="/nonexistent/forkTemplates"           # simulate a userConfig pointing elsewhere
HOMOG=$(mktemp -d)
lpDo pushd "$HOMOG"
lpDo eval mkdir -p proj/sub
lpDo pushd proj
lpDo aiActivity.cs -i initiate --activity="xu-single" --templates="/bisos/apps/defaults/ai-templates"
lpDo pushd sub
lpDo aiActivity.cs -i initiateSub --activity="xu-single"           # EXPECT: success; templates taken from the ancestor, not userConfig
lpDo aiActivity.cs -i refresh           # EXPECT: MODE: sub
lpDo eval rm -f CLAUDE.md AI-Activity.org AI-DevStatus.org AI-WorkPlan.org
lpDo eval rm -rf .aiActivity.cs
# Heterogeneous: an explicit --templates naming another tree is honoured (a minimal second tree).
lpDo eval mkdir -p "$HOMOG/tplB/xu-single" "$HOMOG/tplB/mother/initiateSub"
lpDo eval cp /bisos/apps/defaults/ai-templates/mother/initiateSub/CLAUDE.md "$HOMOG/tplB/mother/initiateSub/"
lpDo eval cp /bisos/apps/defaults/ai-templates/xu-single/* "$HOMOG/tplB/xu-single/"
lpDo eval cp /bisos/apps/defaults/ai-templates/mother/AI-DevStatus.org /bisos/apps/defaults/ai-templates/mother/AI-WorkPlan.org "$HOMOG/tplB/mother/"
lpDo aiActivity.cs -i initiateSub --activity="xu-single" --templates="$HOMOG/tplB"           # EXPECT: success, note HETEROGENEOUS; AI-Activity.org links into tplB
lpDo readlink AI-Activity.org
lpDo aiActivity.cs -i refresh           # EXPECT: MODE: sub (cwdConfig now names tplB)
lpDo popd
lpDo popd
lpDo popd
lpDo eval rm -rf "$HOMOG"
lpDo aiActivity.cs -i userConfig_set --parName="templates" --parValue="/bisos/apps/defaults/ai-templates"           # restore BISOS DEFAULT
