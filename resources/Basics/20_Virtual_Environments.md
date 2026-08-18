# Virtual Environments & `pip`

## What is a virtual environment?
A **virtual environment** (venv) is a private, per-project Python setup. Packages you install for one project stay in that project's folder and don't affect anything else. Every real Python project should use one.

## Why bother?
- **Isolation** — Project A needs `requests 2.28`, Project B needs `requests 2.31`. Both work.
- **Reproducibility** — pin exact versions in `requirements.txt`; anyone can recreate the environment.
- **System hygiene** — no `sudo pip install` polluting the system interpreter (or breaking OS tools).

## Creating a venv (stdlib — `venv`)
```bash
python -m venv .venv        # creates a .venv/ directory in the project
```
Convention: name it `.venv` and add it to `.gitignore`. It's per-machine, per-Python-version.

## Activating and deactivating
Activation just prepends the venv's `bin/` to your `PATH` so `python` and `pip` point inside the venv.
```bash
# macOS / Linux (bash/zsh)
source .venv/bin/activate

# macOS / Linux (tcsh — the shell in this project)
source .venv/bin/activate.csh

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Deactivate (any shell)
deactivate
```
When activated, your prompt is usually prefixed with `(.venv)`.

## Installing packages — `pip`
```bash
pip install requests                    # latest version
pip install "requests>=2.28,<3"         # version range
pip install requests==2.31.0            # exact pin
pip install -U requests                 # upgrade to latest
pip uninstall requests                  # remove
pip list                                # list installed packages
pip show requests                       # details on one package
```

## Freezing dependencies
Capture the exact versions installed:
```bash
pip freeze > requirements.txt
```
Recreate on another machine (after creating and activating a fresh venv):
```bash
pip install -r requirements.txt
```
Commit `requirements.txt` to git; do **not** commit the venv itself.

## `requirements.txt` in the wild
```
requests==2.31.0
pandas>=2.0,<3
mypy~=1.8.0          # ~=X.Y.Z → same minor (1.8.*), latest patch
```

## Alternative tools you may see
- **`pip-tools`** — `pip-compile` produces a locked `requirements.txt` from a human-edited `requirements.in`.
- **Poetry** — full project + dependency manager (`pyproject.toml`, lockfile).
- **`uv`** — very fast Rust-based installer & venv manager (superset of `pip` + `venv`).
- **`conda`** — separate ecosystem, popular in data science; handles non-Python binaries too.

For learning, plain `venv + pip + requirements.txt` is fine and universally understood.

## Checking what interpreter you're using
```bash
which python                # macOS/Linux
where python                # Windows
python -c "import sys; print(sys.executable)"
```
Should point inside `.venv/bin/` (or `.venv\Scripts\`) when the venv is active.

## Common patterns
Full lifecycle for a new project:
```bash
python -m venv .venv
source .venv/bin/activate           # or activate.csh on tcsh
pip install --upgrade pip
pip install requests pandas
pip freeze > requirements.txt
echo ".venv/" >> .gitignore
```

## Gotchas
- **Activation is per-shell-session** — open a new terminal? Reactivate. Or point at the venv's python directly: `.venv/bin/python script.py`.
- **`pip install` outside a venv installs globally.** Some OSes (recent macOS, Debian) now refuse; use `--user` or, better, a venv.
- **Don't commit `.venv/`** — it's platform- and path-specific. Commit `requirements.txt` instead.
- **`pip freeze` captures everything, including transitive deps** — reproducible but noisy. Tools like `pip-compile` separate direct from transitive.
- **Multiple Python versions** — `python -m venv` uses whichever `python` you invoke. Be explicit: `python3.12 -m venv .venv`.
- **tcsh users** — activate with `.venv/bin/activate.csh`, not `activate`. This project's shell is tcsh.
