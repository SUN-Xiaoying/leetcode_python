# https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=problem-list-v2&envId=trie


# 1588ms Beats 5.06%
class Trie:

    def __init__(self):
        self.count = 1
        INT_MAX = 2000
        self.tree = [[0] * 26 for _ in range(INT_MAX)]
        self.pass_count = [0]*INT_MAX
        self.end_count = [0]*INT_MAX

    def get_index(self, ch:str) -> int:
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        cur = 1
        self.pass_count[cur] += 1
        for ch in word:
            idx = self.get_index(ch)
            if self.tree[cur][idx] == 0:
                self.count +=1
                self.tree[cur][idx] = self.count
            cur = self.tree[cur][idx]
            self.pass_count[cur] += 1
        self.end_count[cur] += 1

    def search(self, word: str) -> bool:
        cur = 1
        for ch in word:
            idx = self.get_index(ch)
            if self.tree[cur][idx] == 0:
                return False
            cur = self.tree[cur][idx]

        return self.end_count[cur]>0

    def startsWith(self, prefix: str) -> bool:
        cur = 1
        for ch in prefix:
            idx = self.get_index(ch)
            if self.tree[cur][idx] == 0:
                return False
            cur = self.tree[cur][idx]

        return self.pass_count[cur] > 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)