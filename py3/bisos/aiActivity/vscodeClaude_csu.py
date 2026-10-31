# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= for the Claude sessions of the local VS Code: the Claude layer of
=vscodeClaude.cs=, on top of =vscode_csu=.
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
** This File: /bxRepos/bisos-pip/aiActivity/py3/bisos/aiActivity/vscodeClaude_csu.py
** File True Name: /bisos/git/auth/bxRepos/bisos-pip/aiActivity/py3/bisos/aiActivity/vscodeClaude_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inDev"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['vscodeClaude_csu'], }
csInfo['version'] = '202610290000'
csInfo['status']  = 'inDev'
csInfo['panel'] = 'vscodeClaude_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]]
The Claude layer (WorkPlan Stage 22; before, =claudeSessions.cs= and =claudeSessions.py=, 20.3): which
Claude sessions are running, and a prompt into one of them. =claudeSessionsList= prints one
tab-separated line per live session, =claudeSessionsLatest= only the =sessionId= of the most recently
active one, so their output can be used as is. =--mode= picks the instance (=local= desktop VS Code,
=remote= VS Code server, =all=), =--cwd= a project directory.

Claude Code writes one =<pid>.json= per running Claude process into =~/.claude/sessions/= and removes
it when the process ends cleanly. In the VS Code extension each open conversation is a process: a new
conversation or tab is a new file, =/clear= rewrites =sessionId= in place, a resume from history is a
new process. The registry is undocumented (seen in Claude Code 2.1.311), so it is read here only.

A file counts only if its process is alive: =/proc/<pid>= exists and field 22 of its =stat= (start
time) equals the file's =procStart=, which rejects a file left by a crash whose pid was reused. The
instance is told by the process's executable: under =~/.vscode/extensions/= is the local (desktop) VS
Code, under =~/.vscode-server/extensions/= the remote VS Code server, anything else (e.g. =claude= in
a terminal) is =other=.

A prompt goes in through the extension's =/open= URI, handed to VS Code by =vscode_csu=.
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

import dataclasses
import json
import os
import pathlib
import shlex
import shutil
import sys
import urllib.parse

from bisos.aiActivity import vscode_csu


registryDir = pathlib.Path.home() / '.claude' / 'sessions'
localExtensionsDir = pathlib.Path.home() / '.vscode' / 'extensions'
remoteExtensionsDir = pathlib.Path.home() / '.vscode-server' / 'extensions'

modes = ('local', 'remote', 'all')
submitChoices = ('no', 'yes')

# The events hookToEmacs hands to Blee, as hooksSnippet installs them (Claude Code hook event names).
hookEvents = ('Stop', 'Notification')


@dataclasses.dataclass
class Session:
    """One live Claude process, as its registry file and /proc describe it."""
    pid: int
    sessionId: str
    cwd: str
    name: str
    status: str
    startedAt: int          # ms since the epoch
    updatedAt: int          # ms since the epoch; startedAt when the file has none
    instance: str           # local, remote or other
    entrypoint: str

    def line(self) -> str:
        """The tab-separated form printed by claudeSessionsList."""
        return "\t".join((self.sessionId, self.instance, self.cwd, self.name, self.status,
                          str(self.updatedAt), str(self.pid)))


lineFields = ('sessionId', 'instance', 'cwd', 'name', 'status', 'updatedAt', 'pid')


def _procStart(pid: int) -> typing.Optional[str]:
    """Field 22 of /proc/<pid>/stat (start time), or None if there is no such process."""
    try:
        stat = pathlib.Path(f'/proc/{pid}/stat').read_text()
    except OSError:
        return None
    # The command name (field 2) is in parentheses and may contain spaces: split after the last ')'.
    return stat.rsplit(')', 1)[1].split()[19]


def _instance(pid: int) -> str:
    try:
        exe = pathlib.Path(f'/proc/{pid}/exe').readlink()
    except OSError:
        return 'other'
    if exe.is_relative_to(localExtensionsDir):
        return 'local'
    if exe.is_relative_to(remoteExtensionsDir):
        return 'remote'
    return 'other'


def sessionsRunning(registry: pathlib.Path = registryDir) -> typing.List[Session]:
    """The live sessions in the registry; unreadable files and dead processes are skipped."""
    sessions: typing.List[Session] = []
    if not registry.is_dir():
        return sessions
    for path in sorted(registry.glob('*.json')):
        try:
            entry = json.loads(path.read_text())
            pid = int(entry['pid'])
            sessionId = entry['sessionId']
        except (OSError, ValueError, KeyError, TypeError):
            continue
        if _procStart(pid) != str(entry.get('procStart')):
            continue
        startedAt = int(entry.get('startedAt') or 0)
        sessions.append(Session(
            pid=pid,
            sessionId=sessionId,
            cwd=entry.get('cwd', ''),
            name=entry.get('name', ''),
            status=entry.get('status', ''),
            startedAt=startedAt,
            updatedAt=int(entry.get('updatedAt') or startedAt),
            instance=_instance(pid),
            entrypoint=entry.get('entrypoint', ''),
        ))
    return sessions


def sessionsSelect(
        sessions: typing.List[Session],
        mode: str = 'local',
        cwd: typing.Optional[str] = None,
) -> typing.List[Session]:
    """Those of the instance named by mode (all: every one), and in cwd if given, newest first."""
    if mode not in modes:
        raise ValueError(f"mode must be one of {modes}, not {mode}")
    selected = [s for s in sessions if mode == 'all' or s.instance == mode]
    if cwd:
        # /bxRepos/... and /bisos/git/auth/bxRepos/... are the same place
        wanted = pathlib.Path(cwd).expanduser().resolve()
        selected = [s for s in selected if pathlib.Path(s.cwd).resolve() == wanted]
    return sorted(selected, key=lambda s: s.updatedAt, reverse=True)


# The URI handler of the Claude VS Code extension (WorkPlan 20.3.2). It opens the session (a new
# conversation without one) and puts the prompt in its input box, unsubmitted: the user presses Enter.
# But a session already open (every running one) is only brought to the front, and a prompt given
# for it is dropped with "Session is already open. Your prompt was not applied": for those the prompt
# goes on the clipboard instead (vscode_csu.clipboardSet). Both parameters are optional.
# Read from the extension's code (2.1.311), not a documented API: build it here only.
claudeOpenUriBase = 'vscode://anthropic.claude-code/open'


def claudeOpenUri(prompt: typing.Optional[str] = None, sessionId: typing.Optional[str] = None) -> str:
    """The /open URI for prompt (none: only open), into sessionId, or a new conversation when None."""
    query = {'session': sessionId} if sessionId else {}
    if prompt is not None:
        query['prompt'] = prompt
    return f"{claudeOpenUriBase}?{urllib.parse.urlencode(query, quote_via=urllib.parse.quote)}"


def _selected(
        mode: typing.Optional[str],
        cwd: typing.Optional[str],
) -> typing.Optional[typing.List[Session]]:
    """The selected sessions, or None after a usage error (parChoices does not restrict --mode)."""
    mode = mode or 'local'
    if mode not in modes:
        b_io.eh.problem_usageError(f"--mode must be one of {', '.join(modes)}, not {mode}")
        return None
    return sessionsSelect(sessionsRunning(), mode, cwd)


def _promptUri(
        session: typing.Optional[str],
        cwd: typing.Optional[str],
        argsList: typing.Optional[typing.List[str]],
) -> typing.Optional[typing.Tuple[str, typing.Optional[str]]]:
    """(the /open URI, the text for the clipboard or None), or None after a usage error.

    session: a sessionId, 'new' (a new conversation), or None (the latest local session, in cwd).
    A running session is already open, and the extension drops a prompt given for it: its URI only
    brings it to the front, and the prompt goes on the clipboard. Otherwise the prompt is in the URI.
    """
    prompt = ' '.join(argsList or [])
    if not prompt:
        b_io.eh.problem_usageError("No prompt: give its text as the arguments")
        return None
    if session == 'new':
        return claudeOpenUri(prompt), None
    live = sessionsSelect(sessionsRunning(), 'local', cwd)
    if not session:
        if not live:
            b_io.eh.problem_usageError(f"No running local session (cwd={cwd}): give --session=<id> or --session=new")
            return None
        session = live[0].sessionId
    elif session not in [s.sessionId for s in live]:
        b_io.ann.note(f"{session} is not a running local session; VS Code may open it from history")
        return claudeOpenUri(prompt, session), None
    return claudeOpenUri(None, session), prompt


def _promptArgsSpec() -> cs.CmndArgsSpecDict:
    cmndArgsSpecDict = cs.CmndArgsSpecDict()
    cmndArgsSpecDict.argsDictAdd(
        argPosition="0&-1",
        argName="prompt",
        argDefault=None,
        argChoices=[],
        argDescription="The prompt's text; several arguments are joined with spaces",
    )
    return cmndArgsSpecDict


####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /examples_csu/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Examples of the Claude layer's commands.
    #+end_org """
    od = collections.OrderedDict
    cmnd = cs.examples.cmndEnter
    literal = cs.examples.execInsert

    cs.examples.menuChapter('=claudeSessionsList= -- running sessions, one tab-separated line each, newest first')
    cmnd('claudeSessionsList', comment="# Local (desktop VS Code) sessions")
    cmnd('claudeSessionsList', pars=od([('mode', 'remote')]), comment="# The VS Code server's sessions")
    cmnd('claudeSessionsList', pars=od([('mode', 'all')]), comment="# All, including claude in a terminal")
    cmnd('claudeSessionsList', pars=od([('cwd', '.')]), comment="# Local sessions working in this directory")
    literal(f"# Fields: {' '.join(lineFields)}")

    cs.examples.menuChapter('=claudeSessionsLatest= -- the sessionId of the most recently active session')
    cmnd('claudeSessionsLatest', comment="# The default target of claudePrompt")
    cmnd('claudeSessionsLatest', pars=od([('cwd', '.')]), comment="# The latest working in this directory")

    cs.examples.menuChapter('=claudePrompt= -- a prompt into a local session\'s input box (you press Enter)')
    cmnd('claudePromptUri', args='"Hello from vscodeClaude.cs"', comment="# Print the /open URI only, send nothing")
    cmnd('claudePrompt', args='"Hello from vscodeClaude.cs"', comment="# Into the latest local session")
    cmnd('claudePrompt', pars=od([('cwd', '.')]), args='"/bx-status-read"',
         comment="# Into the latest local session working in this directory")
    cmnd('claudePrompt', pars=od([('session', 'new')]), args='"Hello from vscodeClaude.cs"',
         comment="# Into a new conversation")
    cmnd('claudePrompt', pars=od([('session', '<sessionId>')]), args='"Hello from vscodeClaude.cs"',
         comment="# Into a given session (see claudeSessionsList)")
    cmnd('claudePrompt', pars=od([('session', 'new'), ('submit', 'yes')]), args='"Hello from vscodeClaude.cs"',
         comment="# And press Enter: submitted (try it on a new conversation first)")

    cs.examples.menuChapter('=Hooks= -- Claude Code hooks to the partner Emacs (optional; no partner: no effect)')
    cmnd('hooksSnippet', comment="# The ~/.claude/settings.json \"hooks\" entry to add by hand")
    literal('echo \'{"hook_event_name":"Stop","session_id":"x","cwd":"/tmp"}\' | vscodeClaude.cs -i hookToEmacs Stop  # As a hook runs it')


def commonParamsSpecify(
        csParams: cs.param.CmndParamDict,
) -> None:

    csParams.parDictAdd(
        parName='mode',
        parDescription=("Which instance's sessions: local (desktop VS Code), remote (VS Code server) "
                        "or all (also claude in a terminal). Default: local."),
        parDataType=None,
        parDefault='local',
        parChoices=list(modes),
        argparseShortOpt=None,
        argparseLongOpt='--mode',
    )
    csParams.parDictAdd(
        parName='cwd',
        parDescription="Optional: only sessions whose working directory is this one (symlinks resolved).",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--cwd',
    )
    csParams.parDictAdd(
        parName='session',
        parDescription=("The sessionId to prompt, or 'new' for a new conversation. Default: the latest "
                        "local session (in --cwd if given)."),
        parDataType=None,
        parDefault=None,
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--session',
    )
    csParams.parDictAdd(
        parName='submit',
        parDescription=("claudePrompt: yes also presses Enter (xdotool) after the prompt is in the input "
                        "box, submitting it. Default: no, the user presses Enter."),
        parDataType=None,
        parDefault='no',
        parChoices=list(submitChoices),
        argparseShortOpt=None,
        argparseLongOpt='--submit',
    )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "claudeSessionsList" :comment "Running sessions, one tab-separated line each" :extent "verify" :ro "cli" :parsMand "" :parsOpt "mode cwd" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<claudeSessionsList>>  *Running sessions, one tab-separated line each*  =verify= parsOpt=mode cwd ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class claudeSessionsList(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'mode', 'cwd', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             mode: typing.Optional[str]=None,  # Cs Optional Param
             cwd: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:
        """Running sessions, one tab-separated line each"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'mode': mode, 'cwd': cwd, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        mode = csParam.mappedValue('mode', mode)
        cwd = csParam.mappedValue('cwd', cwd)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  One line per live Claude session of the instance =--mode= names,
most recently active first, fields separated by tabs: sessionId, instance, cwd, name, status,
updatedAt (ms since the epoch), pid. Nothing else goes to stdout. A conversation the VS Code side-bar
panel switched away from is still running, so it is listed too.
        #+end_org """)

        if (sessions := _selected(mode, cwd)) is None:
            return failed(cmndOutcome)
        for session in sessions:
            print(session.line())
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "claudeSessionsLatest" :comment "The sessionId of the most recently active session" :extent "verify" :ro "cli" :parsMand "" :parsOpt "mode cwd" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<claudeSessionsLatest>>  *The sessionId of the most recently active session*  =verify= parsOpt=mode cwd ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class claudeSessionsLatest(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'mode', 'cwd', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             mode: typing.Optional[str]=None,  # Cs Optional Param
             cwd: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:
        """The sessionId of the most recently active session"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'mode': mode, 'cwd': cwd, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        mode = csParam.mappedValue('mode', mode)
        cwd = csParam.mappedValue('cwd', cwd)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print only the sessionId of the live session with the most recent
=updatedAt= (last activity), of the instance =--mode= names and in =--cwd= if given. With none, stdout
stays empty and a note says so. Usually, not always, the conversation on screen.
        #+end_org """)

        if (sessions := _selected(mode, cwd)) is None:
            return failed(cmndOutcome)
        if not sessions:
            b_io.eh.problem_usageError(f"No running session: mode={mode or 'local'} cwd={cwd}")
            return failed(cmndOutcome)
        print(sessions[0].sessionId)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "claudePromptUri" :comment "Print the /open URI of a prompt, send nothing" :extent "verify" :ro "cli" :parsMand "" :parsOpt "session cwd" :argsMin 1 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<claudePromptUri>>  *Print the /open URI of a prompt, send nothing*  =verify= parsOpt=session cwd argsMin=1 argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class claudePromptUri(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'session', 'cwd', ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             session: typing.Optional[str]=None,  # Cs Optional Param
             cwd: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Print the /open URI of a prompt, send nothing"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'session': session, 'cwd': cwd, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        session = csParam.mappedValue('session', session)
        cwd = csParam.mappedValue('cwd', cwd)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print the =vscode://anthropic.claude-code/open= URI that =claudePrompt=
would send, and nothing else on stdout. The session is chosen as for =claudePrompt=. For a running
session the URI carries no prompt (=claudePrompt= puts it on the clipboard instead); a note on stderr
says so.
        #+end_org """)

        if (chosen := _promptUri(session, cwd, self.cmndArgsGet("0&-1", cmndArgsSpecDict, argsList))) is None:
            return failed(cmndOutcome)
        uri, clipText = chosen
        if clipText is not None:
            b_io.ann.note("A running session: claudePrompt would put the text on the clipboard")
        print(uri)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        return _promptArgsSpec()


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "claudePrompt" :comment "Put a prompt in a local session's input box" :extent "verify" :ro "cli" :parsMand "" :parsOpt "session cwd submit" :argsMin 1 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<claudePrompt>>  *Put a prompt in a local session's input box*  =verify= parsOpt=session cwd submit argsMin=1 argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class claudePrompt(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'session', 'cwd', 'submit', ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             session: typing.Optional[str]=None,  # Cs Optional Param
             cwd: typing.Optional[str]=None,  # Cs Optional Param
             submit: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Put a prompt in a local session's input box"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'session': session, 'cwd': cwd, 'submit': submit, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        session = csParam.mappedValue('session', session)
        cwd = csParam.mappedValue('cwd', cwd)
        submit = csParam.mappedValue('submit', submit)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Open a session of the local (desktop) VS Code with the prompt in its
input box, not submitted: the user reads it and presses Enter. =--session=<id>=, =--session=new= for a
new conversation, or by default the latest local session (in =--cwd= if given). Runs
=code --open-url= with the extension's =/open= URI (=vscode_csu=).

A running session is already open, and the extension only brings it to the front (a prompt given for
it is dropped): its prompt goes on the X clipboard (=xclip=), and once the session is in front it is
pasted with a Ctrl+V from =xdotool= (both from =rawBisos-sbom.pcs=). Without =xdotool= the user presses
Ctrl+V. Either way the user presses Enter --- unless =--submit=yes=: then =xdotool= presses Enter in the
VS Code window once the prompt is in (refused without =xdotool=). The Enter goes to what has the focus
there, as the paste does.
        #+end_org """)

        submit = submit or 'no'
        if submit not in submitChoices:
            b_io.eh.problem_usageError(f"--submit must be one of {', '.join(submitChoices)}, not {submit}")
            return failed(cmndOutcome)
        if submit == 'yes' and not shutil.which(vscode_csu.returnCommand()[0]):
            b_io.eh.problem_usageError("--submit=yes needs xdotool (rawBisos-sbom.pcs)")
            return failed(cmndOutcome)
        if (chosen := _promptUri(session, cwd, self.cmndArgsGet("0&-1", cmndArgsSpecDict, argsList))) is None:
            return failed(cmndOutcome)
        uri, clipText = chosen
        if (problem := vscode_csu.displayProblem()):
            b_io.eh.problem_usageError(problem)
            return failed(cmndOutcome)
        if clipText is not None:
            if not shutil.which(vscode_csu.clipboardCommand()[0]):
                b_io.eh.problem_usageError("xclip is not installed (rawBisos-sbom.pcs): a running session's prompt goes on the clipboard")
                return failed(cmndOutcome)
            b_io.ann.note(f"DISPLAY={os.environ['DISPLAY']} {shlex.join(vscode_csu.clipboardCommand())} <<< {shlex.quote(clipText)}")
            result = vscode_csu.clipboardSet(clipText)
            if result.returncode != 0:
                b_io.eh.problem_usageError(f"xclip failed ({result.returncode})")
                return failed(cmndOutcome)
        b_io.ann.note(f"DISPLAY={os.environ['DISPLAY']} {shlex.join(vscode_csu.openUriCommand(uri))}")
        result = vscode_csu.openUriSend(uri)
        if result.returncode != 0:
            b_io.eh.problem_usageError(f"code --open-url failed ({result.returncode}): {result.stderr.strip()}")
            return failed(cmndOutcome)
        if clipText is not None:
            if not shutil.which(vscode_csu.pasteCommand()[0]):
                b_io.ann.note("xdotool is not installed (rawBisos-sbom.pcs): the prompt is on the clipboard: Ctrl+V, then Enter")
                return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)
            b_io.ann.note(f"DISPLAY={os.environ['DISPLAY']} {shlex.join(vscode_csu.pasteCommand())}")
            result = vscode_csu.pasteSend()
            if result.returncode != 0:
                b_io.eh.problem_usageError(f"xdotool failed ({result.returncode}): {result.stderr.strip()}; the prompt is on the clipboard: Ctrl+V")
                return failed(cmndOutcome)
        if submit == 'yes':
            # A new conversation (the prompt in the URI) opens a tab first: wait longer.
            delay = 0.3 if clipText is not None else 1.5
            b_io.ann.note(f"DISPLAY={os.environ['DISPLAY']} {shlex.join(vscode_csu.returnCommand(delay))}")
            result = vscode_csu.returnSend(delay)
            if result.returncode != 0:
                b_io.eh.problem_usageError(f"xdotool failed ({result.returncode}): {result.stderr.strip()}; the prompt is in, not submitted")
                return failed(cmndOutcome)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        return _promptArgsSpec()


def hookEventForward(event: str, payload: str) -> str:
    """Hand a Claude Code hook event to the partner Emacs; what happened, in one word.

    none: no live partner (nothing done); sent; notDefined: that Emacs lacks b:vscode:claude/hookHandle;
    timeout; failed. Never raises: a hook must not disturb the session.
    """
    entry, _why = vscode_csu.partnerRead()
    if entry is None:
        return 'none'
    form = ("(if (fboundp 'b:vscode:claude/hookHandle)"
            f" (b:vscode:claude/hookHandle {vscode_csu.elispString(event)} {vscode_csu.elispString(payload)})"
            " 'notDefined)")
    result = vscode_csu.emacsEval(entry['socket'], form, timeout=5)
    if result is None:
        return 'timeout'
    if result.returncode != 0:
        return 'failed'
    return 'notDefined' if result.stdout.strip() == 'notDefined' else 'sent'


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "hookToEmacs" :comment "A Claude Code hook: hand the event to the partner Emacs" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<hookToEmacs>>  *A Claude Code hook: hand the event to the partner Emacs*  =verify= argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class hookToEmacs(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """A Claude Code hook: hand the event to the partner Emacs"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Run by Claude Code as a hook (=hooksSnippet=): the event's JSON is on
stdin. With no live partner Emacs (=vscode.cs -i vscodePartner=) it does nothing, at once and silently:
a pure VS Code session is not affected. Otherwise it calls =b:vscode:claude/hookHandle= in that Emacs
(=emacsclient=, 5s timeout). Nothing goes to stdout (Claude Code would read it as a hook decision), and
it always succeeds: a hook never fails the session. The argument names the event; without it, the
JSON's =hook_event_name=.
        #+end_org """)
        payload = '' if sys.stdin is None or sys.stdin.isatty() else sys.stdin.read()
        event = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        if not event:
            try:
                event = json.loads(payload).get('hook_event_name', '')
            except (ValueError, AttributeError):
                event = ''
        outcome = hookEventForward(event or 'unknown', payload)
        if outcome not in ('none', 'sent'):
            b_io.ann.note(f"hookToEmacs {event}: {outcome}")
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="event",
            argDefault=None,
            argChoices=[],
            argDescription="Optional: the hook event (Stop, Notification, ...)",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "hooksSnippet" :comment "The settings.json hooks entry for hookToEmacs" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<hooksSnippet>>  *The settings.json hooks entry for hookToEmacs*  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class hooksSnippet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
        """The settings.json hooks entry for hookToEmacs"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print the ="hooks"= entry that runs =hookToEmacs= on Claude Code's Stop and
Notification events, to add by hand to the user's =~/.claude/settings.json= (not to a project's, nor to
the shared templates). Merge it with any ="hooks"= already there. Nothing is written.
        #+end_org """)
        program = vscode_csu.programPath('vscodeClaude.cs')
        hooks = {event: [{"hooks": [{"type": "command",
                                     "command": f"{program} -i hookToEmacs {event}",
                                     "timeout": 10}]}]
                 for event in hookEvents}
        print(f"// {pathlib.Path.home() / '.claude' / 'settings.json'}: merge into the top-level object")
        print(json.dumps({"hooks": hooks}, indent=2))
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)
