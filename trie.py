class Trie():
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word.lower():
            if node.has_child(char):
                node = node.get_child(char)
            else:
                node = node.add_child(char)
        node.is_word = True

    def get_node(self, string):
        node = self.root
        for char in string:
            if not node.has_child(char):
                return None
            else:
                node = node.get_child(char)
        return node

class TrieNode():
    def __init__(self, char = ""):
        self.char = char
        self.children = []
        self.is_word = False

    def add_child(self, char):
        child = TrieNode(char)
        self.children.append(child)
        return child

    def has_child(self, char):
        return char in [c.char for c in self.children]

    def get_child(self, char):
        return [c for c in self.children if c.char == char][0] if self.has_child(char) else None