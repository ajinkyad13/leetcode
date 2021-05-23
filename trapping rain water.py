# idea is to use two pointers, l =0 and r = len(heights) - 1 and two vars to store lmax and rmax
# if value at l < val at r:
   # check if lmax > val at l
    # if yes, add maxL - height[l] to ans
    # if no, update lmax to val at l
# if no,
 # check if rmax > val at r
    # if yes, add rmax - height[r] to ans
    # if no, update rmax to val at r

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, lMax, rMax, ans = 0, len(height) -1, 0, 0 , 0
        
        while l < r:
            if height[l] < height[r]:
                if lMax < height[l]:
                    lMax = height[l]
                else:
                    ans += lMax - height[l]
                l+=1
            else:
                if rMax < height[r]:
                    rMax = height[r]
                else:
                    ans += rMax - height[r]
                r-=1
        return ans
    
# time : O(N) to iterate over the heights list
# space : O(1) constant space used here
        