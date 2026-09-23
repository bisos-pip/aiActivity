#!/bin/env python
# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CSXU= for initiating AI collaborative development templates.
#+end_org """

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/panels/bisos-core/bisos-pip/bisos.tocsModules/_nodeBase_/fullUsagePanel-en.org][BISOS Panel]]   [[elisp:(org-cycle)][| ]]

** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO Review Panel's Design and Evolution section.
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
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/auth/bxRepos/bisos-pip/aiActivity/py3/bin/aiActivity.cs
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['aiActivity'], }
csInfo['version'] = '202508030000'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'aiActivity-Panel.org'
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
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

import datetime
import os
import pathlib
import shutil
import sys
import typing

from bisos.pyDblock import updateDblock
import bisos.pyDblock.dblock_particulars  # registers b:ai:file/particulars handler

""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~csuList emacs-list Specifications~  [[elisp:(blee:org:code-block/above-run)][ /Eval Below/ ]] [[elisp:(org-cycle)][| ]]
#+BEGIN_SRC emacs-lisp
(setq  b:py:cs:csuList
  (list
   "bisos.b.userConfig_csu"
   "bisos.b.cwdConfig_csu"
 ))
#+END_SRC
#+RESULTS:
| bisos.b.userConfig_csu | bisos.b.cwdConfig_csu |
#+end_org """

####+BEGIN: b:py3:cs:framework/csuListProc :pyImports t :csuImports t :csuParams t :csxuParams nil
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~Process CSU List~ with /1/ in csuList pyImports=t csuImports=t csuParams=t
#+end_org """

from bisos.b import userConfig_csu
from bisos.b import cwdConfig_csu

csuList = [ 'bisos.b.userConfig_csu', 'bisos.b.cwdConfig_csu', ]

g_importedCmndsModules = cs.csuList_importedModules(csuList)

def g_extraParams():
    csParams = cs.param.CmndParamDict()
    cs.csuList_commonParamsSpecify(csuList, csParams)
    cs.argsparseBasedOnCsParams(csParams)

####+END:


####+BEGIN: b:py3:cs:orgItem/section :title "Common Parameters Specification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

def _detectTemplatesDefault() -> typing.Optional[str]:
    """Probe well-known templates locations in precedence order.

    A user's own clone at ~/aiActivityTemplates (the canonical path
    advertised in the aiActivityTemplates repo README) takes precedence
    over the BISOS-provisioned /bisos/apps/defaults/ai-templates so that
    a customized fork wins over the system copy when both are present.
    Returns the first existing path as a resolved absolute string, or
    None if neither exists (caller must userConfig_set explicitly).

    This function is used ONLY as a last-resort fallback when both the
    CLI --templates override and the persisted user-config value are
    absent. See _resolveTemplatesBase.
    """
    candidates = [
        pathlib.Path('~/aiActivityTemplates').expanduser(),
        pathlib.Path('/bisos/apps/defaults/ai-templates'),
    ]
    for candidate in candidates:
        if candidate.is_dir():
            return str(candidate)
    return None


def _resolveTemplatesBase(cliOverride: typing.Optional[str]) -> typing.Optional[str]:
    """Resolve the templates base with precedence:

    1. Explicit --templates CLI override (if provided by the user)
    2. Per-directory config: <cwd>/.<csxu-name>/fps/templates/value (cwdConfig)
    3. Global user-config value: ~/.config/bisos/<csxu-name>/fps/templates/value
    4. Auto-detect fallback (~/aiActivityTemplates, then BISOS path)

    Returns None only if all four fail. The user-config value MUST take
    precedence over the auto-detect fallback --- otherwise a userConfig_set
    to a non-canonical path (e.g. a T-Mobile fork) would be silently
    ignored whenever an auto-detectable path also exists on disk.
    """
    if cliOverride:
        return cliOverride
    cwdStored = cwdConfig_csu.parGet('templates')
    if cwdStored:
        return cwdStored
    stored = userConfig_csu.parGet('templates')
    if stored:
        return stored
    return _detectTemplatesDefault()


def _resolveActivity(cliOverride: typing.Optional[str]) -> typing.Optional[str]:
    """Resolve activity with precedence:

    1. Explicit --activity CLI override (if provided)
    2. Per-directory cwdConfig value at ./.<csxu-name>/fps/activity/value

    Returns None if neither is set; callers should treat that as a
    usage error.
    """
    if cliOverride:
        return cliOverride
    return cwdConfig_csu.parGet('activity')


def _deduceCwdConfig(
        targetDir: pathlib.Path,
) -> typing.Tuple[typing.Optional[str], typing.Optional[str]]:
    """Deduce (templatesBase, activity) for an already-initiated directory
    by reading its =AI-WORKFLOW.org= and =AI-Activity.org= symlink targets.

    AI-WORKFLOW.org points at =<templatesBase>/mother/AI-WORKFLOW.org=,
    so the templates base is the target's parent's parent.

    AI-Activity.org points at =<templatesBase>/<activity>/AI-Activity.org=,
    so the activity is the target's parent name.

    Fallback: if AI-WORKFLOW.org is missing or not a symlink, derive the
    templates base from AI-Activity.org too (its target's parent's parent).

    Returns =(None, None)= for either field it could not deduce.
    """
    templatesBase: typing.Optional[str] = None
    activity: typing.Optional[str] = None

    workflowOrg = targetDir / 'AI-WORKFLOW.org'
    if workflowOrg.is_symlink():
        wfTarget = pathlib.Path(workflowOrg.readlink())
        if not wfTarget.is_absolute():
            wfTarget = (workflowOrg.parent / wfTarget).resolve()
        # <templatesBase>/mother/AI-WORKFLOW.org --> two parents up.
        templatesBase = str(wfTarget.parent.parent)

    activityOrg = targetDir / 'AI-Activity.org'
    if activityOrg.is_symlink():
        aTarget = pathlib.Path(activityOrg.readlink())
        if not aTarget.is_absolute():
            aTarget = (activityOrg.parent / aTarget).resolve()
        # <templatesBase>/<activity>/AI-Activity.org --> activity is parent
        # dir name; templatesBase is parent's parent (fallback).
        activity = aTarget.parent.name
        if templatesBase is None:
            templatesBase = str(aTarget.parent.parent)

    return (templatesBase, activity)


def _recordCwdConfig(
        templatesBase: typing.Optional[str],
        activity: typing.Optional[str],
) -> typing.List[str]:
    """Write =templates= and =activity= to cwdConfig if not already at
    the given values. Skips =None= fields. Returns a list of
    human-readable notes describing what was written or skipped ---
    caller reports them via =b_io.ann.note=.

    Idempotent: writes only when the stored value differs, so repeat
    invocations after the first one produce =SKIP (unchanged)= lines.
    """
    notes: typing.List[str] = []
    if templatesBase is not None:
        current = cwdConfig_csu.parGet('templates')
        if current != templatesBase:
            cwdConfig_csu.parSet('templates', templatesBase)
            notes.append(f"cwdConfig: templates={templatesBase}")
        else:
            notes.append(f"cwdConfig: templates unchanged ({templatesBase})")
    if activity is not None:
        current = cwdConfig_csu.parGet('activity')
        if current != activity:
            cwdConfig_csu.parSet('activity', activity)
            notes.append(f"cwdConfig: activity={activity}")
        else:
            notes.append(f"cwdConfig: activity unchanged ({activity})")
    return notes


def _detectUser() -> str:
    """Best-effort user identity for the provenance line.

    Fallback chain: =USER= env var, then =LOGNAME=, then =os.getlogin()=
    (which raises OSError under nohup / detached shells), then pwd
    module by real uid. Only returns "unknown" if all four fail.
    """
    for env in ('USER', 'LOGNAME'):
        val = os.environ.get(env)
        if val:
            return val
    try:
        return os.getlogin()
    except OSError:
        pass
    try:
        import pwd
        return pwd.getpwuid(os.getuid()).pw_name
    except Exception:
        pass
    return 'unknown'


def _writeProvenanceLine(dst: pathlib.Path, templatesBase: str) -> None:
    """Insert a multi-line org-comment provenance block into a freshly
    safe-copied editable file (=AI-DevStatus.org=, =AI-WorkPlan.org=).

    The block records the birth-certificate values of the =initiate= /
    =initiateSub= invocation: date, user, templates base actually used,
    and the exact =sys.argv=. It is *plain org text*, never regenerated
    by any dblock machinery (Python or elisp) --- Elisp dblock expanders
    have no access to invocation context, so provenance must be inert
    text written once at install time.

    Placement: immediately after the last =#+= header directive
    (title/date/options/tags) in the file, before any org content or
    dblocks. This is robust to reordering of header directives.
    """
    text = dst.read_text()
    lines = text.splitlines(keepends=True)

    # Find the index of the last #+ directive at the top of the file.
    # Header directives may be interleaved with blank lines; scan until
    # the first non-blank, non-#+ line breaks the header region.
    lastHeaderIdx = -1
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('#+'):
            lastHeaderIdx = idx
        elif stripped == '':
            continue
        else:
            break

    provDate = datetime.datetime.now().astimezone().isoformat(timespec='seconds')
    provUser = _detectUser()
    provCommand = ' '.join(sys.argv)
    provenance = (
        "\n"
        "# Provenance (installed once by aiActivity.cs --- not regenerated):\n"
        f"#   Date:      {provDate}\n"
        f"#   User:      {provUser}\n"
        f"#   Templates: {templatesBase}\n"
        f"#   Command:   {provCommand}\n"
    )

    if lastHeaderIdx < 0:
        # No #+ directives found at top --- prepend to file
        newLines = [provenance] + lines
    else:
        newLines = lines[:lastHeaderIdx + 1] + [provenance] + lines[lastHeaderIdx + 1:]

    dst.write_text(''.join(newLines))


def commonParamsSpecify(
        csParams: cs.param.CmndParamDict,
) -> None:

    csParams.parDictAdd(
        parName='activity',
        parDescription="Template activity type matching a directory under <templatesBase>/.",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--activity',
        parPermanence=["cwdConfig"],
    )
    csParams.parDictAdd(
        parName='templates',
        parDescription="Override templatesBase file parameter for this run.",
        parDataType=None,
        parDefault=None,  # do NOT auto-fill; would mask userConfig_set value.
                          # Auto-detect happens in _resolveTemplatesBase at
                          # read time, only when both CLI override and
                          # user-config are absent.
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--templates',
        parPermanence=["userConfig", "cwdConfig"],
    )
    csParams.parDictAdd(
        parName='noLink',
        parDescription=(
            "Override symlink behavior: safe-copy the specified file instead "
            "of installing it as a symlink. Useful for --activity=custom "
            "activities where AI-Activity.org must be a per-project copy, not "
            "a shared symlink to the template. Accepts a single filename "
            "(e.g. AI-Activity.org). Multi-file support to come later via "
            "bisos.b framework improvements."
        ),
        parDataType=None,
        parDefault=None,
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--noLink',
    )


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

        templatesBaseStr = _resolveTemplatesBase(None)

        cs.examples.myName(cs.G.icmMyName(), cs.G.icmMyFullName())
        cs.examples.commonBrief()

        userConfig_csu.examples_csu().pyCmnd()
        cwdConfig_csu.examples_csu().pyCmnd()

        cs.examples.menuChapter('=cwdConfig_record= -- deduce & record cwdConfig for an already-initiated directory')
        cmnd('cwdConfig_record',
             pars=od([]),
             comment="# Deduce templates/activity from symlinks; write to ./.aiActivity.cs/")

        cs.examples.menuChapter('=aiSuspend= / =aiResume= -- suspend and resume AI collaboration')
        cmnd('aiSuspend',
             pars=od([]),
             comment="# Remove symlinks/.claude, rename WorkPlan/DevStatus to .dormant")
        cmnd('aiResume',
             pars=od([]),
             comment="# Restore .dormant files and re-install symlinks/.claude")

        cs.examples.menuChapter('=refresh= -- re-copy safe-copied invariants (CLAUDE.md) from templates')
        cmnd('refresh',
             pars=od([]),
             comment="# Re-copy CLAUDE.md, backfill missing invariant symlinks (e.g. AI-Outputs.org)")


        cs.examples.menuChapter('=deClaudify= -- remove AI collaboration files')
        cmnd('deClaudify',
             pars=od([]),
             comment="# Remove AI files from current directory")

        # Read cwdConfig to decide whether initiate/initiateSub can be invoked bare.
        cwdActivity = cwdConfig_csu.parGet('activity')

        cs.examples.menuChapter('=initiate= -- install AI templates into current directory')
        if templatesBaseStr is None:
            cmnd('initiate',
                 pars=od([('activity', '<activity>')]),
                 comment="# templates not set — run userConfig_set --parName=templates first")
            activities = []
        else:
            templatesBase = pathlib.Path(templatesBaseStr)
            excludedDirs = {'mother', 'test'}
            activities = sorted([
                d.name for d in templatesBase.iterdir()
                if d.is_dir() and d.name not in excludedDirs and not d.name.startswith('.')
            ])
            for activity in activities:
                cmnd('initiate',
                     pars=od([('activity', activity)]),
                     comment=f"# Install {activity} templates (auto-persists activity to cwdConfig)")
                if activity == 'custom':
                    cmnd('initiate',
                         pars=od([('activity', activity), ('noLink', 'AI-Activity.org')]),
                         comment=f"# Same, but safe-copy AI-Activity.org (project-specific, editable)")

        cs.examples.menuChapter('=initiateSub= -- slim subproject overlay (requires initiated parent)')
        if templatesBaseStr is None:
            cmnd('initiateSub',
                 pars=od([('activity', '<activity>')]),
                 comment="# templates not set — run userConfig_set --parName=templates first")
        else:
            for activity in activities:
                cmnd('initiateSub',
                     pars=od([('activity', activity)]),
                     comment=f"# Install slim {activity} overlay (auto-persists activity to cwdConfig)")
                if activity == 'custom':
                    cmnd('initiateSub',
                         pars=od([('activity', activity), ('noLink', 'AI-Activity.org')]),
                         comment=f"# Same, but safe-copy AI-Activity.org (project-specific, editable)")

        if cwdActivity:
            cs.examples.menuChapter('=initiate/initiateSub Based on CWD Setting= -- Based on ./.aiActivity.cs')
            # cwdConfig supplies activity — But dont show the bare invocation.
            cmnd('initiate',
                 pars=od([('activity', f"{cwdActivity}"), ('templates', f"{templatesBaseStr}"),]),
                 comment=f"# from cwdConfig")
            cmnd('initiateSub',
                 pars=od([('activity', f"{cwdActivity}"), ('templates', f"{templatesBaseStr}"),]),
                 comment=f"# from cwdConfig")

        cs.examples.menuChapter('=listClaudesPath= -- show AI Activities in effect from cwd to repo root')
        cmnd('listClaudesPath',
             pars=od([]),
             comment="# Walk up to git repo root; list each CLAUDE.md + AI-Activity.org target")

        # Migration reminder: old dotdir present but new one absent — shown last
        oldDotdir = pathlib.Path.cwd() / '.startAiActivity.cs'
        newDotdir = pathlib.Path.cwd() / '.aiActivity.cs'
        if oldDotdir.exists() and not newDotdir.exists():
            cs.examples.menuChapter('=MIGRATION NEEDED= -- rename dotdir from old startAiActivity name')
            literal(f"mv .startAiActivity.cs .aiActivity.cs")

        return(cmndOutcome)



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "initiate" :comment "Install AI templates via symlinks and safe-copy" :extent "verify" :ro "cli" :parsMand "" :parsOpt "activity templates noLink" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<initiate>>  =verify= parsOpt="activity templates noLink" ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class initiate(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'activity', 'templates', 'noLink', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             activity: typing.Optional[str]=None,    # Cs Optional Param
             templates: typing.Optional[str]=None,   # Cs Optional Param
             noLink: typing.Optional[str]=None,      # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'activity': activity, 'templates': templates, 'noLink': noLink, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        activity = csParam.mappedValue('activity', activity)
        templates = csParam.mappedValue('templates', templates)
        noLink = csParam.mappedValue('noLink', noLink)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Install AI collaborative development templates.
Symlinks constant files from mother/. Symlinks AI-Activity.org from <activity>/.
Safe-copies AI-DevStatus.org and AI-WorkPlan.org from <activity>/ (falling back to mother/).
Expands b:ai:file/particulars dblock in copied files using pure Python.
Target directory is always cwd. Activity is resolved from --activity CLI arg,
falling back to cwdConfig at ./.<csxu-name>/fps/activity/value.
        #+end_org """)

        activity = _resolveActivity(activity)
        if not activity:
            b_io.eh.problem_usageError(
                "activity not specified. Pass --activity=<name> or set with: "
                "aiActivity.cs -i cwdConfig_set --parName=activity --parValue=<name>")
            return failed(cmndOutcome)

        templatesBaseStr = _resolveTemplatesBase(templates)
        if templatesBaseStr is None:
            b_io.eh.problem_usageError(
                "templates not configured. Run: aiActivity.cs -i userConfig_set --parName=templates --parValue=/path/to/templates")
            return failed(cmndOutcome)
        templatesBase = pathlib.Path(templatesBaseStr)

        activityDir = templatesBase / activity
        if not activityDir.is_dir():
            b_io.eh.problem_usageError(f"Activity directory not found: {activityDir}")
            return failed(cmndOutcome)

        targetDir = pathlib.Path.cwd()

        # Auto-record cwdConfig from the templates base and activity actually
        # used. Unconditional on successful install: the ground truth for
        # "this directory was initiated with these values." Filter unchanged
        # notes so common re-initiate paths stay quiet.
        for _n in _recordCwdConfig(str(templatesBase), activity):
            if 'unchanged' not in _n:
                b_io.ann.note(_n)

        motherDir = templatesBase / 'mother'

        # CLAUDE.md — always safe-copied (never a symlink). Claude Code
        # resolves symlinks before reading, which would cause @./ imports
        # inside a symlinked CLAUDE.md to resolve against the templates
        # directory instead of this project. No provenance line: CLAUDE.md
        # is meant to be the equivalent of a symlink (pristine template
        # content). Use `refresh` to re-copy after templates change.
        claudeMdSrc = motherDir / 'CLAUDE.md'
        claudeMdDst = targetDir / 'CLAUDE.md'
        if claudeMdDst.exists() or claudeMdDst.is_symlink():
            b_io.ann.note(f"SKIP (exists): {claudeMdDst}")
        else:
            shutil.copy2(claudeMdSrc, claudeMdDst)
            b_io.ann.note(f"COPIED: {claudeMdSrc} -> {claudeMdDst}")

        # Other constant files — symlinked to mother/. If --noLink matches,
        # safe-copy instead. AI-Outputs.org is optional: templates trees that
        # don't ship it (e.g. bxexamples, rana-notes as of this writing) are
        # skipped rather than treated as an error.
        constantFiles = ['AI-WORKFLOW.org', 'AI-Outputs.org']
        for fname in constantFiles:
            src = motherDir / fname
            dst = targetDir / fname
            if not src.exists() and not src.is_symlink():
                b_io.ann.note(f"SKIP (no such file in templates): {src}")
                continue
            if dst.exists() or dst.is_symlink():
                b_io.ann.note(f"SKIP (exists): {dst}")
            elif noLink == fname:
                shutil.copy2(src, dst)
                b_io.ann.note(f"COPIED (--noLink={fname}): {src} -> {dst}")
            else:
                dst.symlink_to(src)
                b_io.ann.note(f"SYMLINKED: {dst} -> {src}")

        # AI-Activity.org — usually symlinked to activity/. If --noLink
        # matches, safe-copy instead (typical --activity=custom use case).
        generalSrc = activityDir / 'AI-Activity.org'
        generalDst = targetDir / 'AI-Activity.org'
        if generalDst.exists() or generalDst.is_symlink():
            b_io.ann.note(f"SKIP (exists): {generalDst}")
        elif noLink == 'AI-Activity.org':
            shutil.copy2(generalSrc, generalDst)
            b_io.ann.note(f"COPIED (--noLink=AI-Activity.org): {generalSrc} -> {generalDst}")
        else:
            generalDst.symlink_to(generalSrc)
            b_io.ann.note(f"SYMLINKED: {generalDst} -> {generalSrc}")

        # Initial files — safe-copied from activity/, falling back to mother/
        initialFiles = ['AI-DevStatus.org', 'AI-WorkPlan.org']
        for fname in initialFiles:
            activitySrc = activityDir / fname
            motherSrc = motherDir / fname
            src = activitySrc if activitySrc.exists() else motherSrc
            dst = targetDir / fname
            if dst.exists():
                b_io.ann.note(f"SKIP (exists): {dst}")
            else:
                shutil.copy2(src, dst)
                b_io.ann.note(f"COPIED: {src} -> {dst}")
                _writeProvenanceLine(dst, templatesBaseStr)
                b_io.ann.note(f"PROVENANCE-WRITTEN: {dst}")
                updateDblock.expandAll(dst)
                b_io.ann.note(f"DBLOCK-UPDATED: {dst}")

        # .claude/ — activity-oriented symlinks so the same activity produces
        # identical .claude/ layouts across every project that uses it.
        # For each entry (settings.json file, commands/ directory), prefer the
        # activity's _claude/<entry> when present, else fall back to mother/_claude/<entry>.
        # settings.local.json is a per-machine overlay — never installed from templates.
        claudeDstDir = targetDir / '.claude'
        claudeDstDir.mkdir(exist_ok=True)

        for claudeEntry in ['settings.json', 'commands']:
            activityClaudeSrc = activityDir / '_claude' / claudeEntry
            motherClaudeSrc = motherDir / '_claude' / claudeEntry
            claudeSrc = activityClaudeSrc if activityClaudeSrc.exists() else motherClaudeSrc
            if not claudeSrc.exists():
                continue
            claudeDst = claudeDstDir / claudeEntry
            if claudeDst.exists() or claudeDst.is_symlink():
                b_io.ann.note(f"SKIP (exists): {claudeDst}")
            else:
                claudeDst.symlink_to(claudeSrc)
                b_io.ann.note(f"SYMLINKED: {claudeDst} -> {claudeSrc}")

        # .claude/skills/ — skills live at activity root as _skills/ (not _claude/skills/)
        # so they're independently visible to humans and other tools. Symlinked into
        # .claude/skills/ so Claude Code can discover them.
        activitySkillsSrc = activityDir / '_skills'
        motherSkillsSrc = motherDir / '_skills'
        skillsSrc = activitySkillsSrc if activitySkillsSrc.exists() else motherSkillsSrc
        if skillsSrc.exists():
            skillsDst = claudeDstDir / 'skills'
            if skillsDst.exists() or skillsDst.is_symlink():
                b_io.ann.note(f"SKIP (exists): {skillsDst}")
            else:
                skillsDst.symlink_to(skillsSrc)
                b_io.ann.note(f"SYMLINKED: {skillsDst} -> {skillsSrc}")

        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults=f"AI templates initiated for activity={activity} at {targetDir}",
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "initiateSub" :comment "Install slim subproject AI-collaboration overlay (requires initiated parent)" :extent "verify" :ro "cli" :parsMand "" :parsOpt "activity templates noLink" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<initiateSub>>  =verify= parsOpt="activity templates noLink" ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class initiateSub(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'activity', 'templates', 'noLink', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             activity: typing.Optional[str]=None,    # Cs Optional Param
             templates: typing.Optional[str]=None,   # Cs Optional Param
             noLink: typing.Optional[str]=None,      # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'activity': activity, 'templates': templates, 'noLink': noLink, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        activity = csParam.mappedValue('activity', activity)
        templates = csParam.mappedValue('templates', templates)
        noLink = csParam.mappedValue('noLink', noLink)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Install subproject AI-collaboration overlay.
Installs only AI-Activity.org (symlink), AI-DevStatus.org (safe-copy),
AI-WorkPlan.org (safe-copy), and a slim CLAUDE.md (symlink to
mother/initiateSub/CLAUDE.md) that imports only the local trio.
Does NOT install AI-WORKFLOW.org or .claude/ — those are inherited
from a parent directory that was previously initiated.
Target directory is always cwd. Activity is resolved from --activity CLI arg,
falling back to cwdConfig at ./.<csxu-name>/fps/activity/value.
Refuses if no initiated parent is found (walks up looking for a
aiActivity-signature CLAUDE.md symlink) or if the target directory
already has a CLAUDE.md.
        #+end_org """)

        activity = _resolveActivity(activity)
        if not activity:
            b_io.eh.problem_usageError(
                "activity not specified. Pass --activity=<name> or set with: "
                "aiActivity.cs -i cwdConfig_set --parName=activity --parValue=<name>")
            return failed(cmndOutcome)

        templatesBaseStr = _resolveTemplatesBase(templates)
        if templatesBaseStr is None:
            b_io.eh.problem_usageError(
                "templates not configured. Run: aiActivity.cs -i userConfig_set --parName=templates --parValue=/path/to/templates")
            return failed(cmndOutcome)
        templatesBase = pathlib.Path(templatesBaseStr).resolve()

        activityDir = templatesBase / activity
        if not activityDir.is_dir():
            b_io.eh.problem_usageError(f"Activity directory not found: {activityDir}")
            return failed(cmndOutcome)

        subClaudeSrc = templatesBase / 'mother' / 'initiateSub' / 'CLAUDE.md'
        if not subClaudeSrc.exists():
            b_io.eh.problem_usageError(f"Subproject CLAUDE.md template not found: {subClaudeSrc}")
            return failed(cmndOutcome)

        targetDir = pathlib.Path.cwd()

        # Refuse if target already has a CLAUDE.md (avoid clobbering existing initiate/initiateSub)
        localClaude = targetDir / 'CLAUDE.md'
        if localClaude.exists() or localClaude.is_symlink():
            b_io.eh.problem_usageError(
                f"CLAUDE.md already exists at {targetDir}. "
                "Run deClaudify first if you meant to reinstall.")
            return failed(cmndOutcome)

        # Precondition: walk up looking for a aiActivity-signature parent.
        # CLAUDE.md is now safe-copied (not a symlink), so we can't identify a
        # parent by symlink target. Instead we look for the AI-WORKFLOW.org
        # symlink (still an invariant symlink), whose target must land under
        # templatesBase. If not found, refuse — initiateSub requires an
        # initiated parent.
        parent = targetDir.parent
        foundBase = None
        while True:
            parentWorkflow = parent / 'AI-WORKFLOW.org'
            if parentWorkflow.is_symlink():
                linkTarget = pathlib.Path(parentWorkflow.readlink())
                if not linkTarget.is_absolute():
                    linkTarget = (parentWorkflow.parent / linkTarget).resolve()
                else:
                    linkTarget = linkTarget.resolve()
                try:
                    linkTarget.relative_to(templatesBase)
                    foundBase = parent
                    break
                except ValueError:
                    pass  # symlink target isn't under templatesBase — keep walking
            if parent.parent == parent:
                break  # reached filesystem root
            parent = parent.parent

        if foundBase is None:
            b_io.eh.problem_usageError(
                f"No initiated parent found for {targetDir}. "
                f"Walked up to / looking for an AI-WORKFLOW.org symlink pointing under {templatesBase}. "
                "Run 'initiate' at a parent directory first, or use 'initiate' here "
                "if this should be the base.")
            return failed(cmndOutcome)

        b_io.ann.note(f"Initiated parent found at: {foundBase}")

        # Auto-record cwdConfig from the templates base and activity actually
        # used. Deferred to here so a failed walk-up doesn't leave stale
        # state behind. Filter unchanged notes so re-runs stay quiet.
        for _n in _recordCwdConfig(str(templatesBase), activity):
            if 'unchanged' not in _n:
                b_io.ann.note(_n)

        # Install slim CLAUDE.md — always safe-copied (never a symlink).
        # Claude Code resolves symlinks before reading, which would cause
        # @./ imports inside a symlinked CLAUDE.md to resolve against the
        # templates directory instead of this project. No provenance line:
        # CLAUDE.md is meant to be the equivalent of a symlink.
        shutil.copy2(subClaudeSrc, localClaude)
        b_io.ann.note(f"COPIED: {subClaudeSrc} -> {localClaude}")

        # AI-Activity.org — usually symlinked to activity/. If --noLink
        # matches, safe-copy instead (typical --activity=custom use case).
        activitySrc = activityDir / 'AI-Activity.org'
        activityDst = targetDir / 'AI-Activity.org'
        if activityDst.exists() or activityDst.is_symlink():
            b_io.ann.note(f"SKIP (exists): {activityDst}")
        elif noLink == 'AI-Activity.org':
            shutil.copy2(activitySrc, activityDst)
            b_io.ann.note(f"COPIED (--noLink=AI-Activity.org): {activitySrc} -> {activityDst}")
        else:
            activityDst.symlink_to(activitySrc)
            b_io.ann.note(f"SYMLINKED: {activityDst} -> {activitySrc}")

        # Initial files — safe-copied from activity/, falling back to mother/
        motherDir = templatesBase / 'mother'
        initialFiles = ['AI-DevStatus.org', 'AI-WorkPlan.org']
        for fname in initialFiles:
            activityFileSrc = activityDir / fname
            motherFileSrc = motherDir / fname
            src = activityFileSrc if activityFileSrc.exists() else motherFileSrc
            dst = targetDir / fname
            if dst.exists():
                b_io.ann.note(f"SKIP (exists): {dst}")
            else:
                shutil.copy2(src, dst)
                b_io.ann.note(f"COPIED: {src} -> {dst}")
                _writeProvenanceLine(dst, templatesBaseStr)
                b_io.ann.note(f"PROVENANCE-WRITTEN: {dst}")
                updateDblock.expandAll(dst)
                b_io.ann.note(f"DBLOCK-UPDATED: {dst}")

        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults=f"Subproject AI-collaboration overlay installed for activity={activity} at {targetDir} (inherits from {foundBase})",
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "aiSuspend" :comment "Suspend AI collaboration: remove symlinks/.claude, stash editable files" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<aiSuspend>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class aiSuspend(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Suspend AI collaboration in current directory.
Removes symlinks (AI-WORKFLOW.org, AI-Outputs.org, AI-Activity.org, plus
any legacy AI-AGENTS.org from pre-merge projects) and =.claude/= entries.
Stashes =CLAUDE.md= as =CLAUDE.md.dormant= (rename; CLAUDE.md is now a
safe-copy, not a symlink). Renames AI-DevStatus.org and AI-WorkPlan.org
to .dormant so they survive and can be restored by aiResume.
        #+end_org """)

        targetDir = pathlib.Path.cwd()

        # Stash CLAUDE.md as CLAUDE.md.dormant. CLAUDE.md is now a safe-copy
        # (see initiate/initiateSub) — rename it aside. aiResume renames it
        # back or re-copies from templates if missing.
        claudeLive = targetDir / 'CLAUDE.md'
        claudeDormant = targetDir / 'CLAUDE.md.dormant'
        if claudeLive.is_symlink():
            # Legacy install: previously symlinked CLAUDE.md. Just remove it.
            claudeLive.unlink()
            b_io.ann.note(f"REMOVED legacy symlink: {claudeLive}")
        elif claudeLive.is_file():
            if claudeDormant.exists() or claudeDormant.is_symlink():
                b_io.ann.note(f"SKIP stash (dormant already exists): {claudeDormant}")
            else:
                claudeLive.rename(claudeDormant)
                b_io.ann.note(f"STASHED: {claudeLive} -> {claudeDormant}")
        else:
            b_io.ann.note(f"SKIP (not present): {claudeLive}")

        # Remove the other symlinks (no dormant preservation needed — they're
        # reinstalled from templates based on the CLAUDE.md.dormant signature).
        # AI-AGENTS.org is retained as legacy cleanup — pre-merge projects
        # have this symlink and aiSuspend should still remove it.
        symlinkFiles = ['AI-AGENTS.org', 'AI-WORKFLOW.org', 'AI-Activity.org', 'AI-Outputs.org']
        for fname in symlinkFiles:
            dst = targetDir / fname
            if dst.is_symlink():
                dst.unlink()
                b_io.ann.note(f"REMOVED symlink: {dst}")
            elif dst.exists():
                b_io.ann.note(f"SKIP (not a symlink, leaving intact): {dst}")
            else:
                b_io.ann.note(f"SKIP (not present): {dst}")

        # Stash editable files by renaming to .dormant
        stashFiles = ['AI-DevStatus.org', 'AI-WorkPlan.org']
        for fname in stashFiles:
            src = targetDir / fname
            dst = targetDir / (fname + '.dormant')
            if src.is_file() and not src.is_symlink():
                if dst.exists():
                    b_io.ann.note(f"SKIP stash (dormant already exists): {dst}")
                else:
                    src.rename(dst)
                    b_io.ann.note(f"STASHED: {src} -> {dst}")
            elif src.is_symlink():
                b_io.ann.note(f"SKIP stash (is a symlink, leaving intact): {src}")
            else:
                b_io.ann.note(f"SKIP stash (not present): {src}")

        # Remove .claude/ symlinked entries
        claudeDstDir = targetDir / '.claude'
        for claudeEntry in ['settings.json', 'commands', 'skills']:
            claudeDst = claudeDstDir / claudeEntry
            if claudeDst.is_symlink():
                claudeDst.unlink()
                b_io.ann.note(f"REMOVED symlink: {claudeDst}")
            elif claudeDst.exists():
                b_io.ann.note(f"SKIP (not a symlink, leaving intact): {claudeDst}")
            else:
                b_io.ann.note(f"SKIP (not present): {claudeDst}")

        if claudeDstDir.is_dir() and not any(claudeDstDir.iterdir()):
            claudeDstDir.rmdir()
            b_io.ann.note(f"REMOVED empty directory: {claudeDstDir}")

        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults=f"aiSuspend complete at {targetDir}",
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "aiResume" :comment "Resume AI collaboration: restore .dormant files and re-install symlinks/.claude" :extent "verify" :ro "cli" :parsMand "" :parsOpt "templates" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<aiResume>>  =verify= parsOpt="templates" ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class aiResume(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'templates', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             templates: typing.Optional[str]=None,   # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'templates': templates, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        templates = csParam.mappedValue('templates', templates)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Resume AI collaboration in current directory.
Restores AI-DevStatus.org and AI-WorkPlan.org from their .dormant copies.
Detects base vs sub mode by walking up looking for a parent
=AI-WORKFLOW.org= symlink under templatesBase: if found, this is a sub
install (slim CLAUDE.md only; AI-WORKFLOW.org and =.claude/= inherited
from parent). Otherwise base. CLAUDE.md is re-copied (safe-copy)
from =mother/initiateSub/CLAUDE.md= (sub) or =mother/CLAUDE.md= (base)
if =CLAUDE.md.dormant= is not present; otherwise the dormant copy is
promoted back. Activity is inferred from the =AI-Activity.org= symlink
target or the =Activity:= header in =AI-WorkPlan.org=.
        #+end_org """)

        targetDir = pathlib.Path.cwd()

        # Restore .dormant files
        stashFiles = ['AI-DevStatus.org', 'AI-WorkPlan.org']
        for fname in stashFiles:
            src = targetDir / (fname + '.dormant')
            dst = targetDir / fname
            if src.exists():
                if dst.exists() or dst.is_symlink():
                    b_io.ann.note(f"SKIP restore (already exists): {dst}")
                else:
                    src.rename(dst)
                    b_io.ann.note(f"RESTORED: {src} -> {dst}")
            else:
                b_io.ann.note(f"SKIP restore (dormant not found): {src}")

        # Determine templates base
        templatesBaseStr = _resolveTemplatesBase(templates)
        if templatesBaseStr is None:
            b_io.eh.problem_usageError(
                "templates not configured. Run: aiActivity.cs -i userConfig_set --parName=templates --parValue=/path/to/templates")
            return failed(cmndOutcome)
        templatesBase = pathlib.Path(templatesBaseStr).resolve()
        motherDir = templatesBase / 'mother'

        # Detect base vs sub mode by walking up for a parent AI-WORKFLOW.org
        # symlink that points under templatesBase.
        subMode = False
        parent = targetDir.parent
        while True:
            parentWorkflow = parent / 'AI-WORKFLOW.org'
            if parentWorkflow.is_symlink():
                linkTarget = pathlib.Path(parentWorkflow.readlink())
                if not linkTarget.is_absolute():
                    linkTarget = (parentWorkflow.parent / linkTarget).resolve()
                else:
                    linkTarget = linkTarget.resolve()
                try:
                    linkTarget.relative_to(templatesBase)
                    subMode = True
                    b_io.ann.note(f"MODE: sub (parent AI-WORKFLOW.org found at {parent})")
                    break
                except ValueError:
                    pass
            if parent.parent == parent:
                break
            parent = parent.parent
        if not subMode:
            b_io.ann.note("MODE: base (no initiated parent found)")

        claudeDormant = targetDir / 'CLAUDE.md.dormant'

        # Infer activity from AI-Activity.org symlink target if it still exists,
        # otherwise from the restored AI-WorkPlan.org dblock header, otherwise fail.
        activityOrg = targetDir / 'AI-Activity.org'
        activity = None
        if activityOrg.is_symlink():
            # target is <templatesBase>/<activity>/AI-Activity.org
            target = pathlib.Path(activityOrg.readlink())
            activity = target.parent.name
        else:
            # try to read Activity: line from AI-WorkPlan.org dblock header
            workPlan = targetDir / 'AI-WorkPlan.org'
            if workPlan.exists():
                for line in workPlan.read_text().splitlines():
                    if line.strip().startswith('Activity:'):
                        activity = line.split(':', 1)[1].strip()
                        break

        if activity is None:
            b_io.eh.problem_usageError(
                "Cannot infer activity. Ensure AI-Activity.org symlink or AI-WorkPlan.org with Activity: header is present.")
            return failed(cmndOutcome)

        activityDir = templatesBase / activity
        if not activityDir.is_dir():
            b_io.eh.problem_usageError(f"Activity directory not found: {activityDir}")
            return failed(cmndOutcome)

        b_io.ann.note(f"Inferred activity: {activity}")

        # Re-install CLAUDE.md — safe-copy (never a symlink). Promote
        # CLAUDE.md.dormant back if present; otherwise re-copy from templates
        # based on the detected mode.
        claudeLive = targetDir / 'CLAUDE.md'
        claudeSrc = (motherDir / 'initiateSub' / 'CLAUDE.md') if subMode else (motherDir / 'CLAUDE.md')
        if claudeLive.exists() or claudeLive.is_symlink():
            b_io.ann.note(f"SKIP (exists): {claudeLive}")
        elif claudeDormant.is_file() and not claudeDormant.is_symlink():
            claudeDormant.rename(claudeLive)
            b_io.ann.note(f"PROMOTED: {claudeDormant} -> {claudeLive}")
        else:
            shutil.copy2(claudeSrc, claudeLive)
            b_io.ann.note(f"COPIED: {claudeSrc} -> {claudeLive}")

        # AI-WORKFLOW.org / AI-Outputs.org: base mode only; subs inherit from
        # parent. AI-Outputs.org is optional in the templates tree.
        if not subMode:
            for fname in ['AI-WORKFLOW.org', 'AI-Outputs.org']:
                src = motherDir / fname
                dst = targetDir / fname
                if not src.exists() and not src.is_symlink():
                    b_io.ann.note(f"SKIP (no such file in templates): {src}")
                    continue
                if dst.exists() or dst.is_symlink():
                    b_io.ann.note(f"SKIP (exists): {dst}")
                else:
                    dst.symlink_to(src)
                    b_io.ann.note(f"SYMLINKED: {dst} -> {src}")

        # Re-install AI-Activity.org symlink (both modes)
        activitySrc = activityDir / 'AI-Activity.org'
        activityDst = targetDir / 'AI-Activity.org'
        if activityDst.exists() or activityDst.is_symlink():
            b_io.ann.note(f"SKIP (exists): {activityDst}")
        else:
            activityDst.symlink_to(activitySrc)
            b_io.ann.note(f"SYMLINKED: {activityDst} -> {activitySrc}")

        # .claude/ entries: base mode only; subs inherit from parent.
        if subMode:
            return cmndOutcome.set(
                opError=b.op.OpError.Success,
                opResults=f"aiResume complete at {targetDir} (activity={activity}, mode=sub)",
            )

        # Re-install .claude/ symlinked entries
        claudeDstDir = targetDir / '.claude'
        claudeDstDir.mkdir(exist_ok=True)
        for claudeEntry in ['settings.json', 'commands']:
            activityClaudeSrc = activityDir / '_claude' / claudeEntry
            motherClaudeSrc = motherDir / '_claude' / claudeEntry
            claudeSrc = activityClaudeSrc if activityClaudeSrc.exists() else motherClaudeSrc
            if not claudeSrc.exists():
                continue
            claudeDst = claudeDstDir / claudeEntry
            if claudeDst.exists() or claudeDst.is_symlink():
                b_io.ann.note(f"SKIP (exists): {claudeDst}")
            else:
                claudeDst.symlink_to(claudeSrc)
                b_io.ann.note(f"SYMLINKED: {claudeDst} -> {claudeSrc}")

        # Re-install .claude/skills/ symlink
        activitySkillsSrc = activityDir / '_skills'
        motherSkillsSrc = motherDir / '_skills'
        skillsSrc = activitySkillsSrc if activitySkillsSrc.exists() else motherSkillsSrc
        if skillsSrc.exists():
            skillsDst = claudeDstDir / 'skills'
            if skillsDst.exists() or skillsDst.is_symlink():
                b_io.ann.note(f"SKIP (exists): {skillsDst}")
            else:
                skillsDst.symlink_to(skillsSrc)
                b_io.ann.note(f"SYMLINKED: {skillsDst} -> {skillsSrc}")

        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults=f"aiResume complete at {targetDir} (activity={activity}, mode=base)",
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "refresh" :comment "Re-copy safe-copied invariants (CLAUDE.md) and backfill missing invariant symlinks (AI-Outputs.org)" :extent "verify" :ro "cli" :parsMand "" :parsOpt "templates" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<refresh>>  =verify= parsOpt="templates" ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class refresh(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'templates', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             templates: typing.Optional[str]=None,   # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'templates': templates, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        templates = csParam.mappedValue('templates', templates)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Re-copy safe-copied invariant files from templates,
and create any missing invariant symlinks (e.g. =AI-Outputs.org= on a
project =initiate=-d before that symlink existed in the templates tree).
Detects base vs sub mode by walking up for a parent =AI-WORKFLOW.org=
symlink under templatesBase: if found, this is a sub install and
=CLAUDE.md= is re-copied from =mother/initiateSub/CLAUDE.md=; otherwise
from =mother/CLAUDE.md=. Missing-symlink backfill (=AI-Outputs.org=) is
base-mode only — subs inherit it from the parent, same as
=AI-WORKFLOW.org=.
Upgrades legacy symlinked =CLAUDE.md= installs by unlinking then copying.
Never touches per-project files (AI-DevStatus.org, AI-WorkPlan.org, or
files installed with =--noLink=). No provenance line: CLAUDE.md is meant
to be the equivalent of a symlink.
        #+end_org """)

        targetDir = pathlib.Path.cwd()

        # Resolve templates base.
        templatesBaseStr = _resolveTemplatesBase(templates)
        if templatesBaseStr is None:
            b_io.eh.problem_usageError(
                "templates not configured. Run: aiActivity.cs -i userConfig_set --parName=templates --parValue=/path/to/templates")
            return failed(cmndOutcome)
        templatesBase = pathlib.Path(templatesBaseStr).resolve()
        motherDir = templatesBase / 'mother'

        # Detect base vs sub mode by walking up for a parent AI-WORKFLOW.org
        # symlink that points under templatesBase.
        subMode = False
        parent = targetDir.parent
        while True:
            parentWorkflow = parent / 'AI-WORKFLOW.org'
            if parentWorkflow.is_symlink():
                linkTarget = pathlib.Path(parentWorkflow.readlink())
                if not linkTarget.is_absolute():
                    linkTarget = (parentWorkflow.parent / linkTarget).resolve()
                else:
                    linkTarget = linkTarget.resolve()
                try:
                    linkTarget.relative_to(templatesBase)
                    subMode = True
                    b_io.ann.note(f"MODE: sub (parent AI-WORKFLOW.org found at {parent})")
                    break
                except ValueError:
                    pass
            if parent.parent == parent:
                break
            parent = parent.parent
        if not subMode:
            b_io.ann.note("MODE: base (no initiated parent found)")

        claudeSrc = (motherDir / 'initiateSub' / 'CLAUDE.md') if subMode else (motherDir / 'CLAUDE.md')
        if not claudeSrc.exists():
            b_io.eh.problem_usageError(f"Source CLAUDE.md not found: {claudeSrc}")
            return failed(cmndOutcome)

        claudeDst = targetDir / 'CLAUDE.md'
        if claudeDst.is_symlink():
            # Legacy install: previously symlinked CLAUDE.md. Upgrade to safe-copy.
            claudeDst.unlink()
            shutil.copy2(claudeSrc, claudeDst)
            b_io.ann.note(f"UPGRADED (legacy symlink -> safe-copy): {claudeSrc} -> {claudeDst}")
        elif claudeDst.is_file():
            shutil.copy2(claudeSrc, claudeDst)
            b_io.ann.note(f"REFRESHED: {claudeSrc} -> {claudeDst}")
        else:
            shutil.copy2(claudeSrc, claudeDst)
            b_io.ann.note(f"COPIED (was not present): {claudeSrc} -> {claudeDst}")

        # Backfill missing invariant symlinks — base mode only; subs inherit
        # from parent. Handles projects initiated before AI-Outputs.org
        # existed in the templates tree. Optional: skipped if the templates
        # tree doesn't ship it (e.g. bxexamples, rana-notes as of this writing).
        if not subMode:
            for fname in ['AI-Outputs.org']:
                src = motherDir / fname
                dst = targetDir / fname
                if not src.exists() and not src.is_symlink():
                    b_io.ann.note(f"SKIP (no such file in templates): {src}")
                    continue
                if dst.exists() or dst.is_symlink():
                    b_io.ann.note(f"SKIP (exists): {dst}")
                else:
                    dst.symlink_to(src)
                    b_io.ann.note(f"SYMLINKED (backfilled): {dst} -> {src}")

        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults=f"refresh complete at {targetDir} (mode={'sub' if subMode else 'base'})",
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "cwdConfig_record" :comment "Record deduced cwdConfig for an already-initiated directory" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<cwdConfig_record>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class cwdConfig_record(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Deduce cwdConfig (=templates=, =activity=) from the
current directory's =AI-WORKFLOW.org= and =AI-Activity.org= symlink targets
and write it to =./.aiActivity.cs/fps/=.

Retrofits existing initiated directories that predate cwdConfig auto-persistence,
or repairs a cwdConfig that has been lost. For new installs, =initiate= and
=initiateSub= do this automatically on success.

Writes only when the deduced value differs from what is already in cwdConfig
(idempotent). Reports each deduction/write/skip on stderr.
        #+end_org """)

        targetDir = pathlib.Path.cwd()
        templatesBase, activity = _deduceCwdConfig(targetDir)

        if templatesBase is None and activity is None:
            b_io.eh.problem_usageError(
                f"cwdConfig_record: no AI-WORKFLOW.org or AI-Activity.org symlink "
                f"found at {targetDir}. Nothing to deduce. Run 'initiate' here first.")
            return failed(cmndOutcome)

        notes = _recordCwdConfig(templatesBase, activity)
        for note in notes:
            b_io.ann.note(note)

        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults=f"cwdConfig_record complete at {targetDir}",
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "listClaudesPath" :comment "Walk up to git repo root and list CLAUDE.md + AI-Activity.org at each level" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<listClaudesPath>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class listClaudesPath(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Walk upward from cwd to git repo root, listing every
directory that contains a =CLAUDE.md=. For each, prints the full path of
=CLAUDE.md= and the resolved target of the =AI-Activity.org= symlink (if
present). cwd is printed flush-left; each ancestor level adds one indent
step so the repo root appears most-indented. Stops at the git repo root
(determined via =git rev-parse --show-toplevel=); if cwd is not inside a
git repo, stops at the filesystem root.
        #+end_org """)

        import subprocess

        cwd = pathlib.Path.cwd()

        # Determine git repo root (stop boundary).
        repoRoot: typing.Optional[pathlib.Path] = None
        try:
            result = subprocess.run(
                ['git', 'rev-parse', '--show-toplevel'],
                capture_output=True, text=True, check=True,
            )
            repoRoot = pathlib.Path(result.stdout.strip())
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass  # not a git repo; walk to filesystem root

        # Collect directories from cwd upward (inclusive) stopping at repoRoot.
        dirs: typing.List[pathlib.Path] = []
        current = cwd
        while True:
            dirs.append(current)
            if repoRoot is not None and current == repoRoot:
                break
            if current.parent == current:
                break  # filesystem root
            current = current.parent

        # Print entries: dirs[0] = cwd (indent 0), dirs[1] = parent (indent 1), etc.
        # cwd is always printed, even when it has no CLAUDE.md.
        found = 0
        for depth, directory in enumerate(dirs):
            claudeMd = directory / 'CLAUDE.md'
            hasClaude = claudeMd.exists() or claudeMd.is_symlink()
            if not hasClaude:
                if depth == 0:
                    # cwd: always report, even when absent
                    b_io.ann.note(f"CLAUDE.md: None at {directory}")
                    b_io.ann.note(f"AI-Activity.org -> None")
                continue
            found += 1
            indent = '  ' * depth
            activityOrg = directory / 'AI-Activity.org'
            if activityOrg.is_symlink():
                rawTarget = pathlib.Path(activityOrg.readlink())
                if not rawTarget.is_absolute():
                    rawTarget = (activityOrg.parent / rawTarget).resolve()
                activityLine = f"{indent}AI-Activity.org -> {rawTarget}"
            elif activityOrg.is_file():
                activityLine = f"{indent}AI-Activity.org (file, no symlink target)"
            else:
                activityLine = f"{indent}AI-Activity.org -> None"
            b_io.ann.note(f"{indent}CLAUDE.md: {claudeMd}")
            b_io.ann.note(activityLine)

        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults=f"listClaudesPath complete: {found} CLAUDE.md(s) found",
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "deClaudify" :comment "Remove AI collaboration files installed by initiate" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<deClaudify>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class deClaudify(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Remove AI collaboration files installed by initiate.
Deletes symlinks: CLAUDE.md, AI-WORKFLOW.org, AI-Outputs.org, AI-Activity.org,
.claude/settings.json, .claude/commands (plus legacy AI-AGENTS.org
from pre-merge projects, if present).
Deletes copied files: AI-DevStatus.org, AI-WorkPlan.org.
Removes .claude/ directory if it becomes empty.
        #+end_org """)

        targetDir = pathlib.Path.cwd()

        # Symlinked constant files and activity file (includes CLAUDE.md.dormant
        # in case deClaudify runs while a session is suspended).
        # AI-AGENTS.org is retained here as a legacy cleanup — pre-merge
        # projects have an AI-AGENTS.org symlink that deClaudify should
        # still remove even though initiate no longer installs it.
        # AI-AGENTS.org is retained here as a legacy cleanup — pre-merge
        # projects have an AI-AGENTS.org symlink that deClaudify should
        # still remove even though initiate no longer installs it.
        symlinkFiles = ['AI-AGENTS.org', 'AI-WORKFLOW.org', 'AI-Outputs.org']
        for fname in symlinkFiles:
            dst = targetDir / fname
            if dst.is_symlink():
                dst.unlink()
                b_io.ann.note(f"REMOVED symlink: {dst}")
            elif dst.exists():
                b_io.ann.note(f"SKIP (not a symlink, leaving intact): {dst}")
            else:
                b_io.ann.note(f"SKIP (not present): {dst}")

        # CLAUDE.md is now safe-copied by default (was previously symlinked).
        # AI-Activity.org may be either a symlink (default install) or a
        # regular file (--noLink=AI-Activity.org install). Remove either form
        # for both. AI-DevStatus.org / AI-WorkPlan.org are always safe-copies.
        # Includes .dormant copies in case deClaudify runs while a session is suspended.
        removableFiles = ['CLAUDE.md', 'CLAUDE.md.dormant',
                          'AI-Activity.org', 'AI-Activity.org.dormant',
                          'AI-DevStatus.org', 'AI-WorkPlan.org',
                          'AI-DevStatus.org.dormant', 'AI-WorkPlan.org.dormant']
        for fname in removableFiles:
            dst = targetDir / fname
            if dst.is_symlink():
                dst.unlink()
                b_io.ann.note(f"REMOVED symlink: {dst}")
            elif dst.is_file():
                dst.unlink()
                b_io.ann.note(f"REMOVED file: {dst}")
            else:
                b_io.ann.note(f"SKIP (not present): {dst}")

        # .claude/ symlinked entries
        claudeDstDir = targetDir / '.claude'
        for claudeEntry in ['settings.json', 'commands', 'skills']:
            claudeDst = claudeDstDir / claudeEntry
            if claudeDst.is_symlink():
                claudeDst.unlink()
                b_io.ann.note(f"REMOVED symlink: {claudeDst}")
            elif claudeDst.exists():
                b_io.ann.note(f"SKIP (not a symlink, leaving intact): {claudeDst}")
            else:
                b_io.ann.note(f"SKIP (not present): {claudeDst}")

        # Remove .claude/ dir if now empty
        if claudeDstDir.is_dir() and not any(claudeDstDir.iterdir()):
            claudeDstDir.rmdir()
            b_io.ann.note(f"REMOVED empty directory: {claudeDstDir}")

        return cmndOutcome.set(
            opError=b.op.OpError.Success,
            opResults=f"deClaudify complete at {targetDir}",
        )


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Main" :anchor ""  :extraInfo "Framework DBlock"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Main_: |]]  Framework DBlock  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/main :csInfo "csInfo" :noCmndEntry "examples" :extraParamsHook "g_extraParams" :importedCmndsModules "g_importedCmndsModules"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] =g_csMain= (csInfo, _examples_, g_extraParams, g_importedCmndsModules)
#+end_org """

if __name__ == '__main__':
    cs.main.g_csMain(
        csInfo=csInfo,
        noCmndEntry=examples,
        extraParamsHook=g_extraParams,
        ignoreUnknownParams=False,
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
