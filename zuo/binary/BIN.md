# XOR
异或运算是无进位相加
1
2. 找出只出现一次的数（异或特性：成对数字异或为 0）。

# 加减乘除
## add
XOR + 进位，一直到没有进位
a^b + (a&b)<<1

## minus
-x = (~x + 1) & 0xFFFFFFFF

# Shift
> Python does not have `>>>`.

Only `>>` exists, and it always behaves like arithmetic right shift:

### Logical Shift
```python
def logical_rshift(x, n, bits=32):
    """
    Logical right shift: shift x by n bits, fill with 0.
    bits = 32 for 32-bit integers.
    """
    if x < 0:
        x += 1 << bits  # convert to unsigned
    return x >> n
```

# Negative

```python
    ～x=−x−1

print(~0)   # -1
print(~1)   # -2
print(~5)   # -6
print(~-5)  # 4
```
( 整体 - 1 ) 取反

# Multiple

左乘右除
Non-negative, >=0
```python
1<<1 #2
1<<2 #4
```
Python 需要手动处理溢出
```python
(n << shift_number) & 0xFFFFFFFF
```

# Print
## Integer to Binary
```python
    n = 42
    binary_str = format(n, "032b") # 32进制
    print(binary_str)
```
## Binary to Integer
```python
s = "1010"        # binary for 10
n = int(s, 2)
print(n)          # 10
```
