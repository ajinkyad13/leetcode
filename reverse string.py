# idea is to swap values from left to the same position on the right side

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

# time : O(N) - to traverse n//2 els 2 times (from left n//2 and from right n//2)
# space: O(1) - constant space is used here