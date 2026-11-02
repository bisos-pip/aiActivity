# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= classifying AI-Activities: root or sub, home, native or foreign to a Session-Root.
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
** This File: /bisos/git/auth/bxRepos/bisos-pip/aiActivity/py3/bisos/aiActivity/activityModel_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inDev"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['activityModel_csu'], }
csInfo['version'] = '202611020000'
csInfo['status']  = 'inDev'
csInfo['panel'] = 'activityModel_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]]

The model and terminology of AI-Activities, as file-system facts (the bisos.aiActivity
ModelAndTerminology panel):

- *AI-Activity*: a directory with a =CLAUDE.md=.
- *AI-Activity Root*: one where =aiActivity.cs -i initiate= was run: =CLAUDE.md=, =.claude/= and
  =AI-WORKFLOW.org=. It carries the tooling.
- *Sub-AI-Activity*: an AI-Activity that is not a root (=initiateSub=). /Homogeneous/ when it has
  no =.claude/skills= of its own or one resolving to its home's; /heterogeneous/ otherwise.
- *Home*: of a directory, the first AI-Activity Root at or above it.
- *Session-Root*: a session's working directory; it must be an AI-Activity Root.
- *Native* / *Foreign*: an AI-Activity is native to a session whose Session-Root is its home, and
  foreign otherwise. A nested root (an AI-Activity Root inside another's tree) is its own home, so
  foreign to a session at the outer root: reported with a warning.

Only the file system is read: no =CLAUDE.md= chain, no session state. What a session reached, and
other running sessions, are for the callers (the /bx- commands, Blee) to add.

** Status: In development
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

import json
import pathlib


# ---------------------------------------------------------------------------
# File-system facts
# ---------------------------------------------------------------------------

def canonical(path: typing.Union[str, pathlib.Path]) -> pathlib.Path:
    """The true name of path (symlinks resolved, ~ expanded)."""
    return pathlib.Path(path).expanduser().resolve()


def isAiActivity(dirPath: pathlib.Path) -> bool:
    return (dirPath / 'CLAUDE.md').is_file()


def isAiActivityRoot(dirPath: pathlib.Path) -> bool:
    """A root carries the tooling (.claude/) and the invariants (AI-WORKFLOW.org)."""
    return (isAiActivity(dirPath)
            and (dirPath / '.claude').is_dir()
            and (dirPath / 'AI-WORKFLOW.org').exists())


def _atOrAbove(dirPath: pathlib.Path) -> typing.List[pathlib.Path]:
    return [dirPath] + list(dirPath.parents)


def activityOf(dirPath: pathlib.Path) -> typing.Optional[pathlib.Path]:
    """The AI-Activity at or above dirPath: the nearest directory with a CLAUDE.md."""
    return next((each for each in _atOrAbove(dirPath) if isAiActivity(each)), None)


def homeOf(dirPath: pathlib.Path) -> typing.Optional[pathlib.Path]:
    """The first AI-Activity Root at or above dirPath."""
    return next((each for each in _atOrAbove(dirPath) if isAiActivityRoot(each)), None)


def skillsTarget(dirPath: pathlib.Path) -> typing.Optional[pathlib.Path]:
    skills = dirPath / '.claude' / 'skills'
    return skills.resolve() if skills.exists() else None


def activityType(dirPath: pathlib.Path) -> typing.Optional[str]:
    """The activity named by AI-Activity.org's link target (its directory's name)."""
    activityOrg = dirPath / 'AI-Activity.org'
    if not activityOrg.is_symlink():
        return None
    return activityOrg.resolve().parent.name


def activityClassify(
        dirPath: typing.Union[str, pathlib.Path],
        sessionRoot: typing.Union[str, pathlib.Path, None] = None,
) -> typing.Dict[str, typing.Any]:
    """Classify dirPath's AI-Activity; relative to sessionRoot when given. Values are strings or None."""
    given = canonical(dirPath)
    result: typing.Dict[str, typing.Any] = {
        'dir': str(given), 'aiActivity': None, 'kind': 'none', 'home': None,
        'homogeneity': None, 'activityType': None, 'nestedIn': None,
        'sessionRoot': None, 'sessionRootValid': None, 'relation': None, 'warnings': [],
    }
    if not given.is_dir():
        result['warnings'].append(f"not a directory: {given}")
        return result
    activity = activityOf(given)
    home = homeOf(given)
    result['home'] = str(home) if home else None
    if home:
        outer = homeOf(home.parent)
        if outer:
            result['nestedIn'] = str(outer)
            result['warnings'].append(f"nested root: {home} is inside the AI-Activity Root {outer}")
    if activity:
        result['aiActivity'] = str(activity)
        result['activityType'] = activityType(activity)
        if isAiActivityRoot(activity):
            result['kind'] = 'root'
        else:
            result['kind'] = 'sub'
            own = skillsTarget(activity)
            homeSkills = skillsTarget(home) if home else None
            result['homogeneity'] = ('heterogeneous' if own and own != homeSkills
                                     else 'homogeneous')
            if not home:
                result['warnings'].append(f"no AI-Activity Root above the sub {activity}")
    if sessionRoot is not None:
        root = canonical(sessionRoot)
        result['sessionRoot'] = str(root)
        result['sessionRootValid'] = isAiActivityRoot(root)
        if not result['sessionRootValid']:
            result['warnings'].append(f"the Session-Root {root} is not an AI-Activity Root")
        if activity and home:
            result['relation'] = 'native' if home == root else 'foreign'
            if result['relation'] == 'foreign' and result['sessionRootValid'] and root in home.parents:
                result['warnings'].append(
                    f"foreign although under the Session-Root: its home {home} is a nested root")
    return result


def sessionRootJudge(
        dirPath: typing.Union[str, pathlib.Path],
) -> typing.Tuple[bool, str]:
    """Rule 1: is dirPath an AI-Activity Root? Returns (ok, one-line verdict)."""
    given = canonical(dirPath)
    if not given.is_dir():
        return False, f"REFUSED: not a directory: {given}"
    if isAiActivityRoot(given):
        return True, f"OK: {given} is an AI-Activity Root"
    home = homeOf(given)
    what = ("a sub-AI-Activity" if isAiActivity(given)
            else "not an AI-Activity")
    nearest = f"; the nearest AI-Activity Root above is {home}" if home else "; no AI-Activity Root above it"
    return False, f"REFUSED: {given} is {what}{nearest}"


_reportOrder = ('dir', 'aiActivity', 'kind', 'home', 'homogeneity', 'activityType', 'nestedIn',
                'sessionRoot', 'sessionRootValid', 'relation')


def reportLines(result: typing.Dict[str, typing.Any]) -> typing.List[str]:
    lines = [f"{key + ':':<17} {result[key]}" for key in _reportOrder
             if result[key] is not None]
    lines.extend(f"{'warning:':<17} {each}" for each in result['warnings'])
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
** [[elisp:(org-cycle)][| *DocStr | ] Examples of the activity model commands.
    #+end_org """
    od = collections.OrderedDict
    cmnd = cs.examples.cmndEnter

    cs.examples.menuChapter('=activityReport= -- root or sub, home, native or foreign (file system only)')
    cmnd('activityReport', comment="# This directory's AI-Activity")
    cmnd('activityReport', pars=od([('sessionRoot', '.')]), args='.',
         comment="# Relative to a Session-Root: native or foreign")
    cmnd('activityReport', pars=od([('sessionRoot', '.'), ('format', 'json')]), args='.',
         comment="# The same, as JSON, for callers")

    cs.examples.menuChapter('=sessionRootCheck= -- rule 1: a Session-Root must be an AI-Activity Root')
    cmnd('sessionRootCheck', comment="# This directory: OK, or REFUSED naming the nearest root above")


def commonParamsSpecify(csParams: cs.param.CmndParamDict) -> None:

    csParams.parDictAdd(
        parName='sessionRoot',
        parDescription="activityReport: the Session-Root to relate the AI-Activity to (native or foreign).",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--sessionRoot',
    )
    csParams.parDictAdd(
        parName='format',
        parDescription="activityReport: text (default) or json.",
        parDataType=None,
        parDefault='text',
        parChoices=['text', 'json'],
        argparseShortOpt=None,
        argparseLongOpt='--format',
    )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "activityReport" :comment "Classify an AI-Activity" :extent "verify" :ro "cli" :parsMand "" :parsOpt "sessionRoot format" :argsMin 0 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<activityReport>>  *Classify an AI-Activity*  =verify= parsOpt=sessionRoot format argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class activityReport(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'sessionRoot', 'format', ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             sessionRoot: typing.Optional[str]=None,  # Cs Optional Param
             format: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Classify an AI-Activity"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'sessionRoot': sessionRoot, 'format': format, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Classify the AI-Activity at or above the directory (default: this
one), from the file system only: its directory, root or sub, its home (the AI-Activity Root at or
above it), homogeneous or heterogeneous (a sub), its activity type, a nested root. With
=--sessionRoot=, also whether that is a valid Session-Root and whether the AI-Activity is native or
foreign to it. =--format=json= prints the same as one JSON object. Read-only.
        #+end_org """)
        dirArg = self.cmndArgsGet("0", cmndArgsSpecDict, argsList) or '.'
        format = format or 'text'
        if format not in ('text', 'json'):
            b_io.eh.problem_usageError(f"--format must be text or json, not {format}")
            return failed(cmndOutcome)
        result = activityClassify(dirArg, sessionRoot)
        if format == 'json':
            print(json.dumps(result))
        else:
            for line in reportLines(result):
                print(line)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="dir",
            argDefault='.',
            argChoices=[],
            argDescription="The directory (default: this one)",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "sessionRootCheck" :comment "Rule 1: is the directory an AI-Activity Root" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<sessionRootCheck>>  *Rule 1: is the directory an AI-Activity Root*  =verify= argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class sessionRootCheck(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Rule 1: is the directory an AI-Activity Root"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Rule 1 of the activity model: a Session-Root must be an AI-Activity
Root. Prints one line: =OK: ...=, or =REFUSED: ...= naming what the directory is and the nearest
AI-Activity Root above it. The exit code is 0 either way (PyCS): read the first word. Read-only.
        #+end_org """)
        dirArg = self.cmndArgsGet("0", cmndArgsSpecDict, argsList) or '.'
        ok, verdict = sessionRootJudge(dirArg)
        print(verdict)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="dir",
            argDefault='.',
            argChoices=[],
            argDescription="The directory (default: this one)",
        )
        return cmndArgsSpecDict
