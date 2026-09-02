# Modules & Imports

## Definition
A **module** is a single `.py` file. A **package** is a directory of modules. Both are units of code reuse: importing binds names from another file into the current namespace.

## Import forms
```python
import math                     # bind module object as `math`
math.sqrt(16)

from math import sqrt, pi       # bind names directly
sqrt(16)

import numpy as np              # rename on import
from math import sqrt as sq
```
`import x` keeps the origin visible at each call site. `from x import y` is shorter but drops that trace and rebinds `y` locally.

## Star imports
```python
from math import *              # imports every public name
```
Discouraged in modules and libraries: it hides the source of each name and can shadow builtins. A module can restrict what `*` exposes:
```python
__all__ = ["greet", "VERSION"]  # only these are pulled in by `import *`
```

## `if __name__ == "__main__":`
Every module has a `__name__` attribute. It is `"__main__"` when the file is run directly and the module's dotted name when imported. A module's top-level code executes on import; the guard confines script-only side effects.
```python
# hello.py
def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    print(greet("World"))       # runs only via `python hello.py`
```

## Packages
A directory is a **regular package** if it contains `__init__.py`. That file runs once on first import and can expose package-level names.
```
myapp/
    __init__.py
    utils/
        __init__.py
        strings.py
```
A directory without `__init__.py` is a **namespace package** (PEP 420). Namespace packages can span multiple directories on `sys.path`; they have no init code.

## Absolute vs relative imports
```python
# inside myapp/utils/strings.py
from myapp.utils import math    # absolute — preferred by PEP 8
from . import math              # relative — sibling module
from ..config import DEFAULTS   # relative — parent package
```
Relative imports resolve against `__package__`. They only work when the file is imported as part of a package; running it directly (`python strings.py`) makes `__package__` empty and relative imports raise `ImportError`. Use `python -m myapp.utils.strings` instead.

## Running a package
```bash
python -m myapp                 # executes myapp/__main__.py
```
`-m` sets `__package__` correctly, so relative imports resolve.

## The import path
`sys.path` is searched in order:
1. Directory of the script (or `""` for interactive sessions).
2. Entries in `PYTHONPATH`.
3. Installation defaults (stdlib, then `site-packages`).

## Module cache — `sys.modules`
The first import executes the file and stores the resulting module object in `sys.modules`. Every later `import` returns the cached object without re-executing.
```python
import sys
"math" in sys.modules           # True after first import
```
This is why editing a module in a running REPL has no effect until reload.

## Dynamic and reload
```python
import importlib
mod = importlib.import_module("myapp.utils.strings")   # dynamic import
importlib.reload(mod)                                  # re-run the file
```
`reload` re-executes the module and rebinds its attributes in place, but existing references (e.g. `from mod import fn`) still point at the old objects.

## Import order (PEP 8)
Group imports, separated by blank lines:
```python
import os                       # 1. stdlib
import sys

import requests                 # 2. third-party

from .helpers import fetch      # 3. local / same package
```

## Gotchas
- **Circular imports** — `a` imports `b`, `b` imports `a`. One side sees a **partially initialized** module. Defer by moving the import inside a function, or use `if TYPE_CHECKING:` for type-only imports.
- **`from x import y` binds by value at import time.** Rebinding `x.y` afterwards does not update the local `y`.
- **Missing guard** — top-level side effects run every time the module is imported, not just when executed as a script.
- **Star imports shadow silently** — no warning when `from math import *` overwrites your `pow`.
- **Heavy top-level code slows startup** — every importer pays the cost. Push work into functions.
- **Namespace packages don't run init code** — if you need setup on import, use a regular package.
