# recursion with memoization
# basically, recursively check for +1 and +2 steps and record the values for these two steps, if the current step is already in the list take the value from there

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n
        
        def rec(x):
            if x == n:
                return 1
            if x > n:
                return 0
            if memo[x] != -1:
                return memo[x]
            memo[x] = rec(x+1) + rec(x+2)
            return memo[x]
        return rec(0)

# time : O(N) ~ the recursion tree can go upto n depth
# space : O(N) to store the calculated values
