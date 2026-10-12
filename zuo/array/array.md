# Smallest num

```python
    arr = [5, 3, 9, 1, 6]
    smallest = min(arr)
```

## Swap
```python
    nums[i], nums[j] = nums[j], nums[i]  # Swap, no extra space
```

# Reverse Copy

```python
    reversed_list = list[::-1]
```

### Avoid creating a second list with reversed()

reversed() returns an iterator, so you don’t need an extra list copy until you convert it:

```python
    bytes_list = list(map(int, reversed(binary_string)))
```