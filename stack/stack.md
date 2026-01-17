# Define stack in python

In Python, a stack is usually implemented using a built-in data structure rather than a custom class.

✅ Recommended way: list

```python
stack = []

stack.append(1)   # push
stack.append(2)

top = stack.pop() # pop → 2
```

Read the top but don't pop:

```python
    stack[-1]
```
# isEmpty
```python
    if not stack:
        print("Empty")  # Output: Empty
    
    if stack:
        print("Not empty") 
```