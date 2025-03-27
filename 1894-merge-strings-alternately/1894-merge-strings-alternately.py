class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = list(word1)
        w2 = list(word2) 

        result = []

        for i in range(0,max(len(w1), len(w2))):
            if i < len(w1) and i < len(w2):
                result.append(w1[i])
                result.append(w2[i])
            elif i >= len(w1) and i <= len(w2):
                result.append(w2[i])

            elif i >= len(w2) and i <= len(w1):
                    result.append(w1[i])

        return "".join(result)