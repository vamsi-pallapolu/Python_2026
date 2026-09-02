# About Python

## What is Python?
Python is a popular programming language known for **easy-to-read syntax**. You write code in `.py` files and run them without a separate compile step. It's used everywhere — web apps, data science, machine learning, automation, scripting.

Key traits (interview one-liners):
- **Interpreted** — no separate compile step for the developer; source is executed by the Python interpreter (usually CPython).
- **Dynamically typed** — variable types are checked at runtime, not declared up front.
- **Strongly typed** — implicit unsafe conversions are rejected (`"1" + 2` → `TypeError`).
- **Garbage collected** — memory managed via reference counting + a cyclic garbage collector.
- **Multi-paradigm** — OOP, functional, procedural.
- **Cross-platform** — same code runs on Linux, macOS, Windows.
- **Open source** — governed by the Python Software Foundation (PSF).

---

## History

| Year | Event |
|------|-------|
| Late 1980s | **Guido van Rossum** starts Python at CWI (Netherlands) as a successor to the ABC language. |
| **1991**   | **Python 0.9.0** released — first public release. |
| 1994       | Python 1.0 — first major version; functional tools (`lambda`, `map`, `filter`, `reduce`) already present. |
| 2000       | Python 2.0 — list comprehensions, garbage collection for cycles, Unicode support. |
| 2008       | Python 3.0 — intentionally backward-incompatible cleanup (print is a function, `str` is Unicode by default, integer division changed). |
| 2020       | **Python 2.7 end-of-life** (Jan 1, 2020). Python 3 is the only actively supported line. |
| 2021       | Python 3.10 — structural pattern matching (`match / case`), better error messages. |
| 2023       | Python 3.12 — per-interpreter GIL (PEP 684, C-API), formalized f-string grammar (PEP 701), improved error messages. |
| 2024       | Python 3.13 — experimental **free-threaded (no-GIL) build**, experimental JIT. |

- The name **"Python"** was inspired by the British comedy group *Monty Python's Flying Circus*, not the snake.
- Van Rossum was known as the **"Benevolent Dictator For Life" (BDFL)**; he stepped down as BDFL in July 2018. Since 2019, Python has been governed by an elected **Steering Council** (PEP 8016).
- Language changes are proposed through **PEPs** (Python Enhancement Proposals). The style guide is **PEP 8**; the design philosophy is **PEP 20** ("The Zen of Python" — `import this`).

---

## Architecture — how Python code runs

Python is often called "interpreted", but under the hood there's a compile step too. The typical execution flow (for the reference implementation, **CPython**):

```
  .py source
       │
       ▼   ┌────────────────────────────────────────┐
  ┌────────┤       Python Compiler (in CPython)      │
  │        │  1. Lexer  → tokens                      │
  │        │  2. Parser → AST                         │
  │        │  3. Compiler → bytecode (.pyc)          │
  │        └────────────────────────────────────────┘
  │                    │
  │                    ▼
  │        ┌────────────────────────────────────────┐
  └──────► │  Python Virtual Machine (PVM)           │
           │  Executes bytecode instruction-by-      │
           │  instruction on the CPython runtime      │
           └────────────────────────────────────────┘
                       │
                       ▼
                    Output
```

### Step by step
1. **Source file** — plain-text `.py`, UTF-8 by default.
2. **Lexer** — breaks source into tokens (identifiers, keywords, literals, operators).
3. **Parser** — builds an **Abstract Syntax Tree (AST)** representing the program's structure.
4. **Compiler** — walks the AST and emits **bytecode** — a low-level, platform-independent instruction set for the Python VM.
5. **Cache** — bytecode is written to `__pycache__/<module>.cpython-<ver>.pyc` so future runs skip recompilation when the source hasn't changed.
6. **Python Virtual Machine (PVM)** — a **stack-based** interpreter (in CPython, written in C) that reads the bytecode and executes each opcode.

### Inspecting each stage
```python
import ast, dis

src = "x = 1 + 2"
print(ast.dump(ast.parse(src)))    # AST
dis.dis(compile(src, "<s>", "exec"))  # bytecode
```

### CPython vs other implementations
| Implementation | Written in | Highlights |
|----------------|-----------|-----------|
| **CPython**    | C         | Reference implementation. What you get from python.org. |
| **PyPy**       | RPython   | JIT-compiled; often several times faster on long-running pure-Python workloads (variable — sometimes slower for short scripts or C-extension-heavy code). |
| **Jython**     | Java      | Runs on the JVM; interop with Java. |
| **IronPython** | C#        | Runs on .NET / CLR. |
| **MicroPython**| C         | For microcontrollers (ESP32, Pico). |
| **GraalPy**    | Java      | Runs on GraalVM; interoperates with other GraalVM languages. |

### The GIL (Global Interpreter Lock)
CPython uses a **GIL** — a mutex that allows only **one thread** to execute Python bytecode at a time within a single process. Consequences:
- Threads don't give you true parallelism for CPU-bound Python code.
- I/O-bound code still benefits from threads (the GIL is released during I/O).
- Use **`multiprocessing`** or **C extensions** (NumPy, etc.) for CPU-bound parallelism.
- Python 3.13 introduces an experimental **free-threaded build** that removes the GIL.

### Memory management
- Every value is an **object** on the heap.
- **Reference counting** — objects are freed when their refcount drops to 0.
- **Cyclic garbage collector** (module `gc`) — cleans up reference cycles that pure refcounting can't.
- Small ints (`-5` to `256`) are **cached**, and some strings (identifier-like literals) are **interned** — so `a is b` may unexpectedly be `True` for equal small ints or compile-time string literals. Don't rely on this behavior; use `==` for value equality.

---

## Compiled vs interpreted — where does Python fit?

Python is **both**: a two-stage system.

| Stage           | Analogy             |
|-----------------|---------------------|
| `.py` → bytecode | Like `.java` → `.class` (a compile step, hidden from you). |
| bytecode → run   | Like the JVM running `.class` files. |

So a more accurate label is *"compiled to bytecode, interpreted on a virtual machine"* — similar in spirit to Java.

---

## Building, compiling, and running

### 1. Installing Python
- **macOS**: `brew install python`, or download from python.org, or use `pyenv`.
- **Linux**: usually preinstalled (`python3`); or via package manager (`apt install python3`, `dnf install python3`).
- **Windows**: installer from python.org (check "Add Python to PATH"), or Microsoft Store.
- **Version manager**: [`pyenv`](https://github.com/pyenv/pyenv) lets you switch versions per project.

### 2. Running a script
```bash
python3 hello.py           # execute a file
python3 -m module_name     # run a module as a script
python3                    # interactive REPL
python3 -c "print(1+1)"    # one-liner
```

The **shebang** line lets a script run directly on Unix:
```python
#!/usr/bin/env python3
print("hi")
```
```bash
chmod +x hello.py
./hello.py
```

### 3. Virtual environments (essential!)
Isolate dependencies per project so installs don't pollute the system Python.
```bash
python3 -m venv .venv           # create
source .venv/bin/activate       # activate (macOS/Linux)
.venv\Scripts\activate          # activate (Windows)
pip install requests            # install into this env
deactivate                      # exit
```
Alternatives: **`virtualenv`**, **`conda`**, **`poetry`**, **`pipenv`**, **`uv`** (fast).

### 4. Installing packages — `pip`
```bash
pip install <package>            # install
pip install -r requirements.txt  # install pinned list
pip freeze > requirements.txt    # snapshot current env
pip uninstall <package>
```

### 5. Bytecode files (`.pyc`)
CPython automatically writes bytecode to `__pycache__/`:
```
mymod.py
__pycache__/mymod.cpython-312.pyc
```
- The filename embeds the interpreter version so different Pythons don't clash.
- Regenerated automatically when the source changes (mtime-based by default; hash-based invalidation available since Python 3.7, PEP 552).
- You can precompile manually: `python -m compileall .`

### 6. Packaging & distribution
- **`pyproject.toml`** — the modern project config file: build-system (PEP 518), build backend interface (PEP 517), project metadata (PEP 621).
- **`setuptools` / `hatchling` / `flit` / `poetry`** — build backends.
- **`pip install .`** — install a local project.
- **`python -m build`** — produce a **sdist** (`.tar.gz`) and **wheel** (`.whl`).
- **`twine upload dist/*`** — publish to PyPI.
- **`wheel`** — a pre-built binary package format for pip.

### 7. Distributing standalone apps
Python isn't compiled to a native binary by default; to ship an executable:
- **PyInstaller / py2exe / cx_Freeze** — bundle Python + your code into an `.exe`/`.app`.
- **Nuitka** — actually compiles Python to C, producing a real binary.
- **shiv / PEX** — zipapp-based single-file archives.

---

## Interpreter internals — quick tour

- **CPython source**: [github.com/python/cpython](https://github.com/python/cpython)
- Main C entry point: `Python/ceval.c` — the giant `switch` on opcodes.
- **Object model**: everything is a `PyObject *` in C.
- **`dis` module** — disassemble any Python object to bytecode.
- **`ast` module** — parse to AST programmatically.
- **`sys` module** — interpreter state (`sys.version`, `sys.path`, `sys.getsizeof`, `sys.settrace`).

---

## Ecosystem — why Python is popular
- Massive standard library (`os`, `json`, `re`, `datetime`, `collections`, `itertools`, `pathlib`, `subprocess`, `asyncio`, ...).
- **PyPI** (Python Package Index) hosts hundreds of thousands of packages.
- Dominant in data / ML: **NumPy, pandas, scikit-learn, PyTorch, TensorFlow, JAX**.
- Web frameworks: **Django, Flask, FastAPI**.
- Automation / DevOps: **Ansible, SaltStack, Fabric**, plus scripting.
- Scientific: **SciPy, matplotlib, SymPy, Jupyter**.
- Great for **teaching** — clean syntax, high signal-to-ceremony ratio.

---

## Python 2 vs Python 3 (still occasionally asked)

| Feature | Python 2 | Python 3 |
|---------|----------|----------|
| `print` | statement `print "hi"` | function `print("hi")` |
| Default string | `bytes` | `str` (Unicode) |
| `/` on ints | floor division | true division (use `//` for floor) |
| `range()` | returns a list | returns a lazy `range` object (sequence, not an iterator) |
| `input()` | evaluates input | reads a string |
| `xrange` | separate lazy sequence | gone — `range` is now the lazy sequence |
| Long int | separate `long` type | `int` is arbitrary precision |
| End of life | Jan 1 2020 | actively supported |

Rule: **use Python 3.** Only touch Python 2 for legacy code you're migrating.

---

## Common tooling (interview-relevant)

| Tool | Purpose |
|------|---------|
| `python3` / `py`         | interpreter |
| `pip`                    | package installer |
| `venv` / `virtualenv`    | virtual environments |
| `poetry` / `uv`          | modern dependency/env managers |
| `pytest` / `unittest`    | testing |
| `mypy` / `pyright`       | static type checking |
| `ruff` / `flake8`        | linting |
| `black` / `ruff format`  | formatting |
| `pdb` / `ipdb`           | debugging |
| `cProfile` / `timeit`    | profiling / micro-bench |
| `pyenv`                  | manage multiple Python versions |
| `pyinstaller` / `nuitka` | build standalone binaries |

---

## The Zen of Python (`import this`, excerpt)

> Beautiful is better than ugly.
> Explicit is better than implicit.
> Simple is better than complex.
> Readability counts.
> There should be one — and preferably only one — obvious way to do it.

Guidance rather than rules, but it explains a lot of Python's design choices — including why the language avoids "magic" and unnecessary configurability.
