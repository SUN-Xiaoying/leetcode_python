# https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=problem-list-v2&envId=trie

class TrieNode:
    def __init__(self):
        self.pass_count = 0
        self.end_count = 0
        self.nexts = [None]*26

# 72ms Beats 16.66%
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, ch: str):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        node = self.root
        node.pass_count += 1
        for ch in word:
            idx = self.get_index(ch)
            if node.nexts[idx] is None:
                node.nexts[idx] = TrieNode()
            node = node.nexts[idx]
            node.pass_count += 1
        node.end_count += 1

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = self.get_index(ch)
            if node.nexts[idx] is None:
                return False
            node = node.nexts[idx]

        return node.end_count > 0

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            idx = self.get_index(ch)
            if node.nexts[idx] is None:
                return False
            node = node.nexts[idx]

        return node.pass_count > 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)