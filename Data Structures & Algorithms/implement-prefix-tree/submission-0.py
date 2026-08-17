class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word: # a
            if c not in curr.children: # a not in {}
                curr.children[c] = TrieNode() #{a = TrieNode children more}
            curr = curr.children[c] #already exists 
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord 
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        