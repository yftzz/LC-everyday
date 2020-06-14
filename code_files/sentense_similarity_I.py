class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        
        for i in range(len(words1)):
            found = False
            if words1[i] == words2[i]:
                continue
            
            for j in range(len(pairs)):
                if words1[i] in pairs[j] and pairs[j][abs(pairs[j].index(words1[i]) - 1)] == words2[i]:
                    found = True
                    break
                    
            if not found:
                return False
        return True



class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        from collections import defaultdict
        if len(words1) != len(words2):
            return False
        wordList = defaultdict(set)
        for p0, p1 in pairs:
            wordList[p0].add(p1)
            wordList[p1].add(p0)
        
        for word1, word2 in zip(words1, words2):
            if word1 == word2:
                continue
            
            if word1 in wordList[word2]:
                continue
            
            return False
        return True
        