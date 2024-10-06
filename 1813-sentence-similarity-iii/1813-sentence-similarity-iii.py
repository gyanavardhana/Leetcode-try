class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1)<len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        words = sentence1.split(' ')
        swords = sentence2.split(' ')
        i,j = 0,0
        while i<len(swords) and words[i]==swords[i]:
            i+=1
        while j<len(swords) and words[-(j+1)] == swords[-(j+1)]:
            j+=1
        return i+j >= len(swords)
        
        



        