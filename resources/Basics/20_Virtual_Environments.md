# Virtual Environments & `pip`

## Definition
A **virtual environment** is a per-project directory containing a Python interpreter (usually a symlink) and an isolated `site-packages`. Packages installed inside it do not affect other projects or the system interpreter.

## Why
- **Isolation** — project A pins `requests==2.28`, project B pins `requests==2.31`. Both run.
- **Reproducibility** — a pinned `requirements.txt` reconstructs the same set of packages elsewhere.
- **System hygiene** — no writes to the system interpreter. Modern OSes (macOS, Debian/Ubuntu) block `pip install` on the system Python via PEP 668 for this reason.

## Creating
```bash
python -m venv .venv            # creates .venv/ using the current interpreter
python3.12 -m venv .venv        # be explicit about the version
```
Convention: name it `.venv`, add it to `.gitignore`. The venv is per-machine and tied to the exact Python it was created with.

## Activation
Activation prepends `.venv/bin` to `PATH` and sets `VIRTUAL_ENV`. That's all — `python` and `pip` now resolve inside the venv.
```bash
# bash / zsh
source .venv/bin/activate

# tcsh (this project)
source .venv/bin/activate.csh

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# any shell
deactivate                      # restores the previous PATH
```
Activation is a shell convenience. You can skip it and call `.venv/bin/python` directly.

## Installing packages
```bash
pip install requests
pip install "requests>=2.28,<3"     # version range
pip install requests==2.31.0        # exact pin
pip install ~=1.8.0                 # compatible release: >=1.8.0, <1.9.0
pip install -U requests             # upgrade to latest
pip uninstall requests
pip list                            # what's installed
pip show requests                   # metadata for one package
```
Version specifiers follow PEP 440. `~=X.Y` allows patch-level updates; `~=X.Y.Z` allows only bug-fix updates.

## Freezing and restoring
```bash
pip freeze > requirements.txt       # snapshot of every installed version
pip install -r requirements.txt     # reinstall the exact set
```
Commit `requirements.txt`. Do not commit `.venv/` — it is machine- and path-specific.

## Editable installs
For a local package under development:
```bash
pip install -e .                    # install the project in editable mode
```
Edits to the source take effect immediately without reinstalling. Requires a `pyproject.toml` or `setup.py`.

## PEP 668 — externally-managed environments
Recent macOS Homebrew and Debian/Ubuntu ship a marker file that makes `pip install` refuse to touch the system Python. The fix is to use a venv per project, or `pipx` for standalone tools.

## `pipx`
Installs each CLI tool into its own private venv but exposes the entry-point on `PATH`. For end-user tools (e.g. `black`, `httpie`), not for project dependencies.
```bash
pipx install black
```

## `uv`
A Rust rewrite of pip + venv, an order of magnitude faster. Drop-in for most workflows:
```bash
uv venv                             # create .venv
uv pip install requests
uv pip freeze > requirements.txt
```

## Lockfiles vs `requirements.txt`
`pip freeze` captures every installed package — direct and transitive — in one flat list. That reproduces state but hides intent. Tools that separate the two:
- **pip-tools** — `pip-compile requirements.in` produces a locked `requirements.txt`.
- **Poetry** — `pyproject.toml` for direct deps, `poetry.lock` for the full graph.
- **uv** — `uv.lock` with the same split.

## Verifying the interpreter
```bash
which python                        # should end in .venv/bin/python
python -c "import sys; print(sys.executable)"
python -c "import site; print(site.getsitepackages())"
```
`sys.executable` is the authoritative answer — `which` reflects `PATH`, which activation manipulates.

## Full lifecycle
```bash
python -m venv .venv
source .venv/bin/activate.csh       # tcsh
pip install --upgrade pip
pip install requests pandas
pip freeze > requirements.txt
echo ".venv/" >> .gitignore
```

## Gotchas
- **Activation is per shell session** — a new terminal is not activated. Reactivate, or invoke `.venv/bin/python` directly.
- **Don't commit `.venv/`** — it embeds absolute paths and platform-specific binaries.
- **`pip freeze` is noisy** — it includes transitive deps. Prefer `pip-compile`, Poetry, or `uv` to separate direct from transitive.
- **Wrong interpreter** — `python -m venv .venv` uses whichever `python` is first on `PATH`. Pin the version explicitly (`python3.12 -m venv .venv`).
- **PEP 668** — `pip install` on the system interpreter is now blocked on many OSes. Use a venv, `pipx`, or `--break-system-packages` (don't).
- **tcsh** — this project's shell. Activate with `activate.csh`, not `activate`.
