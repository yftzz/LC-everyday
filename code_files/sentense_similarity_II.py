class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        wordList = dict()
        for p1, p2 in pairs:
            if p1 in wordList and p2 in wordList:
                while wordList[p1] != p1:
                    p1 = wordList[p1]
                while wordList[p2] != p2:
                    p2 = wordList[p2]
                wordList[p2] = p1
            elif p1 not in wordList and p2 not in wordList:
                wordList[p1] = p1
                wordList[p2] = p1
            elif p1 in wordList:
                wordList[p2] = wordList[p1]
            elif p2 in wordList:
                wordList[p1] = wordList[p2]
            else:
                raise ValueError

        for word1, word2 in zip(words1, words2):
            if word1 == word2:
                continue

            if word1 in wordList and word2 in wordList:
                while wordList[word1] != word1:
                    word1 = wordList[word1]
                while wordList[word2] != word2:
                    word2 = wordList[word2]
                if word1 == word2:
                    continue
            return False
        return True

class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return false
        wordList = dict()
        def find(w):
            if not w in wordList:
                wordList[w] = w
            while wordList[w] != w:
                w = wordList[w]
            return w
        for p1, p2 in pairs:
            p1 = find(p1)
            p2 = find(p2)
            wordList[p2] = p1
        for w1, w2 in zip(words1, words2):
            if find(w1) != find(w2):
                return False
        return True
