# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =pyLibPure= that lists the running Claude Code sessions of this host, from Claude
Code's own registry (=~/.claude/sessions/<pid>.json=).
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
** This File: /bxRepos/bisos-pip/aiActivity/py3/bisos/aiActivity/claudeSessions.py
** File True Name: /bisos/git/auth/bxRepos/bisos-pip/aiActivity/py3/bisos/aiActivity/claudeSessions.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]]
The logic behind =claudeSessions.cs= (WorkPlan 20.3.1), free of the CS framework.

Claude Code writes one =<pid>.json= per running Claude process into =~/.claude/sessions/= and removes
it when the process ends cleanly. In the VS Code extension each open conversation is a process: a new
conversation or tab is a new file, =/clear= rewrites =sessionId= in place, a resume from history is a
new process. The registry is undocumented (seen in Claude Code 2.1.311), so it is read here only.

A file counts only if its process is alive: =/proc/<pid>= exists and field 22 of its =stat= (start
time) equals the file's =procStart=, which rejects a file left by a crash whose pid was reused. The
instance is told by the process's executable: under =~/.vscode/extensions/= is the local (desktop) VS
Code, under =~/.vscode-server/extensions/= the remote VS Code server, anything else (e.g. =claude= in
a terminal) is =other=.
** Status: inDev
#+end_org """

import dataclasses
import json
import os
import pathlib
import subprocess
import typing
import urllib.parse

registryDir = pathlib.Path.home() / '.claude' / 'sessions'
localExtensionsDir = pathlib.Path.home() / '.vscode' / 'extensions'
remoteExtensionsDir = pathlib.Path.home() / '.vscode-server' / 'extensions'

modes = ('local', 'remote', 'all')


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
        """The tab-separated form printed by list."""
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
# goes on the clipboard instead (clipboardSet). Both parameters are optional.
# Read from the extension's code (2.1.311), not a documented API: build it here only.
openUriBase = 'vscode://anthropic.claude-code/open'


def openUri(prompt: typing.Optional[str] = None, sessionId: typing.Optional[str] = None) -> str:
    """The /open URI for prompt (none: only open), into sessionId, or a new conversation when None."""
    query = {'session': sessionId} if sessionId else {}
    if prompt is not None:
        query['prompt'] = prompt
    return f"{openUriBase}?{urllib.parse.urlencode(query, quote_via=urllib.parse.quote)}"


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

    After delay (the extension's reveal is not immediate), activate the desktop VS Code window, wait
    until it has the focus, and press Ctrl+V. X sees the window only: the extension's reveal puts the
    focus in the Claude panel's input box (tested by Mohsen, 2026-10-28, focus first in a source file).
    With several VS Code windows the first one found is used.
    """
    return ['xdotool', 'sleep', str(delay),
            'search', '--onlyvisible', '--class', 'code',
            'windowactivate', '--sync', 'key', '--clearmodifiers', 'ctrl+v']


def pasteSend(delay: float = 0.5) -> subprocess.CompletedProcess:
    """Paste the clipboard into the session that /open just brought to the front."""
    return subprocess.run(pasteCommand(delay), capture_output=True, text=True, check=False)


def openUriCommand(uri: str) -> typing.List[str]:
    """The command openUriSend runs."""
    return ['code', '--open-url', uri]


def openUriSend(uri: str) -> subprocess.CompletedProcess:
    """Hand uri to the local (desktop) VS Code with code --open-url.

    VSCODE_IPC_HOOK_CLI is dropped: when set (a VS Code terminal), the desktop launcher defers to a
    remote-cli on PATH, and the remote CLI does not support --open-url. DISPLAY must be that of the
    desktop VS Code: without it nothing reaches the running window, and code still exits 0.
    """
    env = {k: v for k, v in os.environ.items() if k != 'VSCODE_IPC_HOOK_CLI'}
    return subprocess.run(openUriCommand(uri), env=env, capture_output=True, text=True, check=False)
