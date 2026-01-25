
# https://www.bilibili.com/list/8888480?sid=3509640&oid=702378376&bvid=BV19m4y1n7mo
# Hard

def move(i:int, origin: str, to:str, other:str):
    if i==1:
        print("Move 1 " + "from " + origin + " to " + to)

    move(i, origin, other, to)
    move(i-1, origin, to, other)
    print("Move " + i + "from " + origin + " to " + to)
    move(i-1, other, to, origin)


class Solution:

    def hanoi(self, n:int):
        if n > 0 :
            move(n, "L", "R", "M")



s = Solution()
print(s.hanoi(3))
