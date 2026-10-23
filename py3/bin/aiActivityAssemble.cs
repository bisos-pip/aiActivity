#!/bin/env python
# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CSXU= that assembles a templates base from its two input trees.
#+end_org """

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/bxRepos/bisos-pip/aiActivity/README.org][aiActivity README]]

A template-maintainer tool (Stage 18 of the bisos.aiActivity WorkPlan). A templates base, the
directory =aiActivity.cs= installs from, contains two inputs with fixed names, =aiTemplates-workFlow=
(BISOS-AI-Workflow: the =/bx-*= commands, workflow skills, =mother/= workflow files, generic
activities) and =aiTemplates-DE= (an ecosystem's skills and activities). Each is a real directory or a
symlink to a clone anywhere. =assemblyUpdate= makes the base the aggregate of the two: real
directories, relative links to the inputs' files, and the inputs' own symlinks reproduced. A path in
both inputs is refused. =assemblyDiff= shows what would change, =assemblyCheck= says IN SYNC or BEHIND
and lists dangling links. The base's own files are never touched; nothing is committed.
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
** This File: /bxRepos/bisos-pip/aiActivity/py3/bin/aiActivityAssemble.cs
** File True Name: /bisos/git/auth/bxRepos/bisos-pip/aiActivity/py3/bin/aiActivityAssemble.cs
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inDev"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
if 'csInfo' not in globals(): import typing ; csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['aiActivityAssemble'], }
csInfo['version'] = '202610200000'
csInfo['status']  = 'inDev'
csInfo['panel'] = 'aiActivityAssemble-Panel.org'
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

import pathlib
import typing

from bisos.aiActivity import assemble as assembleLib

""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~csuList emacs-list Specifications~  [[elisp:(blee:org:code-block/above-run)][ /Eval Below/ ]] [[elisp:(org-cycle)][| ]]
#+BEGIN_SRC emacs-lisp
(setq  b:py:cs:csuList
  (list
 ))
#+END_SRC
#+RESULTS:
: nil
#+end_org """

####+BEGIN: b:py3:cs:framework/csuListProc :pyImports t :csuImports t :csuParams t :csxuParams nil
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] ~Process CSU List~ with /0/ in csuList pyImports=t csuImports=t csuParams=t
#+end_org """

csuList = []

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
        parName='base',
        parDescription=("The templates base to assemble, holding the inputs aiTemplates-workFlow and "
                        "aiTemplates-DE (e.g. /bisos/apps/defaults/ai-templates)."),
        parDataType=None,
        parDefault=None,
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--base',
    )
    csParams.parDictAdd(
        parName='workFlow',
        parDescription="Optional: a clone to link as <base>/aiTemplates-workFlow (if not there yet).",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--workFlow',
    )
    csParams.parDictAdd(
        parName='de',
        parDescription="Optional: a clone to link as <base>/aiTemplates-DE (if not there yet).",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--de',
    )


def _planFor(
        base: typing.Optional[str],
        workFlow: typing.Optional[str] = None,
        de: typing.Optional[str] = None,
        linkInputs: bool = False,
) -> typing.Tuple[assembleLib.Plan, typing.List[str]]:
    """The plan, and the input-link actions taken; or assembleLib.AssembleRefusal (nothing written)."""
    if not base:
        raise assembleLib.AssembleRefusal("--base is required: the templates base to assemble")
    basePath = pathlib.Path(base).expanduser()
    actions: typing.List[str] = []
    for name, target in (('aiTemplates-workFlow', workFlow), ('aiTemplates-DE', de)):
        if target:
            if not linkInputs:
                if not (basePath / name).exists():
                    raise assembleLib.AssembleRefusal(
                        f"{name} is missing in {basePath}; assemblyUpdate with --{'workFlow' if name.endswith('workFlow') else 'de'}"
                        f" creates the link")
                continue
            actions.append(assembleLib.inputLink(basePath, name, pathlib.Path(target)))
    return assembleLib.planBuild(basePath), actions


def _planNote(plan: assembleLib.Plan) -> None:
    b_io.ann.note(f"BASE: {plan.base}")
    for rel in plan.create:
        b_io.ann.note(f"TO LINK: {rel} -> {plan.desired[rel]}")
    for rel in plan.update:
        b_io.ann.note(f"TO UPDATE: {rel} -> {plan.desired[rel]}")
    for rel in plan.remove:
        b_io.ann.note(f"TO REMOVE (no longer provided): {rel}")
    for item in plan.conflicts:
        b_io.ann.note(f"CONFLICT (not ours, in the way): {item}")
    b_io.ann.note(f"SAME: {len(plan.same)}")


def _planCounts(plan: assembleLib.Plan) -> str:
    return (f"link={len(plan.create)} update={len(plan.update)} remove={len(plan.remove)} "
            f"conflict={len(plan.conflicts)} same={len(plan.same)}")


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

        # Concrete values where the well-known trees exist on this host (WorkPlan 18.11), else placeholders.
        knownBase = pathlib.Path('/bisos/git/bxRepos/bxexamples/aiActivityTemplates')
        knownWorkFlow = pathlib.Path('/bisos/git/bxRepos/bxexamples/aiTemplates-workFlow')
        base = str(knownBase) if knownBase.is_dir() else '<templatesBase>'
        workFlow = str(knownWorkFlow) if knownWorkFlow.is_dir() else '<workFlowClone>'

        cs.examples.menuChapter('=assemblyDiff= -- what an assembly would link, update or remove (read-only)')
        cmnd('assemblyDiff', pars=od([('base', base)]),
             comment="# Lists conflicts too: things in the way that the assembler did not make")

        cs.examples.menuChapter('=assemblyCheck= -- IN SYNC or BEHIND, with counts, and dangling links')
        cmnd('assemblyCheck', pars=od([('base', base)]),
             comment="# Read-only")

        cs.examples.menuChapter('=assemblyUpdate= -- make the base the aggregate of its two inputs')
        cmnd('assemblyUpdate', pars=od([('base', base)]),
             comment="# Links, updates and removes only what the assembler manages")
        cmnd('assemblyUpdate', pars=od([('base', base), ('workFlow', workFlow)]),
             comment="# Also create the input link aiTemplates-workFlow -> the clone, if missing")

        literal("# A path in both inputs is refused. The base's own files are never touched.")

        return(cmndOutcome)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "assemblyDiff" :comment "Report what an assembly would change (read-only)" :extent "verify" :ro "cli" :parsMand "base" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<assemblyDiff>>  *Report what an assembly would change (read-only)*  =verify= parsMand=base ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class assemblyDiff(cs.Cmnd):
    cmndParamsMandatory = [ 'base', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             base: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:
        """Report what an assembly would change (read-only)"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'base': base, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        base = csParam.mappedValue('base', base)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Compare what =aiTemplates-workFlow= and =aiTemplates-DE= provide with
what the base holds, and list what =assemblyUpdate= would link, update and remove, and any conflict
(something in the way that the assembler did not make). Writes nothing.
        #+end_org """)

        try:
            plan, _ = _planFor(base)
        except assembleLib.AssembleRefusal as refusal:
            b_io.eh.problem_usageError(f"REFUSED: {refusal}")
            return failed(cmndOutcome)
        _planNote(plan)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=_planCounts(plan))


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "assemblyCheck" :comment "Say IN SYNC or BEHIND, and list dangling links" :extent "verify" :ro "cli" :parsMand "base" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<assemblyCheck>>  *Say IN SYNC or BEHIND, and list dangling links*  =verify= parsMand=base ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class assemblyCheck(cs.Cmnd):
    cmndParamsMandatory = [ 'base', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             base: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:
        """Say IN SYNC or BEHIND, and list dangling links"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'base': base, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        base = csParam.mappedValue('base', base)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  One line: =IN SYNC=, or =BEHIND= with counts; conflicts and dangling
links (e.g. after a file was renamed in an input) are listed. Writes nothing. The PyCS main exits 0
whichever it says: read the line.
        #+end_org """)

        try:
            plan, _ = _planFor(base)
        except assembleLib.AssembleRefusal as refusal:
            b_io.eh.problem_usageError(f"REFUSED: {refusal}")
            return failed(cmndOutcome)
        for item in plan.conflicts:
            b_io.ann.note(f"CONFLICT (not ours, in the way): {item}")
        dangling = assembleLib.danglingLinks(plan)
        for rel in dangling:
            b_io.ann.note(f"DANGLING: {rel} -> {plan.desired.get(rel, '?')}")
        behind = plan.isBehind() or plan.conflicts or dangling
        verdict = "BEHIND" if behind else "IN SYNC"
        return cmndOutcome.set(opError=b.op.OpError.Success,
                               opResults=f"{verdict}: {_planCounts(plan)} dangling={len(dangling)}")


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "assemblyUpdate" :comment "Make the base the aggregate of its two inputs" :extent "verify" :ro "cli" :parsMand "base" :parsOpt "workFlow de" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<assemblyUpdate>>  *Make the base the aggregate of its two inputs*  =verify= parsMand=base parsOpt=workFlow de ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class assemblyUpdate(cs.Cmnd):
    cmndParamsMandatory = [ 'base', ]
    cmndParamsOptional = [ 'workFlow', 'de', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             base: typing.Optional[str]=None,  # Cs Mandatory Param
             workFlow: typing.Optional[str]=None,  # Cs Optional Param
             de: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:
        """Make the base the aggregate of its two inputs"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'base': base, 'workFlow': workFlow, 'de': de, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        base = csParam.mappedValue('base', base)
        workFlow = csParam.mappedValue('workFlow', workFlow)
        de = csParam.mappedValue('de', de)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Deep-merge =aiTemplates-workFlow= and =aiTemplates-DE= into the base:
real directories, relative links to the inputs' files, the inputs' own symlinks reproduced, and a
manifest (=.aiActivityAssembled=) of what was made. Links it made that are no longer provided are
removed. With =--workFlow= / =--de=, first creates the input link to that clone if it is missing.
Refuses, writing nothing, when an input is missing, when a path is in both inputs, or when something
not made by the assembler is in the way (a real file, or someone else's link). Never commits.
        #+end_org """)

        try:
            plan, actions = _planFor(base, workFlow, de, linkInputs=True)
            actions += assembleLib.planApply(plan)
        except assembleLib.AssembleRefusal as refusal:
            b_io.eh.problem_usageError(f"REFUSED: {refusal}")
            return failed(cmndOutcome)
        for action in actions:
            b_io.ann.note(action)
        return cmndOutcome.set(opError=b.op.OpError.Success,
                               opResults=f"assembled {plan.base}: {_planCounts(plan)}")


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
