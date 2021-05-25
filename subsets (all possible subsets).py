# DP like approach, use previous calculated values to calculate new ones (backtracking  + recursion)
# initialize list of list as out,
# for each num in nums, use the each element from out to append the current num

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for num in nums:
            out += [curr + [num] for curr in out]
        return out

# time : O(N * 2**N) - N to iterate over the nums and 2**N to generate all possible sets 
# space : O(N * 2**N) - 2**N choices for N numbers 
            