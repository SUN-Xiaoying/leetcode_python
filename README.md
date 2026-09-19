# Set up
```bash
python3 -m venv venv
source venv/bin/activate
```

# Upgrade

```bash
python -m pip install --upgrade pip
```


## Python naming
|Concept| Naming                                  ||
|---|-----------------------------------------|---|
|Function and Variable Names| Lowercase with underscores (snake_case) |`string_utils.py`,`math_helpers.py`|
|Class Names| Camel                                   |`class DataLoader:`|
Global Variable (Private)|Prefix with an underscore _|`_internal_var = 42`|


# Jackpot

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
    max_value = float('-inf')  # for smallest possible value
    min_value = float('inf')   # for largest possible value
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
# Random integer from 1 to 10, including both endpoints
number = random.randint(1, 10)
```