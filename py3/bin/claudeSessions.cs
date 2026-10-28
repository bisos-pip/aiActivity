#!/bin/env python
# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CSXU= that lists the running Claude Code sessions of this host.
#+end_org """

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/bxRepos/bisos-pip/aiActivity/README.org][aiActivity README]]

The CLI layer under Blee's Emacs-to-Claude integration (Stage 20 of the bisos.aiActivity WorkPlan):
Emacs asks it which Claude sessions are running, then sends a prompt into one of them. =list= prints
one tab-separated line per live session, =latest= only the =sessionId= of the most recently active
one, so its output can be used as is. =--mode= picks the instance (=local= desktop VS Code, =remote=
VS Code server, =all=), =--cwd= a project directory. Reads Claude Code's own registry,
=~/.claude/sessions/=, which is undocumented; writes nothing.
** Status: inDev
#+end_org """


####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-mu"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-mu
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-mu") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-mu
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
** This File: /bxRepos/bisos-pip/aiActivity/py3/bin/claudeSessions.cs
** File True Name: /bisos/git/auth/bxRepos/bisos-pip/aiActivity/py3/bin/claudeSessions.cs
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inDev"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
if 'csInfo' not in globals(): import typing ; csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['loadAs'], }
csInfo['version'] = '202610284226'
csInfo['status']  = 'inDev'
csInfo['panel'] = 'claudeSessions-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:


####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
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
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] *Imports* =Based on Classification=cs-mu=
#+end_org """
from bisos import b  # noqa: E402
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

import os
import shlex
import shutil
import typing

from bisos.aiActivity import claudeSessions as sessionsLib

""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~csuList emacs-list Specifications~  [[elisp:(blee:org:code-block/above-run)][ /Eval Below/ ]] [[elisp:(org-cycle)][| ]]
#+BEGIN_SRC emacs-lisp
(setq  b:py:cs:csuList
  (list
 ))
#+END_SRC
#+RESULTS:
#+end_org """

####+BEGIN: b:py3:cs:framework/csuListProc :pyImports t :csuImports t :csuParams t :csxuParams nil
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~Process CSU List~ with /0/ in csuList pyImports=t csuImports=t csuParams=t
#+end_org """


csuList = [ ]

g_importedCmndsModules = cs.csuList_importedModules(csuList)

def g_extraParams():
    csParams = cs.param.CmndParamDict()
    cs.csuList_commonParamsSpecify(csuList, csParams)
    cs.argsparseBasedOnCsParams(csParams)

####+END:


####+BEGIN: b:py3:cs:orgItem/section :title "Common Parameters Specification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification*   [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

def commonParamsSpecify(
        csParams: cs.param.CmndParamDict,
) -> None:

    csParams.parDictAdd(
        parName='mode',
        parDescription=("Which instance's sessions: local (desktop VS Code), remote (VS Code server) "
                        "or all (also claude in a terminal). Default: local."),
        parDataType=None,
        parDefault='local',
        parChoices=[*sessionsLib.modes],  # not list(): the list Cmnd below shadows the builtin
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


def _selected(
        mode: typing.Optional[str],
        cwd: typing.Optional[str],
) -> typing.Optional[typing.List[sessionsLib.Session]]:
    """The selected sessions, or None after a usage error (parChoices does not restrict --mode)."""
    mode = mode or 'local'
    if mode not in sessionsLib.modes:
        b_io.eh.problem_usageError(f"--mode must be one of {', '.join(sessionsLib.modes)}, not {mode}")
        return None
    return sessionsLib.sessionsSelect(sessionsLib.sessionsRunning(), mode, cwd)


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
        return sessionsLib.openUri(prompt), None
    live = sessionsLib.sessionsSelect(sessionsLib.sessionsRunning(), 'local', cwd)
    if not session:
        if not live:
            b_io.eh.problem_usageError(f"No running local session (cwd={cwd}): give --session=<id> or --session=new")
            return None
        session = live[0].sessionId
    elif session not in [s.sessionId for s in live]:
        b_io.ann.note(f"{session} is not a running local session; VS Code may open it from history")
        return sessionsLib.openUri(prompt, session), None
    return sessionsLib.openUri(None, session), prompt


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


####+BEGIN: b:py3:cs:main/outcomeReportControl :disabled? nil :cmnd t :ro nil
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~Invokation's Outcome Reporting Control~ with /cmnd=t/ /ro=nil/ 
#+end_org """
# cs.invOutcomeReportControl(cmnd=True, ro=True)
####+END:


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "CmndSvcs" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _CmndSvcs_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples" :extent "verify" :ro "noCli" :comment "FrameWrk: CS-Main-Examples" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples>>  *FrameWrk: CS-Main-Examples*  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
        """FrameWrk: CS-Main-Examples"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Conventional top level example.
        #+end_org """)

        od = collections.OrderedDict
        cmnd = cs.examples.cmndEnter
        literal = cs.examples.execInsert

        cs.examples.myName(cs.G.icmMyName(), cs.G.icmMyFullName())
        cs.examples.commonBrief()

        cs.examples.menuChapter('=list= -- running sessions, one tab-separated line each, newest first')
        cmnd('list', comment="# Local (desktop VS Code) sessions")
        cmnd('list', pars=od([('mode', 'remote')]), comment="# The VS Code server's sessions")
        cmnd('list', pars=od([('mode', 'all')]), comment="# All, including claude in a terminal")
        cmnd('list', pars=od([('cwd', '.')]), comment="# Local sessions working in this directory")
        literal(f"# Fields: {' '.join(sessionsLib.lineFields)}")

        cs.examples.menuChapter('=latest= -- the sessionId of the most recently active session')
        cmnd('latest', comment="# The default target for a prompt from Emacs")
        cmnd('latest', pars=od([('cwd', '.')]), comment="# The latest working in this directory")

        cs.examples.menuChapter('=prompt= -- a prompt into a local session\'s input box (you press Enter)')
        cmnd('promptUri', args='"Hello from Emacs"', comment="# Print the /open URI only, send nothing")
        cmnd('prompt', args='"Hello from Emacs"', comment="# Into the latest local session")
        cmnd('prompt', pars=od([('cwd', '.')]), args='"/bx-status-read"',
             comment="# Into the latest local session working in this directory")
        cmnd('prompt', pars=od([('session', 'new')]), args='"Hello from Emacs"',
             comment="# Into a new conversation")
        cmnd('prompt', pars=od([('session', '<sessionId>')]), args='"Hello from Emacs"',
             comment="# Into a given session (see list)")

        return(cmndOutcome)


# The commands with arguments come before list: their generated heads annotate argsList with
# list[str], which would name the list Cmnd once it is defined.

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "promptUri" :comment "Print the /open URI of a prompt, send nothing" :extent "verify" :ro "cli" :parsMand "" :parsOpt "session cwd" :argsMin 1 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<promptUri>>  *Print the /open URI of a prompt, send nothing*  =verify= parsOpt=session cwd argsMin=1 argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class promptUri(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print the =vscode://anthropic.claude-code/open= URI that =prompt= would
send, and nothing else on stdout. The session is chosen as for =prompt=. For a running session the URI
carries no prompt (=prompt= puts it on the clipboard instead); a note on stderr says so.
        #+end_org """)

        if (chosen := _promptUri(session, cwd, self.cmndArgsGet("0&-1", cmndArgsSpecDict, argsList))) is None:
            return failed(cmndOutcome)
        uri, clipText = chosen
        if clipText is not None:
            b_io.ann.note("A running session: prompt would put the text on the clipboard")
        print(uri)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        return _promptArgsSpec()


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "prompt" :comment "Put a prompt in a local session's input box" :extent "verify" :ro "cli" :parsMand "" :parsOpt "session cwd" :argsMin 1 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<prompt>>  *Put a prompt in a local session's input box*  =verify= parsOpt=session cwd argsMin=1 argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class prompt(cs.Cmnd):
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
        """Put a prompt in a local session's input box"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'session': session, 'cwd': cwd, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        session = csParam.mappedValue('session', session)
        cwd = csParam.mappedValue('cwd', cwd)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Open a session of the local (desktop) VS Code with the prompt in its
input box, not submitted: the user reads it and presses Enter. =--session=<id>=, =--session=new= for a
new conversation, or by default the latest local session (in =--cwd= if given). Runs
=code --open-url= with the extension's =/open= URI.

A running session is already open, and the extension only brings it to the front (a prompt given for
it is dropped): its prompt goes on the X clipboard (=xclip=), and once the session is in front it is
pasted with a Ctrl+V from =xdotool= (both from =rawBisos-sbom.pcs=). Without =xdotool= the user presses
Ctrl+V. Either way the user presses Enter.
        #+end_org """)

        if (chosen := _promptUri(session, cwd, self.cmndArgsGet("0&-1", cmndArgsSpecDict, argsList))) is None:
            return failed(cmndOutcome)
        uri, clipText = chosen
        if not os.environ.get('DISPLAY'):
            b_io.eh.problem_usageError("DISPLAY is not set: give the desktop VS Code's display (e.g. DISPLAY=:1)")
            return failed(cmndOutcome)
        if clipText is not None:
            if not shutil.which(sessionsLib.clipboardCommand()[0]):
                b_io.eh.problem_usageError("xclip is not installed (rawBisos-sbom.pcs): a running session's prompt goes on the clipboard")
                return failed(cmndOutcome)
            b_io.ann.note(f"DISPLAY={os.environ['DISPLAY']} {shlex.join(sessionsLib.clipboardCommand())} <<< {shlex.quote(clipText)}")
            result = sessionsLib.clipboardSet(clipText)
            if result.returncode != 0:
                b_io.eh.problem_usageError(f"xclip failed ({result.returncode})")
                return failed(cmndOutcome)
        b_io.ann.note(f"DISPLAY={os.environ['DISPLAY']} {shlex.join(sessionsLib.openUriCommand(uri))}")
        result = sessionsLib.openUriSend(uri)
        if result.returncode != 0:
            b_io.eh.problem_usageError(f"code --open-url failed ({result.returncode}): {result.stderr.strip()}")
            return failed(cmndOutcome)
        if clipText is not None:
            if not shutil.which(sessionsLib.pasteCommand()[0]):
                b_io.ann.note("xdotool is not installed (rawBisos-sbom.pcs): the prompt is on the clipboard: Ctrl+V, then Enter")
                return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)
            b_io.ann.note(f"DISPLAY={os.environ['DISPLAY']} {shlex.join(sessionsLib.pasteCommand())}")
            result = sessionsLib.pasteSend()
            if result.returncode != 0:
                b_io.eh.problem_usageError(f"xdotool failed ({result.returncode}): {result.stderr.strip()}; the prompt is on the clipboard: Ctrl+V")
                return failed(cmndOutcome)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        return _promptArgsSpec()


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "list" :comment "Running sessions, one tab-separated line each" :extent "verify" :ro "cli" :parsMand "" :parsOpt "mode cwd" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<list>>  *Running sessions, one tab-separated line each*  =verify= parsOpt=mode cwd ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class list(cs.Cmnd):
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


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "latest" :comment "The sessionId of the most recently active session" :extent "verify" :ro "cli" :parsMand "" :parsOpt "mode cwd" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<latest>>  *The sessionId of the most recently active session*  =verify= parsOpt=mode cwd ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class latest(cs.Cmnd):
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


####+BEGIN: b:py3:cs:framework/main :csInfo "csInfo" :noCmndEntry "examples" :extraParamsHook "g_extraParams" :importedCmndsModules "g_importedCmndsModules"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] =g_csMain= (csInfo, _examples_, g_extraParams, g_importedCmndsModules)
#+end_org """

if __name__ == '__main__':
    cs.main.g_csMain(
        csInfo=csInfo,
        noCmndEntry=examples,  # specify a Cmnd name
        extraParamsHook=g_extraParams,
        ignoreUnknownParams=False,  # True is for Uploaded Modules
        importedCmndsModules=g_importedCmndsModules,
    )

####+END:

####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
