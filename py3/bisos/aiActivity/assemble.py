# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =pyLibPure= that assembles a templates base from its two input trees
(=aiTemplates-workFlow=, =aiTemplates-DE=) by a deep merge of relative links.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "pyLibPure"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=pyLibPure
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "pyLibPure") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: pyLibPure
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
** This File: /bxRepos/bisos-pip/aiActivity/py3/bisos/aiActivity/assemble.py
** File True Name: /bisos/git/auth/bxRepos/bisos-pip/aiActivity/py3/bisos/aiActivity/assemble.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]]
The logic behind =aiActivityAssemble.cs= (Stage 18 of the bisos.aiActivity WorkPlan), free of the CS
framework. Pure functions over =pathlib= paths; refusals are raised as =AssembleRefusal=.

A templates base =<base>/= contains two inputs with fixed names, =aiTemplates-workFlow= and
=aiTemplates-DE= (real directories or symlinks to clones anywhere), of the same structure as the base.
Assembly is a *deep merge*:
- every directory an input has is a real directory in the base;
- every file an input has appears at the same relative path in the base as a *relative* symlink
  through the input's name (=mother/CLAUDE.md -> ../aiTemplates-workFlow/mother/CLAUDE.md=), so the
  base keeps working wherever it and its inputs are;
- every symlink an input has is reproduced in the base as the same symlink (a relative
  =bisos-pip/_skills -> ../mother/_skills= then resolves against the base, i.e. the merged skills).
An input's own root files and dot-directories (its =LICENSE=, =README.org=, self-hosted =AI-*.org=,
=CLAUDE.md=, =.git/=, =.claude/=) are not template content and are ignored: only its top-level real
directories are merged. A path provided by both inputs is an error (no layering). The assembler manages only what it made,
recorded in a manifest, =<base>/.aiActivityAssembled=; anything else in the base (its own
=README.org=, =LICENSE=, self-hosted =AI-*.org=) is left alone, and it refuses to replace a real file.
** Status: inDev
#+end_org """

import dataclasses
import datetime
import json
import os
import pathlib
import typing

inputNames = ('aiTemplates-workFlow', 'aiTemplates-DE')
manifestName = '.aiActivityAssembled'
skipNames = {'.git', '__pycache__'}


class AssembleRefusal(Exception):
    """An assembly that must not start; the message says why. Nothing has been written."""


@dataclasses.dataclass
class Plan:
    """What an assembly of =base= would do, by base-relative path."""
    base: pathlib.Path
    desired: typing.Dict[str, str]          # path -> link target, as it should be
    create: typing.List[str]
    update: typing.List[str]                # a link of ours, pointing elsewhere
    same: typing.List[str]
    remove: typing.List[str]                # a link of ours no longer provided
    conflicts: typing.List[str]             # something not ours is in the way

    def isBehind(self) -> bool:
        return bool(self.create or self.update or self.remove)


def _inputLeaves(root: pathlib.Path) -> typing.Dict[str, typing.Tuple[str, str]]:
    """Relative path -> ('file', '') or ('link', target) for the files and symlinks of one input.
    Directories are walked, not listed; a symlink to a directory is a leaf (reproduced as such)."""
    leaves: typing.Dict[str, typing.Tuple[str, str]] = {}
    for dirPath, dirNames, fileNames in os.walk(root, followlinks=False):
        relDir = pathlib.Path(dirPath).relative_to(root)
        if str(relDir) == '.':
            # The input's root belongs to its own repository (LICENSE, README.org, CLAUDE.md, AI-*.org,
            # .git/, .claude/, .aiActivity.cs/): only its real, non-dot top-level directories are template
            # content (mother/, the activities, _nonTemplate_/).
            dirNames[:] = [name for name in dirNames
                           if not name.startswith('.') and name not in skipNames
                           and not (pathlib.Path(dirPath) / name).is_symlink()]
            continue
        for name in list(dirNames):
            path = pathlib.Path(dirPath) / name
            if name in skipNames:
                dirNames.remove(name)
            elif path.is_symlink():
                leaves[str(relDir / name)] = ('link', os.readlink(path))
                dirNames.remove(name)
        for name in fileNames:
            if name in skipNames:
                continue
            path = pathlib.Path(dirPath) / name
            rel = str(relDir / name)
            leaves[rel] = ('link', os.readlink(path)) if path.is_symlink() else ('file', '')
    return leaves


def inputsResolve(base: pathlib.Path) -> typing.List[typing.Tuple[str, pathlib.Path]]:
    """The two inputs of =base= by their fixed names, or AssembleRefusal."""
    if not base.is_dir():
        raise AssembleRefusal(f"base is not a directory: {base}")
    found = []
    for name in inputNames:
        path = base / name
        if not path.is_dir():
            state = "a dangling symlink" if path.is_symlink() else "missing"
            raise AssembleRefusal(f"input {name} is {state} in {base}")
        found.append((name, path))
    return found


def inputLink(base: pathlib.Path, name: str, target: pathlib.Path) -> str:
    """Create =<base>/<name>= as a symlink to =target= (an input clone). Returns what was done.
    Refuses when =<base>/<name>= exists and is not already that link."""
    if name not in inputNames:
        raise AssembleRefusal(f"not an input name: {name} (expected one of {', '.join(inputNames)})")
    target = pathlib.Path(target).expanduser()
    # A relative target is kept relative and, like any symlink target, read against the base.
    if not (target if target.is_absolute() else base / target).is_dir():
        raise AssembleRefusal(f"input target is not a directory: {target} (relative targets are read "
                              f"against the base, {base})")
    link = base / name
    if link.is_symlink():
        if pathlib.Path(os.readlink(link)) == target:
            return f"OK (input link already right): {name} -> {target}"
        raise AssembleRefusal(f"{link} already points to {os.readlink(link)}, not {target}")
    if link.exists():
        raise AssembleRefusal(f"{link} exists and is not a symlink (a real input directory?)")
    link.symlink_to(target)
    return f"LINKED input: {name} -> {target}"


def manifestRead(base: pathlib.Path) -> typing.Dict[str, str]:
    """Path -> target of the links the assembler made, as recorded at its last run."""
    path = base / manifestName
    if not path.is_file():
        return {}
    links = json.loads(path.read_text()).get('links', {})
    return dict(links) if isinstance(links, dict) else {}


def planBuild(base: pathlib.Path) -> Plan:
    """Compare what the inputs provide with what the base holds."""
    inputs = inputsResolve(base)
    leavesByInput = {name: _inputLeaves(path) for name, path in inputs}

    # A path in both inputs, or a leaf of one that is a directory of the other: no layering.
    owners: typing.Dict[str, str] = {}
    clashes: typing.List[str] = []
    for name, leaves in leavesByInput.items():
        for rel in leaves:
            if rel in owners:
                clashes.append(f"{rel} (in both {owners[rel]} and {name})")
            owners[rel] = name
    allLeaves = set(owners)
    for rel in allLeaves:
        for parent in pathlib.Path(rel).parents:
            if str(parent) != '.' and str(parent) in allLeaves:
                clashes.append(f"{rel} (under {parent}, a file or link of {owners[str(parent)]})")
    if clashes:
        raise AssembleRefusal("a path provided by both inputs:\n  " + "\n  ".join(sorted(clashes)))

    desired: typing.Dict[str, str] = {}
    for name, leaves in leavesByInput.items():
        for rel, (kind, target) in leaves.items():
            if kind == 'link':
                desired[rel] = target
            else:
                linkDir = (base / rel).parent
                desired[rel] = os.path.relpath(base / name / rel, linkDir)

    ours = manifestRead(base)
    create, update, same, conflicts = [], [], [], []
    remove = []
    for rel in sorted(set(ours) - set(desired)):
        path = base / rel
        if not path.is_symlink():
            continue
        if os.readlink(path) == ours[rel]:
            remove.append(rel)
        else:
            conflicts.append(f"{rel} (no longer provided, but changed since the assembler made it)")
    removeSet = set(remove)

    def _onlyOursBeingRemoved(directory: pathlib.Path) -> bool:
        # A real directory the assembler made for an input's directory, which that input has since turned
        # into a symlink (e.g. <activity>/_skills/ -> ../mother/_skills): everything in it is a link of
        # ours being removed, so planApply's removals empty it, prune it, and the new link takes its place.
        entries = [str((pathlib.Path(dirPath) / name).relative_to(base))
                   for dirPath, dirNames, fileNames in os.walk(directory, followlinks=False)
                   for name in fileNames + [d for d in dirNames if (pathlib.Path(dirPath) / d).is_symlink()]]
        return bool(entries) and all(entry in removeSet for entry in entries)

    for rel, target in sorted(desired.items()):
        path = base / rel
        if path.is_symlink():
            current = os.readlink(path)
            if current == target:
                same.append(rel)
            elif ours.get(rel) == current:
                update.append(rel)
            elif rel in ours:
                conflicts.append(f"{rel} (changed since the assembler made it: -> {current})")
            else:
                conflicts.append(f"{rel} (a symlink not made by the assembler: -> {current})")
        elif path.is_dir() and _onlyOursBeingRemoved(path):
            create.append(rel)
        elif path.exists():
            conflicts.append(f"{rel} (a real {'directory' if path.is_dir() else 'file'})")
        else:
            blocking = [p for p in pathlib.Path(rel).parents
                        if str(p) != '.' and ((base / p).is_symlink() or (base / p).is_file())]
            if blocking:
                conflicts.append(f"{rel} (its parent {blocking[-1]} is a file or a symlink in the base)")
            else:
                create.append(rel)
    return Plan(base, desired, create, update, same, remove, conflicts)


def danglingLinks(plan: Plan) -> typing.List[str]:
    """Links of the assembly whose target does not resolve (e.g. a renamed file in an input)."""
    return sorted(rel for rel in plan.same + plan.update
                  if (plan.base / rel).is_symlink() and not (plan.base / rel).exists())


def planApply(plan: Plan) -> typing.List[str]:
    """Carry out the plan; one line per action. Refuses, before writing, if there are conflicts."""
    if plan.conflicts:
        raise AssembleRefusal("in the way, not made by the assembler:\n  " + "\n  ".join(plan.conflicts))
    actions: typing.List[str] = []
    for rel in plan.remove:
        (plan.base / rel).unlink()
        actions.append(f"REMOVED (no longer provided): {rel}")
        for parent in pathlib.Path(rel).parents:
            directory = plan.base / parent
            if str(parent) == '.' or not directory.is_dir() or any(directory.iterdir()):
                break
            directory.rmdir()
            actions.append(f"REMOVED (empty directory): {parent}")
    for rel in plan.update:
        path = plan.base / rel
        path.unlink()
        path.symlink_to(plan.desired[rel])
        actions.append(f"UPDATED: {rel} -> {plan.desired[rel]}")
    for rel in plan.create:
        path = plan.base / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.symlink_to(plan.desired[rel])
        actions.append(f"LINKED: {rel} -> {plan.desired[rel]}")
    manifest = {
        'note': ("Made by aiActivityAssemble.cs: the links listed here are generated from "
                 + " and ".join(inputNames) + ". Edit the inputs, then assemble again."),
        'assembledAt': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
        'inputs': {name: os.readlink(plan.base / name) if (plan.base / name).is_symlink() else 'real directory'
                   for name in inputNames},
        'links': {rel: plan.desired[rel] for rel in sorted(plan.desired)},
    }
    (plan.base / manifestName).write_text(json.dumps(manifest, indent=2) + '\n')
    actions.append(f"WROTE: {manifestName}")
    return actions


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
