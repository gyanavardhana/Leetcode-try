class TrieNode:
    def __init__(self):
        self.children  = {}
        self.freq = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.freq += 1
    def issub(self,word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
        return curr.freq > 1
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        tree = Trie()
        for word in words:
            for i in range(len(word)):
                tree.insert(word[i:])
        res = []
        for word in words:
            if tree.issub(word):
                res.append(word)
        return res