# idea is to make a set of give words and for each word in the words list, check word made by consecutive letters in each word is present in that word set 
# e.g. curr word = "apple" and curr word set ('a', 'app','appl', 'apple') 

class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = ""
        wordSet = set(words)
        
        for each in words:
            if len(each) > len(ans) or (len(ans) == len(each) and each < ans):
                if all(each[:k] in wordSet for k in range(1, len(each))):
                    ans = each
        return ans
    
# time : O(Sumation of k**2) where k is the length of the word
# space : O(Sumation of k**2)  to make the substrings and store them