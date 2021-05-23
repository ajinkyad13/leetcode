# idea is to take sum of all the nums (totalsum) and maitain a currSum var
# for each num in nums:
 # check if totalSum - each - currSum == currSum  ( because the sum of els left to each will be totalSum - currSum - each, it's logical)
 # if yes return the index
 # else add each to currSum
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum, currSum = sum(nums), 0
        
        for i, each in enumerate(nums):
            if totalSum - currSum - each == currSum:
                return i
            else:
                currSum += each
        return -1

# time: O(N) to iterate over the nums 
# space : O(1) constant space 