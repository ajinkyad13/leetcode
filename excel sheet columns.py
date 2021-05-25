# Idea is to go from left to right, maintain a res = 0 and for each letter multiply by 26 and add it to the res 
'''
for each new multiply the res by 26 and then add the val of curr etter to the res
e.g. ABC
for A, res = res * 26 i.e. 0 * 26 = 0 then Add val of A i.e. 0+1 = 1
for B res = 1 (prev val of res) * 26 = 26 then add val of B ie. 26 + 2 = 28
for C res = 28 * 26 = 728 add val of C i.e. res = 728 + 3 = 731
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            res *= 26
            res += (ord(columnTitle[i]) - ord("A") +  1)
        return res

# time : O(N) - to iterate over each letter
# space : O(1) ~ constant space is used here