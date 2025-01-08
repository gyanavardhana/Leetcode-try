class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isp(str1, str2):
            n1,n2 = len(str1),len(str2)
            if n1>n2:
                return False
            return str2[:n1] == str1 and str2[-n1:] == str1
        n = len(words)
        c = 0
        for i in range(n):
            for j in range(i+1, n):
                if isp(words[i], words[j]):
                    c += 1
        return c        