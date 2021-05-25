# idea is, for each word, check if it can be formed using the given word
# if yes, check if the len of maxWord is < curr word or if len is same for both check if the curr word < maxWord (lexicographically)

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        maxWord = ""
        
        def check(s, word):
            i = 0
            for  char in s:
                if char == word[i]:
                    i+=1
                    if len(word) == i:
                        return True
            return False
        
        for word in dictionary:
            if check(s, word) and ( len(maxWord) < len(word) or (len(word) ==    len(maxWord) and maxWord > word)):
                maxWord = word
        return maxWord
    
# time : O(NK) - N is total number of words in the dictionary and k is length of longest word in the dictionary
# space : O(1) - using constant space here