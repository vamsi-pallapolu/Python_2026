# Virtual Environments and `pip`

## Definition
A virtual environment is an isolated Python environment for one project.

It has its own Python interpreter and installed packages.

This keeps project dependencies separate.

## Why Use a Virtual Environment?
Different projects may need different package versions.

Example:

- project A needs `requests==2.28`
- project B needs `requests==2.31`

A virtual environment lets each project use the version it needs.

It also avoids installing packages into the system Python.

## Creating a Virtual Environment
Create a virtual environment with `venv`.

```bash
python3 -m venv .venv
```

`.venv` is a common folder name for the environment.

Do not commit `.venv` to Git.

## Activating a Virtual Environment
On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, `python` and `pip` should point to the virtual environment.

## Checking the Active Python
Use:

```bash
python -c "import sys; print(sys.executable)"
```

The path should include `.venv`.

You can also check installed packages:

```bash
pip list
```

## Installing Packages
Install packages with `pip`.

```bash
pip install requests
```

Install a specific version:

```bash
pip install requests==2.31.0
```

Upgrade a package:

```bash
pip install --upgrade requests
```

Remove a package:

```bash
pip uninstall requests
```

## Saving Dependencies
Use `pip freeze` to save installed package versions.

```bash
pip freeze > requirements.txt
```

Install from that file later:

```bash
pip install -r requirements.txt
```

Commit `requirements.txt` to Git.

Do not commit `.venv`.

## Deactivating
Use `deactivate` to leave the virtual environment.

```bash
deactivate
```

This affects only the current terminal session.

## Using Python Without Activation
Activation is convenient, but not required.

You can call the environment's Python directly.

```bash
.venv/bin/python script.py
```

On Windows:

```powershell
.\.venv\Scripts\python.exe script.py
```

## Common Workflow
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install requests
pip freeze > requirements.txt
```

Add `.venv/` to `.gitignore`.

```text
.venv/
```

## Other Tools
Several tools build on the same idea.

| Tool | Purpose |
|------|---------|
| `virtualenv` | older and widely used virtual environment tool |
| `pipx` | installs command-line tools in isolated environments |
| `poetry` | manages dependencies and packaging |
| `uv` | fast package and environment manager |
| `conda` | environment manager common in data science |

You can learn these later. Start with `venv` and `pip`.

## Common Mistakes
- Forgetting to activate the environment.
- Installing packages into the wrong Python.
- Committing `.venv` to Git.
- Forgetting to update `requirements.txt`.
- Assuming activation applies to every terminal. It only applies to the current terminal.

## Summary
- A virtual environment isolates packages for one project.
- Create one with `python3 -m venv .venv`.
- Activate it before installing packages.
- Use `pip install` to install packages.
- Save dependencies with `pip freeze > requirements.txt`.
- Commit `requirements.txt`, not `.venv`.
