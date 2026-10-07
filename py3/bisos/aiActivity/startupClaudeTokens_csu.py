# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= estimating the tokens Claude Code loads at session startup.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/auth/bxRepos/bisos-pip/aiActivity/py3/bisos/aiActivity/startupClaudeTokens_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['startupClaudeTokens_csu'], }
csInfo['version'] = '202610070000'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'startupClaudeTokens_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]]

Static (no runtime observation) estimate of what Claude Code reads into
context at session start from the current directory, broken down by source:

1. Managed policy =CLAUDE.md= (=/etc/claude-code/CLAUDE.md=)
2. User memory (=~/.claude/CLAUDE.md=, =~/.claude/rules/=)
3. Walk-up chain, filesystem root down to cwd: =CLAUDE.md=,
   =.claude/CLAUDE.md=, =CLAUDE.local.md=, unscoped =.claude/rules/*.md=
4. Auto-memory =MEMORY.md= (first 200 lines / 25KB)
5. Skill and slash-command descriptions (frontmatter only)

Every memory file is followed through its =@= imports (max 4 hops),
mirroring Claude Code: imports anywhere in a line, relative paths resolved
against the importing file's *real* path (symlinks resolved first), and
markdown code spans / fenced blocks skipped.

Separately listed, not added to the startup total: what loads *on demand*
--- =CLAUDE.md= overlays below cwd, path-scoped rules, =AI-Outputs.org=.

Tokens are estimated as chars/4. The system prompt and tool definitions are
a fixed overhead outside the project's control and are not measured.

Loading rules verified against code.claude.com/docs/en/memory.md and
skills.md on 2026-10-07.

Part of the *Claude binding*, not the agent-neutral core: everything here
encodes Claude Code's loading semantics, hence =Claude= in the name. A
binding for another agent would be a sibling module with its own rules.

** Status: In use with BISOS
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io

import collections
####+END:

import dataclasses
import pathlib
import re
import subprocess


# ---------------------------------------------------------------------------
# Claude Code loading limits (from the official docs, 2026-10-07)
# ---------------------------------------------------------------------------

maxImportHops = 4
maxMemoryFileBytes = 4 * 1024 * 1024        # larger CLAUDE.md files are skipped
autoMemoryMaxLines = 200
autoMemoryMaxBytes = 25 * 1024
skillDescMaxChars = 1536                     # description + when_to_use
charsPerToken = 4

managedPolicyPath = pathlib.Path('/etc/claude-code/CLAUDE.md')

# Directory names never descended into when looking for on-demand overlays.
onDemandPruneNames = {'node_modules', '__pycache__', 'venv', 'site-packages', }


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclasses.dataclass
class ContextItem:
    """One file (or file excerpt) that lands in context."""
    label: str                          # as displayed: path, or @ref as written
    resolved: typing.Optional[pathlib.Path]
    chars: int = 0
    depth: int = 0                      # import hop count; 0 = root memory file
    note: str = ''                      # symlink target, 'already loaded', 'truncated', ...
    group: bool = False                 # header line; chars = subtotal of the items below it

    @property
    def tokens(self) -> int:
        return tokensEstimate(self.chars)


@dataclasses.dataclass
class ContextSection:
    title: str
    items: typing.List[ContextItem] = dataclasses.field(default_factory=list)

    @property
    def tokens(self) -> int:
        return sum(item.tokens for item in self.items if not item.group)


def tokensEstimate(chars: int) -> int:
    return chars // charsPerToken


# ---------------------------------------------------------------------------
# @ import parsing
# ---------------------------------------------------------------------------

_fenceRe = re.compile(r'^\s*(```|~~~)')
_codeSpanRe = re.compile(r'`[^`\n]*`')
# @ not preceded by a word char or @ (so email addresses are not imports);
# the path runs to the first unescaped whitespace.
_importRe = re.compile(r'(?<![\w@])@((?:\\ |\S)+)')


def importRefsExtract(text: str) -> typing.List[str]:
    """Return the @ import references in text, in order, as written.

    Skips markdown fenced code blocks and inline code spans, as Claude Code does.
    """
    refs: typing.List[str] = []
    inFence = False
    for line in text.splitlines():
        if _fenceRe.match(line):
            inFence = not inFence
            continue
        if inFence:
            continue
        line = _codeSpanRe.sub('', line)
        refs.extend(m.group(1) for m in _importRe.finditer(line))
    return refs


def importRefResolve(
        ref: str,
        importingFile: pathlib.Path,
) -> pathlib.Path:
    """Resolve an @ reference relative to the importing file's real location."""
    refPath = pathlib.Path(ref.replace('\\ ', ' ')).expanduser()
    if not refPath.is_absolute():
        refPath = importingFile.resolve().parent / refPath
    return refPath


def _symlinkNote(path: pathlib.Path) -> str:
    if path.is_symlink():
        return f"-> {path.readlink()}"
    return ''


def _textRead(path: pathlib.Path) -> typing.Optional[str]:
    try:
        return path.read_text(encoding='utf-8', errors='replace')
    except OSError:
        return None


def memoryTreeCollect(
        path: pathlib.Path,
        label: str,
        seen: typing.Set[pathlib.Path],
        items: typing.List[ContextItem],
        depth: int = 0,
        extraNote: str = '',
) -> None:
    """Append path and (recursively) its @ imports to items.

    seen holds resolved paths already loaded; a repeat is listed with zero
    chars and an 'already loaded' note so the reader can see the edge.
    extraNote is appended to this item's note (e.g. a symlink-resolution warning).
    """
    resolved = path.resolve()
    if resolved in seen:
        items.append(ContextItem(label, resolved, 0, depth, 'already loaded'))
        return
    if not resolved.is_file():
        return
    if resolved.stat().st_size > maxMemoryFileBytes:
        items.append(ContextItem(label, resolved, 0, depth, 'skipped: over 4MiB'))
        return
    text = _textRead(resolved)
    if text is None:
        return
    seen.add(resolved)
    note = ' '.join(filter(None, [_symlinkNote(path), extraNote]))
    items.append(ContextItem(label, resolved, len(text), depth, note))
    if depth >= maxImportHops:
        return
    for ref in importRefsExtract(text):
        target = importRefResolve(ref, path)
        if not target.resolve().is_file():
            continue
        # A relative import inside a symlinked file resolves against the
        # symlink's target directory, not the project --- usually a mistake
        # (the Stage 11 CLAUDE.md bug class). Say so.
        childNote = ''
        if path.is_symlink() and not pathlib.Path(ref).expanduser().is_absolute():
            if target.parent != path.parent.resolve():
                childNote = f"!! resolved via symlink into {target.parent}"
        memoryTreeCollect(target, f"@{ref}", seen, items, depth + 1, childNote)


# ---------------------------------------------------------------------------
# Frontmatter (rules path-scoping; skill / command descriptions)
# ---------------------------------------------------------------------------

def frontmatterGet(text: str) -> typing.Dict[str, str]:
    """Minimal YAML-frontmatter reader: top-level key -> raw value text.

    Continuation lines (indented) are appended to the preceding key. Good
    enough for sizing descriptions; not a YAML parser.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return {}
    result: typing.Dict[str, str] = {}
    currentKey: typing.Optional[str] = None
    for line in lines[1:]:
        if line.strip() == '---':
            break
        keyMatch = re.match(r'^([A-Za-z_][\w-]*):\s?(.*)$', line)
        if keyMatch:
            currentKey = keyMatch.group(1)
            result[currentKey] = keyMatch.group(2)
        elif currentKey is not None:
            result[currentKey] += '\n' + line.strip()
    return result


def _isPathScopedRule(text: str) -> bool:
    return 'paths' in frontmatterGet(text)


def _describedItem(
        path: pathlib.Path,
        label: str,
) -> typing.Optional[ContextItem]:
    """ContextItem sized by name + description + when_to_use, capped."""
    text = _textRead(path)
    if text is None:
        return None
    front = frontmatterGet(text)
    desc = front.get('description', '') + front.get('when_to_use', '')
    if not desc:
        # No description: Claude falls back to the body's first line.
        desc = next((line for line in text.splitlines() if line.strip()), '')
    chars = len(front.get('name', label)) + min(len(desc), skillDescMaxChars)
    return ContextItem(label, path.resolve(), chars, 0, '')


# ---------------------------------------------------------------------------
# Location helpers
# ---------------------------------------------------------------------------

def gitRootGet(cwd: pathlib.Path) -> typing.Optional[pathlib.Path]:
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--show-toplevel'],
            cwd=cwd, capture_output=True, text=True, check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return pathlib.Path(result.stdout.strip())


def ancestorsGet(cwd: pathlib.Path) -> typing.List[pathlib.Path]:
    """Filesystem root first, cwd last --- Claude Code's load order."""
    return list(reversed([cwd, *cwd.parents]))


def autoMemoryPathGet(cwd: pathlib.Path) -> typing.Optional[pathlib.Path]:
    """Locate the auto-memory MEMORY.md for this project, if any.

    Claude Code keys the project dir on a path with non-alphanumerics
    replaced by '-'. Tries the git root first, then cwd.
    """
    projectsDir = pathlib.Path.home() / '.claude' / 'projects'
    gitRoot = gitRootGet(cwd)
    for candidate in [gitRoot, cwd]:
        if candidate is None:
            continue
        key = re.sub(r'[^A-Za-z0-9]', '-', str(candidate))
        memoryMd = projectsDir / key / 'memory' / 'MEMORY.md'
        if memoryMd.is_file():
            return memoryMd
    return None


def _labelFor(path: pathlib.Path, cwd: pathlib.Path) -> str:
    try:
        return str(path.relative_to(cwd))
    except ValueError:
        return str(path)


def _rulesFiles(claudeDir: pathlib.Path) -> typing.List[pathlib.Path]:
    rulesDir = claudeDir / 'rules'
    if not rulesDir.is_dir():
        return []
    return sorted(rulesDir.rglob('*.md'))


# ---------------------------------------------------------------------------
# Gathering
# ---------------------------------------------------------------------------

def startupSectionsGather(
        cwd: pathlib.Path,
        seen: typing.Set[pathlib.Path],
) -> typing.List[ContextSection]:
    """Everything loaded at session start, in Claude Code's order."""
    sections: typing.List[ContextSection] = []
    userClaudeDir = pathlib.Path.home() / '.claude'

    managed = ContextSection('Managed policy')
    if managedPolicyPath.is_file():
        memoryTreeCollect(managedPolicyPath, str(managedPolicyPath), seen, managed.items)
    sections.append(managed)

    user = ContextSection('User memory (~/.claude)')
    memoryTreeCollect(userClaudeDir / 'CLAUDE.md', '~/.claude/CLAUDE.md', seen, user.items)
    for rule in _rulesFiles(userClaudeDir):
        if not _isPathScopedRule(_textRead(rule) or ''):
            memoryTreeCollect(rule, f"~/.claude/rules/{rule.name}", seen, user.items)
    sections.append(user)

    chain = ContextSection('Walk-up chain (/ down to cwd)')
    for directory in ancestorsGet(cwd):
        candidates = [
            directory / 'CLAUDE.md',
            directory / '.claude' / 'CLAUDE.md',
            directory / 'CLAUDE.local.md',
        ]
        candidates += [
            rule for rule in _rulesFiles(directory / '.claude')
            if not _isPathScopedRule(_textRead(rule) or '')
        ]
        for candidate in candidates:
            if candidate.is_file():
                memoryTreeCollect(candidate, _labelFor(candidate, cwd), seen, chain.items)
    sections.append(chain)

    autoMemory = ContextSection('Auto-memory MEMORY.md')
    memoryMd = autoMemoryPathGet(cwd)
    if memoryMd is not None:
        text = _textRead(memoryMd) or ''
        loaded = '\n'.join(text.splitlines()[:autoMemoryMaxLines])
        loaded = loaded.encode('utf-8')[:autoMemoryMaxBytes].decode('utf-8', errors='ignore')
        note = 'truncated' if len(loaded) < len(text.rstrip('\n')) else ''
        autoMemory.items.append(ContextItem(str(memoryMd), memoryMd, len(loaded), 0, note))
    sections.append(autoMemory)

    # Skills / commands: discovered from cwd up to the repo root, plus ~/.claude.
    gitRoot = gitRootGet(cwd) or cwd
    claudeDirs = [userClaudeDir]
    claudeDirs += [d / '.claude' for d in ancestorsGet(cwd) if d == gitRoot or gitRoot in d.parents]
    descSection = ContextSection('Skill + command descriptions')
    seenDescs: typing.Set[pathlib.Path] = set()
    for claudeDir in claudeDirs:
        for subDir, pattern in (('skills', '*/SKILL.md'), ('commands', '*.md')):
            descDir = claudeDir / subDir
            if not descDir.is_dir():
                continue
            # Header names the directory and, when it is a symlink (the usual
            # case under initiate), where it points --- i.e. which templates
            # tree and activity supplied these skills/commands.
            header = ContextItem(_labelFor(descDir, cwd), descDir.resolve(), 0, 0,
                                 _symlinkNote(descDir), group=True)
            descSection.items.append(header)
            for descFile in sorted(descDir.glob(pattern)):
                if descFile.resolve() in seenDescs:
                    continue
                seenDescs.add(descFile.resolve())
                name = descFile.parent.name if subDir == 'skills' else descFile.stem
                item = _describedItem(descFile, name)
                if item is not None:
                    item.depth = 1
                    header.chars += item.chars
                    descSection.items.append(item)
            if header.chars == 0:
                descSection.items.remove(header)
    sections.append(descSection)

    return sections


def onDemandSectionGather(
        cwd: pathlib.Path,
        seen: typing.Set[pathlib.Path],
) -> ContextSection:
    """Files that load only when Claude touches them; not part of startup."""
    section = ContextSection('On demand (not in startup total)')

    def walk(directory: pathlib.Path) -> None:
        try:
            entries = sorted(directory.iterdir())
        except OSError:
            return
        for entry in entries:
            if not entry.is_dir() or entry.is_symlink():
                continue
            if entry.name.startswith('.') or entry.name in onDemandPruneNames:
                continue
            for name in ('CLAUDE.md', 'CLAUDE.local.md'):
                overlay = entry / name
                if overlay.is_file():
                    memoryTreeCollect(overlay, _labelFor(overlay, cwd), seen, section.items)
            walk(entry)

    walk(cwd)

    for directory in ancestorsGet(cwd):
        for rule in _rulesFiles(directory / '.claude'):
            if _isPathScopedRule(_textRead(rule) or ''):
                memoryTreeCollect(rule, _labelFor(rule, cwd), seen, section.items)
        outputs = directory / 'AI-Outputs.org'
        if outputs.is_file():
            memoryTreeCollect(outputs, _labelFor(outputs, cwd), seen, section.items)

    return section


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def reportLines(
        sections: typing.List[ContextSection],
        onDemand: ContextSection,
        heaviestCount: int = 5,
) -> typing.List[str]:
    lines: typing.List[str] = []
    startupTotal = sum(section.tokens for section in sections)

    def itemLine(item: ContextItem) -> str:
        indent = '  ' * item.depth
        note = f"  {item.note}" if item.note else ''
        return f"  {item.tokens:>8,}  {indent}{item.label}{note}"

    for section in [*sections, onDemand]:
        lines.append(f"{section.title}: ~{section.tokens:,} tokens")
        if not section.items:
            lines.append("            (none)")
        for item in section.items:
            lines.append(itemLine(item))
        lines.append('')

    loadedItems = [item for section in sections for item in section.items
                   if item.chars and not item.group]
    heaviest = sorted(loadedItems, key=lambda item: item.chars, reverse=True)[:heaviestCount]
    lines.append("Heaviest at startup:")
    for item in heaviest:
        share = 100 * item.tokens / startupTotal if startupTotal else 0
        lines.append(f"  {item.tokens:>8,}  {share:4.1f}%  {item.resolved}")
    lines.append('')
    lines.append(f"Startup total (estimate, chars/{charsPerToken}): ~{startupTotal:,} tokens")
    lines.append("  + fixed overhead not measured: system prompt, tool definitions")
    return lines


####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /examples_csu/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Examples of startupClaudeTokens commands.
    #+end_org """
    od = collections.OrderedDict
    cmnd = cs.examples.cmndEnter

    cs.examples.menuChapter('=startupClaudeTokens= -- estimate tokens Claude Code loads at session start from cwd')
    cmnd('startupClaudeTokens',
         pars=od([]),
         comment="# Per-source breakdown: walk-up chain + @ imports, memory, skills; on-demand listed apart")


def commonParamsSpecify(csParams: cs.param.CmndParamDict) -> None:
    pass


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "startupClaudeTokens" :comment "Estimate tokens Claude Code loads at session start" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<startupClaudeTokens>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class startupClaudeTokens(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Estimate the tokens Claude Code loads at session start from cwd.
Lists each source (managed policy, user memory, walk-up =CLAUDE.md= chain with
=@= imports, auto-memory, skill/command descriptions) with a chars/4 token
estimate, then the on-demand files separately, then the heaviest items.
Read-only.
        #+end_org """)

        cwd = pathlib.Path.cwd()
        seen: typing.Set[pathlib.Path] = set()
        sections = startupSectionsGather(cwd, seen)
        onDemand = onDemandSectionGather(cwd, seen)

        for line in reportLines(sections, onDemand):
            print(line)

        startupTotal = sum(section.tokens for section in sections)
        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults={
                'startupTokens': startupTotal,
                'onDemandTokens': onDemand.tokens,
                'bySection': {section.title: section.tokens for section in sections},
            },
        )
