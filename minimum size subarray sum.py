'''
Idea is sliding window method and maintain a currSum and a left pointer to denote the start of the window (end will be our current index) and a var to store the minLen of subarray
If currSum >= target, remove each elemestarting from left pointer until currSum >= target and update the minLen var
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, currSum, minLen = 0, 0, float("inf")
        
        for i in range(len(nums)):
            currSum += nums[i]
            while currSum >= target:
                minLen = min(minLen, i - l +1)
                currSum -= nums[l]
                l+=1
        return minLen if minLen != float("inf") else 0
    

# time : O(N) - iterating over the nums
# space: O(1) - constant space