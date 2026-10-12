# 生成

1. self + 左 + 上 - 左上

```python
sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + matrix[i][j]
```
2. 加入0行0列，减少边界判断

```python
# 获取原始行列
rows = len(matrix)
cols = len(matrix[0])

# 创建新的数组，先用0填充
new_matrix = [[0] * (cols + 2) for _ in range(rows + 2)]

# 将原数组复制到新的数组的中间
for i in range(rows):
    for j in range(cols):
        new_matrix[i + 1][j + 1] = matrix[i][j]
```


# 查询
(a,b) to (c,d)

```python
 sum[c][d] - sum[a-1][d] - sum[c][b-1] + sum[a-1][b-1]
```

# 二维差分

2D difference array

> 左上不变

```python
    def add(a:int, b:int, c:int, d:int, v:int):
        diff[a][b] += v
        diff[a][d+1] -= v
        diff[c+1][b] -= v
        diff[c+1][d+1] += v
```
