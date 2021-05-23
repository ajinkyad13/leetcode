# idea is to use a dic to store the freq of the letters
# iterate over the the first  char with freq == 1, is our ans

import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = collections.defaultdict(int)
        for each in s:
            freq[each] += 1
        
        for i, each in enumerate(s):
            if freq[each] == 1:
                return i
        return -1
    
# time : O(2N) ~ O(N) to iterate over the string 
# space : O(1) to store the freq of limited characters of 26 (lower case alphaa)