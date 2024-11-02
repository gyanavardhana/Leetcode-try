class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l = sentence.split(" ")
        l.append(l[0])
        '''
        ll = len(l[len(l)-1])
        lf = l[len(l)-1][ll-1] == l[0][0]
        print(l)
        '''
        c = 0
        for i in range(1,len(l)):
            le = len(l[i-1])
            if l[i-1][le-1] == l[i][0]:
                c += 1
        if c==len(sentence.split(" ")):
            return True
        return False

        