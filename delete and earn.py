# idea is to sort the nums, for each element maintain 2 values
# avoid - not using the current value
# using - using the current value
# use greedy method to take the max out of avoid and using for each element
# also, check if prev largest value used is not equal to curr - 1
# if yes, add current value * (# occurance of curr) to avoid (as per the condition) to calculate avoid and using
# if no, then add current value * (# occurance of curr) to max(avoid, using)

import collections
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        avoid, using = 0, 0
        count = collections.Counter(nums)
        prev =None
        
        for each in sorted(count):
            if prev != each - 1:
                avoid, using = max(avoid, using), count[each] * each + max(avoid, using)
            else:
                avoid, using = max(avoid, using),  count[each] * each + avoid
                
            prev = each
        return max(avoid, using)

# time : O(Nlogn) - N to iterate over the nums and NlogN to sort the nums
# space : O(N) -  to store the freq. of each num in nums