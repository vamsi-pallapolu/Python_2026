# About Python

## Definition
Python is a general-purpose programming language with clear syntax and a large standard library.

It is used for:

- automation scripts
- web applications
- data science
- machine learning
- testing
- command-line tools

Python files usually end with `.py`.

```python
print("Hello, Python")
```

## Main Features
| Feature | Meaning |
|---------|---------|
| Easy to read | Python code usually looks close to plain English |
| Dynamically typed | variables do not need declared types |
| Strongly typed | Python does not silently mix unrelated types |
| Interpreted | code is run by the Python interpreter |
| Cross-platform | the same code can run on macOS, Linux, and Windows |
| Large ecosystem | many built-in modules and third-party packages are available |

Example of dynamic typing:

```python
x = 10
x = "hello"
```

The same variable name can point to different types at different times.

Example of strong typing:

```python
print("Age: " + 25)  # TypeError
```

Python does not automatically convert `25` to a string here.

Use explicit conversion:

```python
print("Age: " + str(25))
```

## How Python Code Runs
When you run a Python file, Python does a few steps internally:

1. Reads the `.py` source code.
2. Checks the syntax.
3. Compiles the code to bytecode.
4. Runs the bytecode using the Python virtual machine.

You usually do not see these steps.

```bash
python3 hello.py
```

Python may create a `__pycache__` folder to store bytecode files.

## CPython
The most common Python implementation is **CPython**.

CPython is:

- written in C
- the reference implementation of Python
- the version most people install from python.org

Other implementations include PyPy, Jython, IronPython, and MicroPython.

## Python 2 and Python 3
Python 3 is the current version of Python.

Python 2 is no longer supported.

Important differences:

| Topic | Python 2 | Python 3 |
|-------|----------|----------|
| Print | `print "hi"` | `print("hi")` |
| Strings | bytes by default | Unicode text by default |
| Division | `5 / 2` gives `2` | `5 / 2` gives `2.5` |
| Support | ended in 2020 | actively supported |

Use Python 3 for new code.

## Running Python
Run a Python file:

```bash
python3 hello.py
```

Open the interactive shell:

```bash
python3
```

Run a short command:

```bash
python3 -c "print(2 + 3)"
```

Run a module:

```bash
python3 -m pip --version
```

## Installing Packages
Python packages are usually installed with `pip`.

```bash
pip install requests
```

For a project, install packages inside a virtual environment instead of the system Python.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests
```

Virtual environments are covered later in [20_Virtual_Environments.md](20_Virtual_Environments.md).

## Common Tools
| Tool | Purpose |
|------|---------|
| `python3` | runs Python |
| `pip` | installs packages |
| `venv` | creates virtual environments |
| `pytest` | runs tests |
| `mypy` or `pyright` | checks type hints |
| `ruff` | checks style and common mistakes |
| `black` | formats code |

## The Python Philosophy
Python values readable code.

You can see Python's design ideas by running:

```python
import this
```

One useful line is:

```text
Readability counts.
```

## Common Mistakes
- Using Python 2 examples for new Python code.
- Installing packages into the system Python instead of a virtual environment.
- Assuming Python has no compile step at all. It compiles to bytecode internally.
- Using `python` when your system requires `python3`.
- Forgetting that Python is case-sensitive.

## Summary
- Python is readable, flexible, and widely used.
- Python 3 is the modern version.
- Python code is run by an interpreter.
- CPython is the most common implementation.
- Use virtual environments for project dependencies.
