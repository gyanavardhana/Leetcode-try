class TrieNode:
    def __init__(self):
        self.children = {}
        self.pc = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.pc += 1

    def su(self,word):
        node = self.root
        ts = 0
        for char in word:
            if char in node.children:
                node = node.children[char]
                ts += node.pc
            else:
                break
        return ts



class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        Tre = Trie()
        for i in words:
            Tre.insert(i)
        c = 0
        res = []
        for word in words:
            res.append(Tre.su(word))
        return res
        