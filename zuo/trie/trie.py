class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = True  # '#' marks end of word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
