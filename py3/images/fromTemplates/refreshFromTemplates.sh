#!/bin/bash
#
# Copy the rendered workflow figures from the templates tree (bisos/defaults) into this
# directory, for inclusion in bisos.aiActivity's README.org. Copies only; renders nothing:
# regenerate them at the source first (ai-templates/_nonTemplate_/images/*-graphviz.pcs).
# Usually run from the source side by its aiActivityFiguresPush.sh (a push); runnable here
# too (a pull). One implementation for both. See ./README.org.

src=/bisos/git/bxRepos/bisos/defaults/ai-templates/_nonTemplate_/images
dst=$(cd "$(dirname "$0")" && pwd)
figures="aiStartupWorkflow aiUsageWorkflow aiGeneralTree aiEcosystemTree"

for f in $figures ; do
    if [ ! -f "$src/$f.png" ] ; then
        echo "MISSING: $src/$f.png" >&2
        exit 1
    fi
done

changed=0
for f in $figures ; do
    if cmp -s "$src/$f.png" "$dst/$f.png" ; then
        echo "unchanged: $f.png"
    else
        cp -p "$src/$f.png" "$dst/$f.png"
        echo "copied:    $f.png"
        changed=$((changed + 1))
    fi
done

srcRepo=$(git -C "$src" rev-parse --show-toplevel)
srcSha=$(git -C "$src" rev-parse --short HEAD)
echo
echo "Source: $srcRepo at $srcSha"
if [ -n "$(git -C "$src" status --short -- .)" ] ; then
    echo "WARNING: the source images directory has uncommitted changes:"
    git -C "$src" status --short -- . | sed 's/^/    /'
    echo "         these copies come from its working tree, not from $srcSha."
fi

if [ "$changed" -gt 0 ] ; then
    cat <<EOF

$changed figure(s) copied. Still to do:
  1. Update "Last copied" in $dst/README.org (date, and $srcSha).
  2. If ai-templates/_nonTemplate_/images/aiUsageWorkflow.org changed, re-paste its
     read/write table into bisos.aiActivity's README.org (see ./README.org).
  3. bisos.aiActivity needs a commit + push.
  4. The templates repo ($srcRepo) needs a commit + push as well,
     so the copies match a published source.
EOF
fi
