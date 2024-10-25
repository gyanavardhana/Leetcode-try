class Trie:
    def __init__(self):
        self.childs = {}
        self.end = False
class Solution:
    def __init__(self):
        self.root = Trie()
    def addWord(self, word: List[str]) -> None:
        curr = self.root
        for i in word.split('/'):
            if i not in curr.childs:
                curr.childs[i] = Trie()
            curr = curr.childs[i]
        curr.end = True
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for i in folder:
            self.addWord(i)
        def bt(node,path):
            if node.end:
                return ['/'.join(path)]
            ans = []
            for child in node.childs:
                path.append(child)
                ans += bt(node.childs[child], path) 
                path.pop()
            return ans
        return bt(self.root, [])
        