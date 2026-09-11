# Modules and Imports

## Definition
A module is a Python file.

For example, `math_utils.py` is a module.

A package is a folder that contains Python modules.

Imports let you reuse code from another file or library.

## Importing a Module
Use `import` to load a module.

```python
import math

print(math.sqrt(16))
```

Output:

```text
4.0
```

When you use `import math`, you access names through `math`.

## Importing Specific Names
Use `from ... import ...` to import a specific name.

```python
from math import sqrt

print(sqrt(16))
```

This is shorter, but the module name is no longer visible at the call site.

## Import Aliases
Use `as` to give an import a shorter name.

```python
import math as m

print(m.sqrt(16))
```

This is common with large libraries.

```python
import numpy as np
import pandas as pd
```

## Creating Your Own Module
Suppose you have a file named `helpers.py`.

```python
def greet(name):
    return f"Hello, {name}"
```

You can import it from another file in the same folder.

```python
import helpers

print(helpers.greet("Vamsi"))
```

Or import the function directly.

```python
from helpers import greet

print(greet("Vamsi"))
```

## Top-Level Code Runs on Import
Python runs top-level code when a module is imported.

```python
# helpers.py
print("Loading helpers")

def greet(name):
    return f"Hello, {name}"
```

If another file imports `helpers`, `"Loading helpers"` is printed.

Keep top-level code small.

## The `__name__` Check
Use this pattern for code that should run only when the file is executed directly.

```python
def main():
    print("Run program")

if __name__ == "__main__":
    main()
```

If the file is imported, `main()` does not run automatically.

## Packages
A package is a folder of modules.

Example:

```text
myapp/
    __init__.py
    helpers.py
    main.py
```

`__init__.py` marks the folder as a regular package.

You can import from the package:

```python
from myapp.helpers import greet
```

## Absolute Imports
Absolute imports start from the package name.

```python
from myapp.helpers import greet
```

These are usually easiest to understand.

## Relative Imports
Relative imports use dots.

```python
from .helpers import greet
from ..config import settings
```

Relative imports are used inside packages.

They usually do not work when you run a file directly with `python file.py`.

Use `python -m package.module` instead.

## Import Search Path
Python searches for modules using `sys.path`.

```python
import sys

print(sys.path)
```

It usually includes:

1. the script's folder
2. paths from `PYTHONPATH`
3. standard library folders
4. installed package folders

## Import Style
PEP 8 recommends grouping imports like this:

```python
import os
import sys

import requests

from myapp.helpers import greet
```

Groups:

1. standard library imports
2. third-party imports
3. local project imports

## Star Imports
Avoid star imports in normal code.

```python
from math import *
```

This imports many names at once and makes it harder to see where a name came from.

Prefer explicit imports.

```python
from math import sqrt, pi
```

## Common Mistakes
- Putting important work at the top level of a module.
- Forgetting the `if __name__ == "__main__":` guard.
- Using star imports.
- Creating circular imports, where two modules import each other.
- Running a package file directly when it needs relative imports.

## Summary
- A module is a `.py` file.
- A package is a folder of modules.
- Use imports to reuse code.
- Prefer clear, explicit imports.
- Use the `__name__` guard for script-only code.
