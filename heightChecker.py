# idea is to sort the array and check if the each element in the sorted array is equal to the element in the given array in the same position

class Solution
    def heightChecker(self, heights List[int]) - int
        return sum([a != b for (a,b) in zip(heights, sorted(heights))])
    
# time  O(NLogN) to sort the array
# space  O(1) constant  space