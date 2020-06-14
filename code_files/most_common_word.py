class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re
        from collections import Counter
        wordList = re.findall(r'\w+', paragraph.lower())
        freq = Counter(wordList)
        maxFreq = 0
        maxWord = ''
        for word in freq:
            if not word in banned:
                if maxFreq <= freq[word]:
                    maxFreq = freq[word]
                    maxWord = word
        return maxWord