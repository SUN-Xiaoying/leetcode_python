# Setup

Create and activate the project's virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

In VS Code, open this repository as the workspace. The workspace settings use
`venv/bin/python` as the interpreter. If VS Code is still using a different
interpreter, run **Python: Select Interpreter** from the Command Palette and
choose `venv/bin/python`.

To run the currently open Python file, use **Run → Start Debugging** (F5) and
select **Python: Current File** if prompted. You can also run a file from the
integrated terminal, for example:

```bash
python dp/array/coinChange.py
```

## Upgrade pip

```bash
python -m pip install --upgrade pip
```


## Python naming

| Concept | Convention | Example |
|---|---|---|
| Functions and variables | Lowercase with underscores (snake_case) | `string_utils.py`, `math_helpers.py` |
| Classes | Capitalized words (PascalCase) | `class DataLoader:` |
| Private module-level names | Prefix with an underscore | `_internal_var = 42` |


## Miscellaneous Python notes

> No, you do not need to add a semicolon (;) at the end of every statement in Python. **Python uses line breaks to determine the end of a statement, making ; optional in most cases**.

|Concept|Code|
|---|---|
|HashMap|`dict()`|


## Remove Duplicate

```python
    nums = list(set(nums))  # remove duplicates
```

## MAX / MIN
### Int

```python
import sys

INT_MAX = sys.maxsize        # usually 2**63 - 1 on 64-bit systems
INT_MIN = -sys.maxsize - 1   # usually -2**63
```

### Float

```python
    min_value = float('-inf')  # smaller than any finite float
    max_value = float('inf')   # larger than any finite float
```

## Swap

```python
    # Swap elements at index 1 and 3
    arr[1], arr[3] = arr[3], arr[1]
```

* will take up extra space
 
## Mid

```python
    mid = left + (right - left) // 2
```

## Sum

```python
    expected_sum = n * (n + 1) // 2
```

## Range

`range(start, stop, step)`

```python

    for i in range(10, 0, -1):
        10
        9
        8
        7
        6
        5
        4
        3
        2
        1
```

## Random

```python
import random

# Random integer from 1 to 10, including both endpoints
number = random.randint(1, 10)
```
