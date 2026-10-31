# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= for the local (desktop) VS Code, independent of Claude: the vscode layer,
=vscode.cs=. Also a library of =vscodeClaude_csu= (the Claude layer).
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
* *[[elisp:(org-cycle)][| Particulars |]]* :: This File, Authors, version
** This File: /bxRepos/bisos-pip/aiActivity/py3/bisos/aiActivity/vscode_csu.py
** File True Name: /bisos/git/auth/bxRepos/bisos-pip/aiActivity/py3/bisos/aiActivity/vscode_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inDev"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['vscode_csu'], }
csInfo['version'] = '202610290000'
csInfo['status']  = 'inDev'
csInfo['panel'] = 'vscode_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]]
The vscode layer (WorkPlan Stage 22): handing things to the local (desktop) VS Code running on this
host's X display, whether or not Claude is involved. Its =code --open-url= is what the Claude layer
(=vscodeClaude_csu=) sends its =/open= URI through; the X clipboard (=xclip=) and the paste (=xdotool=)
are what it falls back on for a session that is already open.

Desktop VS Code only: the remote VS Code server's =remote-cli/code= refuses =--open-url=. =DISPLAY= must
be that of the desktop VS Code: without it nothing reaches the running window, and =code= still exits 0.
Moved here from =claudeSessions.py= (WorkPlan 20.3.2).
** Status: inDev
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

from bisos.common import csParam  # used by the generated classHead bodies

import datetime
import getpass
import json
import os
import pathlib
import shlex
import shutil
import stat
import subprocess
import urllib.parse


# The desktop VS Code's install (the Debian package) and its user data. workspaceStorage/ is a
# VS Code internal, not a documented API (seen in 1.143.1): read here only.
desktopExe = pathlib.Path('/usr/share/code/code')
userDataDir = pathlib.Path.home() / '.config' / 'Code'
workspaceStorageDir = userDataDir / 'User' / 'workspaceStorage'


def codeEnv() -> typing.Dict[str, str]:
    """The environment code runs in: without VSCODE_IPC_HOOK_CLI.

    When it is set (a VS Code terminal), the desktop launcher defers to a remote-cli on PATH, which
    does not support --open-url and opens nothing on this host's display.
    """
    return {k: v for k, v in os.environ.items() if k != 'VSCODE_IPC_HOOK_CLI'}


def codeRun(args: typing.List[str]) -> subprocess.CompletedProcess:
    """Run code with args (codeEnv), output captured."""
    return subprocess.run(['code', *args], env=codeEnv(), capture_output=True, text=True, check=False)


def launcherKind() -> typing.Tuple[str, typing.Optional[str]]:
    """(desktop | remote-cli | other | none, the resolved path of code on PATH)."""
    found = shutil.which('code')
    if not found:
        return 'none', None
    resolved = pathlib.Path(found).resolve()
    if resolved.is_relative_to(desktopExe.parent):
        return 'desktop', str(resolved)
    if 'remote-cli' in resolved.parts:
        return 'remote-cli', str(resolved)
    return 'other', str(resolved)


def _procEnviron(pid: int) -> typing.Dict[str, str]:
    try:
        raw = pathlib.Path(f'/proc/{pid}/environ').read_bytes()
    except OSError:
        return {}
    return dict(item.split('=', 1) for item in raw.decode(errors='replace').split('\0') if '=' in item)


def desktopProcesses() -> typing.Tuple[typing.List[int], typing.List[str]]:
    """(the pids of the desktop VS Code main processes of this user, the DISPLAYs its processes run on).

    The same executable also runs VS Code's helpers (--type=...: Chromium rewrites their argv into one
    space-joined string, so it is searched as bytes) and, with ELECTRON_RUN_AS_NODE, the language
    servers. The main process's own environment cannot be read (Chromium overwrites that area too), but
    the extension host's children inherit it: the DISPLAYs are gathered from all of them.
    """
    mains: typing.List[int] = []
    displays: typing.Set[str] = set()
    for proc in pathlib.Path('/proc').iterdir():
        if not proc.name.isdigit():
            continue
        try:
            if proc.joinpath('exe').readlink() != desktopExe:
                continue
            cmdline = proc.joinpath('cmdline').read_bytes()
        except OSError:
            continue
        environ = _procEnviron(int(proc.name))
        if environ.get('DISPLAY'):
            displays.add(environ['DISPLAY'])
        if b'--type=' not in cmdline and not environ.get('ELECTRON_RUN_AS_NODE'):
            mains.append(int(proc.name))
    return sorted(mains), sorted(displays)


def displayHost(display: str) -> str:
    """:1.0 and :1 are the same X display."""
    return display.split('.')[0]


def displayProblem() -> typing.Optional[str]:
    """A usage-error message when DISPLAY is unset (naming the desktop VS Code's, if known), else None."""
    if os.environ.get('DISPLAY'):
        return None
    mains, displays = desktopProcesses()
    if displays:
        hint = f"the desktop VS Code runs on DISPLAY={displays[0]}"
    elif mains:
        hint = "a desktop VS Code is running, on an unknown display"
    else:
        hint = "no desktop VS Code is running"
    return f"DISPLAY is not set: give the desktop VS Code's display ({hint})"


def _uriPath(uri: str) -> str:
    """The local path of a file:// URI, else the URI as is."""
    parsed = urllib.parse.urlparse(uri)
    return urllib.parse.unquote(parsed.path) if parsed.scheme == 'file' else uri


def workspacesKnown() -> typing.List[typing.Tuple[float, str]]:
    """(last used, as an mtime, folder or workspace) per workspace VS Code has state for, newest first."""
    known = []
    if not workspaceStorageDir.is_dir():
        return known
    for entry in workspaceStorageDir.iterdir():
        try:
            spec = json.loads(entry.joinpath('workspace.json').read_text())
        except (OSError, ValueError):
            continue    # an empty window's state has no workspace.json
        target = spec.get('folder') or spec.get('workspace') or ''
        known.append((entry.stat().st_mtime, _uriPath(target)))
    return sorted(known, reverse=True)


def extensionsInstalled() -> typing.Optional[typing.List[typing.Tuple[str, str]]]:
    """(id, version) per installed extension, by code --list-extensions; None when code fails."""
    result = codeRun(['--list-extensions', '--show-versions'])
    if result.returncode != 0:
        return None
    return [tuple(line.split('@', 1)) if '@' in line else (line, '')
            for line in result.stdout.splitlines() if line.strip()]


def openUriCommand(uri: str) -> typing.List[str]:
    """The command openUriSend runs."""
    return ['code', '--open-url', uri]


def openUriSend(uri: str) -> subprocess.CompletedProcess:
    """Hand uri to the local (desktop) VS Code with code --open-url (codeEnv).

    DISPLAY must be that of the desktop VS Code: without it nothing reaches the running window, and
    code still exits 0.
    """
    return subprocess.run(openUriCommand(uri), env=codeEnv(), capture_output=True, text=True, check=False)


def focusCommand(name: typing.Optional[str] = None) -> typing.List[str]:
    """The command focusSend runs: activate the visible VS Code window whose title has name (any: the first)."""
    search = ['search', '--onlyvisible', '--class', 'code']
    if name:
        search += ['--name', name]
    return ['xdotool', *search, 'windowactivate', '--sync']


def focusSend(name: typing.Optional[str] = None) -> subprocess.CompletedProcess:
    return subprocess.run(focusCommand(name), capture_output=True, text=True, check=False)


def clipboardCommand() -> typing.List[str]:
    """The command clipboardSet runs (xclip, from rawBisos-sbom.pcs)."""
    return ['xclip', '-selection', 'clipboard']


def clipboardSet(text: str) -> subprocess.CompletedProcess:
    """Put text on the X clipboard of DISPLAY, for Ctrl+V.

    xclip stays in the background to serve the selection until something else takes it, so its
    output must not be captured: a pipe it inherits would keep run() waiting.
    """
    return subprocess.run(clipboardCommand(), input=text, text=True, check=False,
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def pasteCommand(delay: float = 0.5) -> typing.List[str]:
    """The command pasteSend runs (xdotool, from rawBisos-sbom.pcs).

    After delay (a reveal in VS Code is not immediate), activate the desktop VS Code window, wait
    until it has the focus, and press Ctrl+V. X sees the window only: whatever VS Code focused inside
    it receives the paste (for Claude: the panel's input box; tested by Mohsen, 2026-10-28, focus first
    in a source file). With several VS Code windows the first one found is used.
    """
    return ['xdotool', 'sleep', str(delay),
            'search', '--onlyvisible', '--class', 'code',
            'windowactivate', '--sync', 'key', '--clearmodifiers', 'ctrl+v']


def pasteSend(delay: float = 0.5) -> subprocess.CompletedProcess:
    """Paste the clipboard into the desktop VS Code window."""
    return subprocess.run(pasteCommand(delay), capture_output=True, text=True, check=False)


def returnCommand(delay: float = 0.5) -> typing.List[str]:
    """The command returnSend runs: as pasteCommand, but the key is Return (submits the prompt)."""
    return ['xdotool', 'sleep', str(delay),
            'search', '--onlyvisible', '--class', 'code',
            'windowactivate', '--sync', 'key', '--clearmodifiers', 'Return']


def returnSend(delay: float = 0.5) -> subprocess.CompletedProcess:
    """Press Return in the desktop VS Code window: whatever has the focus in it receives it."""
    return subprocess.run(returnCommand(delay), capture_output=True, text=True, check=False)


# The partner Emacs (Blee): one per user. b:vscode/init (blee/vscode-claude) writes the file with the
# Emacs's server socket and pid; kill-emacs-hook removes it. Readers check that it is alive: a stale
# file (dead pid, missing socket) counts as no partner. VS Code alone needs none of this.
partnerDir = pathlib.Path('/bisos/var/blee/vscode')


def partnerFile(user: typing.Optional[str] = None) -> pathlib.Path:
    return partnerDir / f"partner-{user or getpass.getuser()}.json"


def partnerRead() -> typing.Tuple[typing.Optional[typing.Dict[str, typing.Any]], str]:
    """(the live partner's entry, ''), or (None, why there is none)."""
    path = partnerFile()
    try:
        entry = json.loads(path.read_text())
        socket = entry['socket']
        pid = int(entry['pid'])
    except FileNotFoundError:
        return None, f"no partner file ({path})"
    except (OSError, ValueError, KeyError, TypeError) as err:
        return None, f"unreadable partner file {path}: {err}"
    try:
        exe = pathlib.Path(f'/proc/{pid}/exe').readlink().name
    except OSError:
        return None, f"stale partner file {path}: no process {pid}"
    if not exe.startswith('emacs'):
        return None, f"stale partner file {path}: process {pid} is {exe}, not emacs"
    try:
        if not stat.S_ISSOCK(os.stat(socket).st_mode):
            return None, f"stale partner file {path}: {socket} is not a socket"
    except OSError:
        return None, f"stale partner file {path}: no socket {socket}"
    return entry, ''


def elispString(text: str) -> str:
    """text as an elisp string literal (JSON's string syntax is a subset of elisp's, with ASCII only)."""
    return json.dumps(text, ensure_ascii=True)


def emacsEvalCommand(socket: str, form: str) -> typing.List[str]:
    return ['emacsclient', '-s', socket, '--eval', form]


def emacsEval(socket: str, form: str, timeout: float = 10) -> typing.Optional[subprocess.CompletedProcess]:
    """Evaluate form in the Emacs of socket; None when it does not answer within timeout."""
    try:
        return subprocess.run(emacsEvalCommand(socket, form), capture_output=True, text=True,
                              check=False, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None


def programPath(name: str) -> str:
    """The absolute path of program name, as on PATH (for snippets that run outside this shell)."""
    found = shutil.which(name)
    return str(pathlib.Path(found).absolute()) if found else name


windowChoices = ('reuse', 'new')


def _codeSendReported(cmndOutcome: b.op.Outcome, args: typing.List[str]) -> b.op.Outcome:
    """Run code with args for a command: DISPLAY checked, the command noted on stderr, a failure reported."""
    if (problem := displayProblem()):
        b_io.eh.problem_usageError(problem)
        return b_io.eh.badOutcome(cmndOutcome)
    b_io.ann.note(f"DISPLAY={os.environ['DISPLAY']} {shlex.join(['code', *args])}")
    result = codeRun(args)
    if result.returncode != 0:
        b_io.eh.problem_usageError(f"code failed ({result.returncode}): {result.stderr.strip()}")
        return b_io.eh.badOutcome(cmndOutcome)
    return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /examples_csu/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Examples of the vscode layer's commands.
    #+end_org """
    od = collections.OrderedDict
    cmnd = cs.examples.cmndEnter
    literal = cs.examples.execInsert

    cs.examples.menuChapter('=Inspect= -- the local VS Code, read-only (no DISPLAY needed)')
    cmnd('vscodeVersion', comment="# Version, commit, architecture")
    cmnd('vscodeTopology', comment="# Can this shell reach a desktop VS Code? Ends with a verdict")
    cmnd('vscodeWorkspaces', comment="# Folders VS Code has state for, newest first")

    cs.examples.menuChapter('=Extensions= -- installed extensions (installing and pinning: vscode-sbom.pcs)')
    cmnd('vscodeExtensions', comment="# id and version, one per line")
    cmnd('vscodeExtensionVersion', args='anthropic.claude-code', comment="# The version of one extension")
    literal("vscode-sbom.pcs -i extsReport  # The pinned versions against the installed ones")

    cs.examples.menuChapter('=Windows= -- bring a VS Code window to the front (DISPLAY required)')
    cmnd('vscodeFocus', comment="# The first visible VS Code window")
    cmnd('vscodeFocus', args='.', comment="# The window of this directory (by its name in the title)")

    cs.examples.menuChapter('=Open= -- files and folders in the local VS Code (DISPLAY required)')
    cmnd('vscodeOpenFile', args='README.org', comment="# In the last active window")
    cmnd('vscodeOpenFile', args='README.org 10', comment="# At line 10")
    cmnd('vscodeOpenFile', args='README.org 10 5', comment="# At line 10, column 5")
    cmnd('vscodeOpenFolder', args='.', comment="# This directory, in the last active window")
    cmnd('vscodeOpenFolder', pars=od([('window', 'new')]), args='.', comment="# This directory, in a new window")
    cmnd('vscodeAddFolder', args='..', comment="# Add the parent to the last active window's workspace")
    cmnd('vscodeDiff', args='/etc/hosts /etc/hostname', comment="# The diff view of two files")

    cs.examples.menuChapter('=Blee= -- the partner Emacs (optional; b:vscode/init of blee/vscode-claude)')
    cmnd('vscodePartner', comment="# The live partner Emacs (socket, pid), or why there is none")
    cmnd('bleeOpenFile', args='README.org 10 5', comment="# This file in the partner Emacs, at line 10, column 5")
    cmnd('vscodeBleeLinkSnippet', comment="# The VS Code task and key that run bleeOpenFile on the current file")

    cs.examples.menuChapter('=vscodeOpenUri= -- hand a URI to the local VS Code (DISPLAY required)')
    cmnd('vscodeOpenUri', args='"vscode://file/etc/hosts:1"', comment="# VS Code's own vscode://file handler: a file at a line")
    cmnd('vscodeOpenUri', args='"vscode://file/etc/hosts:1:3"', comment="# At line 1, column 3")


def commonParamsSpecify(csParams: cs.param.CmndParamDict) -> None:

    csParams.parDictAdd(
        parName='window',
        parDescription="vscodeOpenFolder: reuse the last active window (default) or open a new one.",
        parDataType=None,
        parDefault='reuse',
        parChoices=list(windowChoices),
        argparseShortOpt=None,
        argparseLongOpt='--window',
    )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeOpenUri" :comment "Hand a URI to the local VS Code" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeOpenUri>>  *Hand a URI to the local VS Code*  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeOpenUri(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Hand a URI to the local VS Code"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Hand the URI to the local (desktop) VS Code with =code --open-url=:
VS Code's own handlers (=vscode://file/<path>:<line>=) or an extension's (=vscode://<publisher>.<name>/...=).
The primitive under =claudePrompt= (WorkPlan 10.6 of blee/vscode-claude). =DISPLAY= must be the desktop
VS Code's; =code= exits 0 even when nothing reached the window.
        #+end_org """)

        uri = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        if not uri:
            b_io.eh.problem_usageError("No URI: give it as the argument")
            return failed(cmndOutcome)
        if (problem := displayProblem()):
            b_io.eh.problem_usageError(problem)
            return failed(cmndOutcome)
        b_io.ann.note(f"DISPLAY={os.environ['DISPLAY']} {shlex.join(openUriCommand(uri))}")
        result = openUriSend(uri)
        if result.returncode != 0:
            b_io.eh.problem_usageError(f"code --open-url failed ({result.returncode}): {result.stderr.strip()}")
            return failed(cmndOutcome)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="uri",
            argDefault=None,
            argChoices=[],
            argDescription="The URI, e.g. vscode://file/<path>:<line>",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeVersion" :comment "The local VS Code version" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeVersion>>  *The local VS Code version*  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeVersion(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
        """The local VS Code version"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print =code --version=: the version, its commit and the architecture, one per line. Needs no =DISPLAY=.
        #+end_org """)
        result = codeRun(['--version'])
        if result.returncode != 0:
            b_io.eh.problem_usageError(f"code --version failed ({result.returncode}): {result.stderr.strip()}")
            return failed(cmndOutcome)
        print(result.stdout, end='')
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeTopology" :comment "Can this shell reach a desktop VS Code" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeTopology>>  *Can this shell reach a desktop VS Code*  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeTopology(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
        """Can this shell reach a desktop VS Code"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Whether this shell can hand things to a desktop VS Code (topology A of
blee/vscode-claude's design), one =key: value= line each: =launcher= (which =code= is on PATH: =desktop=,
=remote-cli=, =other=, =none=), =ipcHook= (=VSCODE_IPC_HOOK_CLI=, dropped by these commands), =display=
(this shell's), =desktopMain= (pid and =DISPLAY= of each running desktop VS Code), then =verdict=:
=ready=, or what is missing. Read-only.
        #+end_org """)
        kind, path = launcherKind()
        mains, displays = desktopProcesses()
        display = os.environ.get('DISPLAY', '')
        print(f"launcher: {kind} {path or ''}".rstrip())
        print(f"ipcHook: {'set (dropped)' if os.environ.get('VSCODE_IPC_HOOK_CLI') else 'unset'}")
        print(f"display: {display or '(unset)'}")
        print(f"desktopMain: {' '.join(map(str, mains)) or '(none)'}")
        print(f"desktopDisplay: {' '.join(displays) or '(unknown)'}")
        if kind != 'desktop':
            verdict = f"no desktop launcher (code is {kind})"
        elif not mains:
            verdict = "no desktop VS Code running"
        elif not display:
            verdict = f"DISPLAY unset (the desktop VS Code's: {' '.join(displays) or 'unknown'})"
        elif displays and displayHost(display) not in map(displayHost, displays):
            verdict = f"DISPLAY={display} is not the desktop VS Code's ({' '.join(displays)})"
        else:
            verdict = "ready"
        print(f"verdict: {verdict}")
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeWorkspaces" :comment "The folders VS Code has state for, newest first" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeWorkspaces>>  *The folders VS Code has state for, newest first*  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeWorkspaces(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
        """The folders VS Code has state for, newest first"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  One line per folder or workspace VS Code keeps state for (=workspaceStorage/=),
most recently used first, tab-separated: the date it was last used, then the path. A history, not
the windows open now; undocumented. Read-only.
        #+end_org """)
        for mtime, target in workspacesKnown():
            print(f"{datetime.datetime.fromtimestamp(mtime):%Y-%m-%d %H:%M}\t{target}")
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeExtensions" :comment "The installed extensions and their versions" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeExtensions>>  *The installed extensions and their versions*  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeExtensions(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
        """The installed extensions and their versions"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  One line per installed extension, tab-separated: its id and version
(=code --list-extensions --show-versions=). Installing and pinning them is =vscode-sbom.pcs='s job.
        #+end_org """)
        if (extensions := extensionsInstalled()) is None:
            b_io.eh.problem_usageError("code --list-extensions failed")
            return failed(cmndOutcome)
        for extId, version in extensions:
            print(f"{extId}\t{version}")
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeExtensionVersion" :comment "The version of one installed extension" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeExtensionVersion>>  *The version of one installed extension*  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeExtensionVersion(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """The version of one installed extension"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print only the version of the extension with this id (case does not matter);
a usage error when it is not installed.
        #+end_org """)
        wanted = (self.cmndArgsGet("0", cmndArgsSpecDict, argsList) or '').lower()
        if not wanted:
            b_io.eh.problem_usageError("No extension id: give it as the argument")
            return failed(cmndOutcome)
        if (extensions := extensionsInstalled()) is None:
            b_io.eh.problem_usageError("code --list-extensions failed")
            return failed(cmndOutcome)
        for extId, version in extensions:
            if extId.lower() == wanted:
                print(version)
                return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)
        b_io.eh.problem_usageError(f"{wanted} is not installed")
        return failed(cmndOutcome)

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="extId",
            argDefault=None,
            argChoices=[],
            argDescription="An extension id, e.g. anthropic.claude-code",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeFocus" :comment "Bring a VS Code window to the front" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeFocus>>  *Bring a VS Code window to the front*  =verify= argsMin=0 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeFocus(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Bring a VS Code window to the front"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Activate the visible desktop VS Code window whose title has the folder's name
(the last part of the path; =.= is this directory), or with none the first one found (=xdotool=).
        #+end_org """)
        folder = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        name = pathlib.Path(folder).resolve().name if folder else None
        if (problem := displayProblem()):
            b_io.eh.problem_usageError(problem)
            return failed(cmndOutcome)
        if not shutil.which(focusCommand()[0]):
            b_io.eh.problem_usageError("xdotool is not installed (rawBisos-sbom.pcs)")
            return failed(cmndOutcome)
        b_io.ann.note(f"DISPLAY={os.environ['DISPLAY']} {shlex.join(focusCommand(name))}")
        result = focusSend(name)
        if result.returncode != 0:
            b_io.eh.problem_usageError(f"No visible VS Code window{f' titled with {name}' if name else ''} ({result.returncode})")
            return failed(cmndOutcome)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="folder",
            argDefault=None,
            argChoices=[],
            argDescription="Optional: a folder whose name is in the window's title",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeOpenFile" :comment "Open a file in VS Code, at a line and column" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 3 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeOpenFile>>  *Open a file in VS Code, at a line and column*  =verify= argsMin=1 argsMax=3 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeOpenFile(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 3,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Open a file in VS Code, at a line and column"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Open the file in the last active VS Code window (=--reuse-window=), at the
line and column when given (=--goto=). A relative path is taken from this directory.
        #+end_org """)
        file = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        line = self.cmndArgsGet("1", cmndArgsSpecDict, argsList)
        column = self.cmndArgsGet("2", cmndArgsSpecDict, argsList)
        if not file:
            b_io.eh.problem_usageError("No file: give it as the first argument")
            return failed(cmndOutcome)
        path = str(pathlib.Path(file).expanduser().absolute())
        if line:
            args = ['--reuse-window', '--goto', ':'.join([path, line] + ([column] if column else []))]
        else:
            args = ['--reuse-window', path]
        return _codeSendReported(cmndOutcome, args)

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="file",
            argDefault=None,
            argChoices=[],
            argDescription="The file",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="line",
            argDefault=None,
            argChoices=[],
            argDescription="Optional: the line",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="2",
            argName="column",
            argDefault=None,
            argChoices=[],
            argDescription="Optional: the column",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeOpenFolder" :comment "Open a folder in VS Code" :extent "verify" :ro "cli" :parsMand "" :parsOpt "window" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeOpenFolder>>  *Open a folder in VS Code*  =verify= parsOpt=window argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeOpenFolder(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'window', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             window: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Open a folder in VS Code"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'window': window, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        window = csParam.mappedValue('window', window)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Open the folder in VS Code: in the last active window (=--window=reuse=, the
default) or a new one (=--window=new=). The folder sets the working directory of the window's Claude
sessions, and so which =CLAUDE.md= and =.claude/= they load.
        #+end_org """)
        folder = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        window = window or 'reuse'
        if window not in windowChoices:
            b_io.eh.problem_usageError(f"--window must be one of {', '.join(windowChoices)}, not {window}")
            return failed(cmndOutcome)
        if not folder:
            b_io.eh.problem_usageError("No folder: give it as the argument")
            return failed(cmndOutcome)
        path = pathlib.Path(folder).expanduser().resolve()
        if not path.is_dir():
            b_io.eh.problem_usageError(f"Not a directory: {path}")
            return failed(cmndOutcome)
        return _codeSendReported(cmndOutcome, [f'--{window}-window', str(path)])

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="folder",
            argDefault=None,
            argChoices=[],
            argDescription="The folder",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeAddFolder" :comment "Add a folder to the last active VS Code window" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeAddFolder>>  *Add a folder to the last active VS Code window*  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeAddFolder(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Add a folder to the last active VS Code window"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Add the folder to the last active window's workspace (=code --add=), making
it a multi-root workspace without a new window.
        #+end_org """)
        folder = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        if not folder:
            b_io.eh.problem_usageError("No folder: give it as the argument")
            return failed(cmndOutcome)
        path = pathlib.Path(folder).expanduser().resolve()
        if not path.is_dir():
            b_io.eh.problem_usageError(f"Not a directory: {path}")
            return failed(cmndOutcome)
        return _codeSendReported(cmndOutcome, ['--add', str(path)])

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="folder",
            argDefault=None,
            argChoices=[],
            argDescription="The folder",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeDiff" :comment "Compare two files in VS Code" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 2 :argsMax 2 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeDiff>>  *Compare two files in VS Code*  =verify= argsMin=2 argsMax=2 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeDiff(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 2, 'Max': 2,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Compare two files in VS Code"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Open VS Code's diff view of the two files (=code --diff=), in the last active
window.
        #+end_org """)
        left = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        right = self.cmndArgsGet("1", cmndArgsSpecDict, argsList)
        if not (left and right):
            b_io.eh.problem_usageError("Give the two files as the arguments")
            return failed(cmndOutcome)
        paths = [pathlib.Path(each).expanduser().absolute() for each in (left, right)]
        if (missing := [str(each) for each in paths if not each.is_file()]):
            b_io.eh.problem_usageError(f"Not a file: {', '.join(missing)}")
            return failed(cmndOutcome)
        return _codeSendReported(cmndOutcome, ['--reuse-window', '--diff', *map(str, paths)])

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="left",
            argDefault=None,
            argChoices=[],
            argDescription="The first file",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="right",
            argDefault=None,
            argChoices=[],
            argDescription="The second file",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodePartner" :comment "The partner Emacs, or why there is none" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodePartner>>  *The partner Emacs, or why there is none*  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodePartner(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
        """The partner Emacs, or why there is none"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Read the partner file (=/bisos/var/blee/vscode/partner-<user>.json=,
written by =b:vscode/init=) and check that its Emacs is alive. Prints =live= and the entry's fields, one
=key value= line each, or =none= and why. Read-only; VS Code alone needs no partner.
        #+end_org """)
        entry, why = partnerRead()
        if entry is None:
            print(f"none\t{why}")
        else:
            print("live")
            for key in ('socket', 'pid', 'display', 'time', 'emacsVersion'):
                print(f"{key}\t{entry.get(key, '')}")
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "bleeOpenFile" :comment "Open a file in the partner Emacs, at a line" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 3 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<bleeOpenFile>>  *Open a file in the partner Emacs, at a line*  =verify= argsMin=1 argsMax=3 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class bleeOpenFile(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 3,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Open a file in the partner Emacs, at a line"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  VS Code to Emacs: visit the file in the partner Emacs (=vscodePartner=), at
the line and column when given (=emacsclient -n +LINE:COL=), and raise its frame. Run by the VS Code
task of =vscodeBleeLinkSnippet=. Refused when there is no live partner.
        #+end_org """)
        file = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        line = self.cmndArgsGet("1", cmndArgsSpecDict, argsList)
        column = self.cmndArgsGet("2", cmndArgsSpecDict, argsList)
        if not file:
            b_io.eh.problem_usageError("No file: give it as the first argument")
            return failed(cmndOutcome)
        entry, why = partnerRead()
        if entry is None:
            b_io.eh.problem_usageError(f"No partner Emacs: {why} (b:vscode/init in Blee)")
            return failed(cmndOutcome)
        path = str(pathlib.Path(file).expanduser().absolute())
        where = [f"+{line}" + (f":{column}" if column else "")] if line else []
        command = ['emacsclient', '-s', entry['socket'], '-n', *where, path]
        b_io.ann.note(shlex.join(command))
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=False, timeout=10)
        except subprocess.TimeoutExpired:
            b_io.eh.problem_usageError(f"emacsclient did not answer within 10s ({entry['socket']})")
            return failed(cmndOutcome)
        if result.returncode != 0:
            b_io.eh.problem_usageError(f"emacsclient failed ({result.returncode}): {result.stderr.strip()}")
            return failed(cmndOutcome)
        emacsEval(entry['socket'], "(let ((f (selected-frame))) (raise-frame f) (select-frame-set-input-focus f))")
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="file",
            argDefault=None,
            argChoices=[],
            argDescription="The file",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="line",
            argDefault=None,
            argChoices=[],
            argDescription="Optional: the line",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="2",
            argName="column",
            argDefault=None,
            argChoices=[],
            argDescription="Optional: the column",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeBleeLinkSnippet" :comment "The VS Code task and key that run bleeOpenFile" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeBleeLinkSnippet>>  *The VS Code task and key that run bleeOpenFile*  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeBleeLinkSnippet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
        """The VS Code task and key that run bleeOpenFile"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print, to paste by hand, the user task (=~/.config/Code/User/tasks.json=,
"Tasks: Open User Tasks") and the key (=keybindings.json=) that run =bleeOpenFile= on the file and line
of the VS Code editor. Also the setting that saves the file first. Nothing is written: VS Code's JSON
files take comments and are not merged automatically.
        #+end_org """)
        label = "Blee: open here"
        task = {
            "label": label,
            "type": "process",
            "command": programPath('vscode.cs'),
            "args": ["-i", "bleeOpenFile", "${file}", "${lineNumber}", "${columnNumber}"],
            "presentation": {"reveal": "silent", "showReuseMessage": False},
            "problemMatcher": [],
        }
        key = {"key": "ctrl+alt+e", "command": "workbench.action.tasks.runTask", "args": label}
        print(f"// {userDataDir / 'User' / 'tasks.json'}: add to \"tasks\"")
        print(json.dumps(task, indent=2))
        print(f"// {userDataDir / 'User' / 'keybindings.json'}: add to the list")
        print(json.dumps(key, indent=2))
        print(f"// {userDataDir / 'User' / 'settings.json'}: so that Emacs gets what is on screen")
        print(json.dumps({"task.saveBeforeRun": "always"}, indent=2))
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)
