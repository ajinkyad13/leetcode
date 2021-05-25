# idea is that two words are anagram is they have same letters with the same count of letters
# so make counter of each word and compare if both are exactly the same

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(s): return False
        
        return collections.Counter(s) == collections.Counter(t)
    
    
# time : O(N + M) - where N is len of first word and M is length of second word
# space : O(1) : constant space is used here (if not used counter and used a hashmap or dict ) in case of counter we can say O(N + M) worst case