# some ideology:
# left(2k) running left elimination on 2k elements
# left(2k+1) running left elimination on 2k+1 elements
# same goes for right
# we need to reduce the problem down
# observations:
# running left(2k) == left(2k+1)  (same nums will be remianing in both the runs) --- (1)
# and left(2k) == 2 * right(k) (e.g. 2k) 
   # then left(2k)'s next round on 2,4,6,8, 10 which is equal to 2 * right(k) --- (2)
# and left(k) - 1 == k - right(k) as elment at index i from left will have same fate as index i from right --- (3)
# hence, deducing the recursion funtion:
# combine 2 and 3
############## left(n) = 2 * (n//2 - left(n//2) + 1) ###############

# also, n == 1 will be the base case
class Solution:
    def lastRemaining(self, n: int) -> int:
        return 1 if n == 1 else 2 * (n//2 - self.lastRemaining(n//2) + 1)
    
# time : O(logN) 
# space : O(1) constant space