# idea is to have two position vars for both the words and ans
# every time we see the position is updated we check min(ans, abs(pos1 - pos2))

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos1, pos2 = -1, -1
        ans = float("inf")
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                pos1 = i
            elif wordsDict[i] == word2:
                pos2 = i
            if pos1 != -1 and pos2 != -1:
                ans = min(ans, abs(pos1 - pos2))
        return ans
    
# time : O(NM) - to iterate over N words and M is length of the longest word in the dictionary, word1 or word2 as we are comparring them
# space : O(1) - using constant space here