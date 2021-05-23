# idea is that two words are anagram of each other if letter count is exactly the same
# so maintain a count of the characters (only lower case alpha is in input) so [] * 26 for each word
# use the tuple of the count as key in a dic and append the words to value list with the same count tuple
# return the dic values

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = collections.defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            for let in word:
                count[ord(let) - ord('a')] +=1
            words[tuple(count)].append(word)
        return words.values()
    
# time : O(NK) to iterate over words N, where K is the len of longest word in the dictionary
# space : O(26 * N) ~ O(N) to store the mapping and count of words
