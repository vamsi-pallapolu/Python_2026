# Modules & Imports

## What is a module?
A **module** is just a `.py` file. When you `import` it, you can use its functions and variables in another file. A **package** is a folder containing modules. This is how you split code across files and reuse it.

## Basic imports
```python
import math
math.sqrt(16)               # 4.0
math.pi                     # 3.14159...
```
`import math` binds the name `math` in the current namespace; you access members through the dot.

## Import specific names
```python
from math import sqrt, pi
sqrt(16)                    # 4.0
```
Convenient, but pollutes the current namespace and hides where the name came from. Prefer the module-qualified form for anything ambiguous.

## Aliasing with `as`
```python
import numpy as np
import pandas as pd
from math import sqrt as square_root
```
Rename on import — common for long/collision-prone names.

## Star imports — `from x import *`
```python
from math import *          # generally discouraged
```
Imports every public name. Makes the source of each name unclear and can silently shadow existing names. Fine in an interactive shell; avoid in scripts and libraries.

## `if __name__ == "__main__":`
Every module has a `__name__` attribute. When the file is **run directly**, `__name__ == "__main__"`. When it's **imported**, `__name__` is the module's dotted name. This idiom lets a file behave as both a library and a script.
```python
# hello.py
def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    print(greet("World"))
```
Run: `python hello.py` → prints `Hello, World`.
Imported: `from hello import greet` → the `print` does **not** run.

## Packages
A directory becomes a package when Python finds `__init__.py` in it (or, in modern Python, even without it via **namespace packages**). Sub-modules use dotted paths.
```
myapp/
    __init__.py
    utils/
        __init__.py
        strings.py
        math.py
```
```python
from myapp.utils.strings import slugify
import myapp.utils.math as mm
```

## Absolute vs relative imports
Inside a package, you can import siblings with a **relative** import.
```python
# inside myapp/utils/strings.py
from . import math              # sibling module
from ..config import DEFAULTS   # parent package
```
Absolute imports (`from myapp.utils import math`) are more explicit and preferred by PEP 8 for anything but internal package code.

## The import path (`sys.path`)
Python searches for modules in this order:
1. The directory of the script (or the current directory for interactive sessions).
2. Directories in the `PYTHONPATH` environment variable.
3. Installation-dependent defaults (stdlib + `site-packages`).

Inspect:
```python
import sys
sys.path
```

## Import caches (`sys.modules`)
Once imported, a module is cached in `sys.modules`. Subsequent `import` statements return the cached object — they do **not** re-execute the file.
```python
import sys
"math" in sys.modules       # True after first import
```
Use `importlib.reload(module)` if you truly need to re-execute (rare — mostly debugging in a REPL).

## Common patterns
```python
# Library imports at the top of the file
import os
import sys
from pathlib import Path

# Third-party imports next
import requests

# Local imports last
from .helpers import fetch
```
PEP 8 groups imports in this order — stdlib, third-party, local — separated by blank lines.

## Gotchas
- **Circular imports** — if `a.py` imports `b.py` which imports `a.py`, one side may see a **partially initialized** module. Restructure the code, or move the import inside a function to defer it.
- **`from x import y` binds `y` in your namespace by value at import time.** Rebinding `x.y` later won't update your local `y`.
- **`__name__ == "__main__"` guard is required** if the module might be imported. Without it, side effects run on every import.
- **Star imports can silently shadow builtins** — `from math import *` overwrites your `pow` with `math.pow`. Rarely worth the noise.
- **Modules are cached** — restart the interpreter (or `importlib.reload`) if you want fresh state after editing.
- **Package needs an entry point** — `python -m myapp` runs `myapp/__main__.py`; `python myapp/` needs `__main__.py` too.
