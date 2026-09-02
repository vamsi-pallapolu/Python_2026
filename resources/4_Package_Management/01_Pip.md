# pip

## Definition
`pip` is Python's standard package installer. It installs and manages third-party packages that are not included in Python's standard library.

Most packages are downloaded from the Python Package Index, usually called PyPI:

```text
https://pypi.org
```

Example:
```bash
python -m pip install requests
```

This installs the `requests` package into the Python environment connected to that `python` command.

## Why we need pip
Python includes many built-in modules, but real projects often need external libraries.

Examples:
| Need | Common package |
|------|----------------|
| HTTP requests | `requests`, `httpx` |
| Data analysis | `pandas`, `numpy` |
| Web apps | `flask`, `django`, `fastapi` |
| Testing | `pytest` |
| Environment variables | `python-dotenv` |
| Formatting | `black`, `ruff` |

Without `pip`, you would have to manually download packages, place them in the correct directory, manage dependencies yourself, and update them by hand.

`pip` automates that work.

## What pip does
`pip` can:

- install packages
- upgrade packages
- uninstall packages
- install dependencies required by a package
- install exact versions
- install from a `requirements.txt` file
- install from local folders
- install from Git repositories
- show package metadata
- list installed packages
- create reproducible dependency lists

## pip, PyPI, and packages
These terms are related but different.

| Term | Meaning |
|------|---------|
| `pip` | the command-line installer |
| PyPI | the public package repository |
| package | reusable Python code distributed for installation |
| dependency | another package required by a package |
| environment | the Python installation or virtual environment receiving packages |

When you run:
```bash
python -m pip install requests
```

`pip` downloads `requests` from PyPI, downloads its dependencies, and installs everything into the active Python environment.

## Why use `python -m pip`
Prefer:
```bash
python -m pip install package_name
```

Instead of:
```bash
pip install package_name
```

This ensures `pip` belongs to the same Python interpreter you are using.

This matters when multiple Python versions are installed:
```bash
python --version
python3 --version
pip --version
pip3 --version
```

`python -m pip` avoids installing a package into one Python version and running code with another.

## Checking pip
```bash
python -m pip --version
```

Example output:
```text
pip 24.0 from ... (python 3.12)
```

This shows both the pip version and the Python version it belongs to.

## Installing pip
Most modern Python installations include pip.

If pip is missing:
```bash
python -m ensurepip --upgrade
```

Then upgrade it:
```bash
python -m pip install --upgrade pip
```

## Virtual environments
A virtual environment is an isolated Python environment for one project.

Create one:
```bash
python -m venv .venv
```

Activate on macOS or Linux:
```bash
source .venv/bin/activate
```

Activate on Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

After activation:
```bash
python -m pip install requests
```

The package installs into `.venv`, not globally.

## Where installed packages are stored
pip installs packages into the active Python environment's `site-packages` directory.

In a virtual environment on macOS or Linux, the path usually looks like this:
```text
.venv/lib/python3.12/site-packages/
```

On Windows, it usually looks like this:
```text
.venv\Lib\site-packages\
```

If you install globally, packages go into the global Python installation's `site-packages` directory. If you install with `--user`, packages go into the current user's Python user-site directory.

Check the install locations for the current Python:
```bash
python -m site
```

Or:
```bash
python -c "import site; print(site.getsitepackages())"
python -c "import site; print(site.getusersitepackages())"
```

## What pip puts inside `site-packages`
When installing a package, pip usually places two kinds of content in `site-packages`.

Example after installing `requests`:
```text
site-packages/
  requests/
  requests-2.32.3.dist-info/
```

| Item | Purpose |
|------|---------|
| package directory | actual importable Python code |
| `.dist-info` directory | metadata such as version, dependencies, license, and installed files |

The package directory is what Python imports:
```python
import requests
```

The `.dist-info` directory is what packaging tools use to understand what is installed:
```bash
python -m pip show requests
```

## Where command-line tools are stored
Some packages install command-line programs.

Example:
```bash
python -m pip install black
```

This installs the importable package into `site-packages`, and it also installs a command-line script.

In a virtual environment on macOS or Linux:
```text
.venv/bin/black
```

On Windows:
```text
.venv\Scripts\black.exe
```

When the virtual environment is activated, its script directory is placed first on `PATH`, so typing:
```bash
black .
```

runs the `black` command from the virtual environment.

## Why virtual environments matter
Virtual environments prevent dependency conflicts.

Example:
- Project A needs `django==4.2`
- Project B needs `django==5.0`

Installing both globally can create conflicts. Separate virtual environments allow each project to use its own package versions.

## Common pip commands
| Command | Purpose |
|---------|---------|
| `python -m pip install requests` | install a package |
| `python -m pip install --upgrade requests` | upgrade a package |
| `python -m pip uninstall requests` | uninstall a package |
| `python -m pip list` | list installed packages |
| `python -m pip show requests` | show package details |
| `python -m pip freeze` | show exact installed versions |
| `python -m pip check` | check dependency conflicts |
| `python -m pip cache dir` | show pip cache location |
| `python -m pip cache purge` | clear pip cache |

## Installing packages
Install the latest compatible version:
```bash
python -m pip install requests
```

Install multiple packages:
```bash
python -m pip install requests pytest black
```

Install an exact version:
```bash
python -m pip install requests==2.32.3
```

Install a minimum version:
```bash
python -m pip install "requests>=2.32"
```

Install a version range:
```bash
python -m pip install "django>=4.2,<5"
```

Quotes are useful because shells can interpret characters like `<` and `>`.

## Upgrading packages
Upgrade one package:
```bash
python -m pip install --upgrade requests
```

Upgrade pip itself:
```bash
python -m pip install --upgrade pip
```

Upgrade from a requirements file:
```bash
python -m pip install --upgrade -r requirements.txt
```

## Uninstalling packages
```bash
python -m pip uninstall requests
```

Skip confirmation:
```bash
python -m pip uninstall -y requests
```

## Listing installed packages
```bash
python -m pip list
```

Example:
```text
Package    Version
---------- -------
pip        24.0
requests   2.32.3
```

Show outdated packages:
```bash
python -m pip list --outdated
```

## Showing package details
```bash
python -m pip show requests
```

This shows metadata such as:
- package name
- version
- summary
- homepage
- author
- install location
- dependencies

## How installed packages load into a program
Installing a package does not automatically load it into every program. It only makes the package available to that Python environment.

A package is loaded when your code imports it:
```python
import requests
```

When Python sees an import, it searches for the module using `sys.path`.
```python
import sys

for path in sys.path:
    print(path)
```

`sys.path` usually includes:
- the directory of the script being run
- directories from the `PYTHONPATH` environment variable, if set
- the standard library directories
- the active environment's `site-packages` directory

If Python finds the package on `sys.path`, it loads and executes the package's module code.

## Import flow
For:
```python
import requests
```

Python roughly does this:

1. Checks whether `requests` is already loaded in `sys.modules`.
2. Searches each location in `sys.path`.
3. Finds the installed `requests` package inside `site-packages`.
4. Runs the package initialization code, usually `requests/__init__.py`.
5. Stores the loaded module in `sys.modules`.
6. Binds the name `requests` in your program.

After the first import, importing the same module again usually reuses the cached module from `sys.modules`.

## Checking where a package was imported from
Use `.__file__`:
```bash
python -c "import requests; print(requests.__file__)"
```

Example output:
```text
/path/to/project/.venv/lib/python3.12/site-packages/requests/__init__.py
```

This is one of the best ways to confirm that your program is importing from the environment you expect.

## Installed name vs import name
The name used with pip is not always the same as the name used in `import`.

Examples:
| pip install name | import name |
|------------------|-------------|
| `python-dotenv` | `dotenv` |
| `beautifulsoup4` | `bs4` |
| `pillow` | `PIL` |
| `opencv-python` | `cv2` |

Always check the package documentation for the correct import name.

## Why `ModuleNotFoundError` happens after installing
If this fails:
```python
import requests
```

But you already installed it, the most common reason is that pip installed the package into a different Python environment.

Debug with:
```bash
python -m pip --version
python -c "import sys; print(sys.executable)"
python -c "import requests; print(requests.__file__)"
```

The Python shown by `sys.executable` should match the environment where pip installed the package.

## `requirements.txt`
A `requirements.txt` file records packages needed by a project.

Example:
```text
requests==2.32.3
pytest==8.3.2
```

Install all dependencies from it:
```bash
python -m pip install -r requirements.txt
```

Generate one from the current environment:
```bash
python -m pip freeze > requirements.txt
```

## `pip freeze` vs `pip list`
| Command | Use |
|---------|-----|
| `pip list` | human-readable list of installed packages |
| `pip freeze` | requirements-style output with exact versions |

Example:
```bash
python -m pip freeze
```

Output:
```text
certifi==2024.7.4
charset-normalizer==3.3.2
idna==3.7
requests==2.32.3
urllib3==2.2.2
```

`pip freeze` includes direct packages and transitive dependencies.

## Direct dependencies vs transitive dependencies
A direct dependency is a package your project explicitly needs.

A transitive dependency is required by one of your direct dependencies.

Example:
```text
your project
  requests
    certifi
    charset-normalizer
    idna
    urllib3
```

If you install `requests`, pip also installs the packages `requests` depends on.

## Reproducible installs
For simple projects, `requirements.txt` is common:
```text
requests==2.32.3
pytest==8.3.2
```

Pinned versions make installs more predictable.

Install:
```bash
python -m pip install -r requirements.txt
```

For larger applications, teams often use lock files from tools such as:
- `pip-tools`
- Poetry
- uv
- PDM

pip itself installs from requirement files but does not create a full lock file with dependency resolution metadata.

## Installing from a local folder
If a folder contains a Python package with `pyproject.toml`, install it with:
```bash
python -m pip install .
```

Install in editable mode during development:
```bash
python -m pip install -e .
```

Editable mode means changes to the source code are reflected without reinstalling the package.

## Installing from Git
```bash
python -m pip install git+https://github.com/user/project.git
```

Install a specific branch, tag, or commit:
```bash
python -m pip install git+https://github.com/user/project.git@main
python -m pip install git+https://github.com/user/project.git@v1.0.0
python -m pip install git+https://github.com/user/project.git@abc123
```

Use this carefully. PyPI releases are usually easier to reproduce.

## Wheels and source distributions
Python packages are commonly distributed as:

| Format | Meaning |
|--------|---------|
| wheel | pre-built package archive, usually `.whl` |
| source distribution | source archive, usually `.tar.gz` |

Wheels install faster because they are already built.

Source distributions may require build tools, compilers, or system libraries.

## Dependency resolver
pip has a dependency resolver. It tries to find versions that satisfy all package requirements.

Example conflict:
```text
package-a requires requests<2
package-b requires requests>=2
```

pip may fail because both constraints cannot be true.

Check installed dependency compatibility:
```bash
python -m pip check
```

## Package indexes
By default, pip installs from PyPI.

Use another index:
```bash
python -m pip install --index-url https://example.com/simple package_name
```

Use PyPI plus an extra index:
```bash
python -m pip install --extra-index-url https://example.com/simple package_name
```

Be careful with extra indexes. Package names can overlap across repositories.

## pip configuration
View configuration:
```bash
python -m pip config list
```

Set a config value:
```bash
python -m pip config set global.index-url https://pypi.org/simple
```

Configuration can exist globally, per user, or per virtual environment.

## Cache
pip caches downloaded packages to speed up future installs.

Show cache directory:
```bash
python -m pip cache dir
```

List cached files:
```bash
python -m pip cache list
```

Clear the cache:
```bash
python -m pip cache purge
```

## Installing without cache
```bash
python -m pip install --no-cache-dir package_name
```

This is sometimes used in containers to reduce image size.

## User installs
Install into the current user's site-packages:
```bash
python -m pip install --user package_name
```

This avoids modifying the system Python, but virtual environments are usually cleaner for projects.

## System Python warning
Avoid installing packages into the system Python unless you know exactly why.

This can break operating-system tools or other projects.

Prefer:
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install package_name
```

Avoid:
```bash
sudo pip install package_name
```

## pip and `pyproject.toml`
Modern Python projects often define build metadata in `pyproject.toml`.

Example:
```toml
[project]
name = "my-project"
version = "0.1.0"
dependencies = [
    "requests>=2.32",
]
```

pip can install a project that uses `pyproject.toml`:
```bash
python -m pip install .
```

pip reads the build system requirements and builds or installs the package.

## pip vs venv
| Tool | Purpose |
|------|---------|
| `venv` | creates isolated Python environments |
| `pip` | installs packages into an environment |

They work together:
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install requests
```

## pip vs conda
| Tool | Main use |
|------|----------|
| pip | Python package installer, usually from PyPI |
| conda | environment and package manager, often for scientific stacks |

Conda can install non-Python system libraries. pip focuses on Python packages.

If using conda, prefer installing conda packages with conda first, then use pip only when needed.

## pip vs pipx
| Tool | Use |
|------|-----|
| pip | install libraries into a project environment |
| pipx | install and run Python command-line applications in isolated environments |

Good `pipx` use cases:
```bash
pipx install black
pipx install poetry
```

Good `pip` use case:
```bash
python -m pip install requests
```

## Common project workflow
```bash
# create environment
python -m venv .venv

# activate environment
source .venv/bin/activate

# upgrade installer
python -m pip install --upgrade pip

# install dependencies
python -m pip install requests pytest

# save exact installed versions
python -m pip freeze > requirements.txt

# later, recreate environment
python -m pip install -r requirements.txt
```

## Common errors and fixes
### `ModuleNotFoundError`
Problem:
```text
ModuleNotFoundError: No module named 'requests'
```

Possible causes:
- the package is not installed
- it was installed into a different Python environment
- the virtual environment is not activated
- the pip install name is different from the import name

Fix:
```bash
python -m pip install requests
python -c "import requests; print(requests.__version__)"
```

## `pip: command not found`
Use:
```bash
python -m pip --version
```

If pip is missing:
```bash
python -m ensurepip --upgrade
```

## Permission denied
This often happens when trying to install globally.

Preferred fix:
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install package_name
```

Avoid using `sudo pip install`.

## Build failed
Some packages need compilers or system dependencies when no wheel is available.

Try:
```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install package_name
```

If it still fails, read the package's installation instructions.

## Dependency conflict
Check conflicts:
```bash
python -m pip check
```

You may need to loosen or tighten version ranges in `requirements.txt`.

## Advantages of pip
- **Standard tool** - included with most Python installations.
- **Huge package ecosystem** - installs packages from PyPI.
- **Dependency handling** - installs required dependencies automatically.
- **Environment integration** - installs into locations Python already searches, such as `site-packages`.
- **Version control** - supports exact versions and version ranges.
- **Project reproducibility** - works with `requirements.txt`.
- **Virtual environment support** - installs cleanly into isolated environments.
- **Flexible sources** - installs from PyPI, local folders, archives, and Git repositories.
- **Cross-platform** - works on macOS, Linux, and Windows.
- **Simple commands** - easy to learn for beginners.

## Limitations of pip
- It does not manage Python versions.
- It does not create virtual environments by itself.
- It does not install every possible system-level dependency.
- `requirements.txt` is not a full lock file.
- Dependency conflicts can still require manual decisions.
- Installing into the wrong Python environment is common if you use plain `pip`.

## Best practices
- Use a virtual environment for each project.
- Prefer `python -m pip` over plain `pip`.
- Keep `pip` updated inside the environment.
- Pin versions for applications.
- Use version ranges carefully for libraries.
- Commit `requirements.txt` for simple projects.
- Do not commit `.venv`.
- Avoid `sudo pip install`.
- Run `python -m pip check` after dependency changes.
- Confirm imports with `python -c "import package; print(package.__file__)"` when environment confusion is possible.
- Read package documentation before installing unfamiliar packages.

## Quick reference
```bash
python -m pip --version
python -m pip install package_name
python -m pip install "package_name>=1,<2"
python -m pip install --upgrade package_name
python -m pip uninstall package_name
python -m pip list
python -m pip list --outdated
python -m pip show package_name
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
python -m pip check
```

## Mental model
Use this sequence for most projects:

1. Create a virtual environment with `python -m venv .venv`.
2. Activate it.
3. Install packages with `python -m pip install ...`.
4. Save dependencies with `python -m pip freeze > requirements.txt`.
5. Reinstall dependencies later with `python -m pip install -r requirements.txt`.

The main rule: install packages into the same Python environment that runs your code.
