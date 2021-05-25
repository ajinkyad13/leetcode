# maintain a dict to store the indexes, 
# for each element if target-each in dict, return current index and val of dic[curr element]
# else add the curr element and index to dic

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,each in enumerate(nums) :
            if target - each in dic:
                return [i, dic[target- each]]
            else:
                dic[each] = i
                
# time :  O(N) - to iterate over the dic 
# space : O(N) - to store the indexes