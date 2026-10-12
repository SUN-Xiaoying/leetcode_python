class TrieNode:
    def __init__(self):
        self.pass_count = 0
        self.end_count = 0
        self.nexts = [None] * 26  # array for 26 lowercase letters


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, ch: str) -> int:
        """Helper to convert a char to an index (0–25)."""
        return ord(ch) - ord('a')
    
    # print(ord('a'))  # 97
    # print(ord('b'))  # 98
    # print(ord('z'))  # 122
