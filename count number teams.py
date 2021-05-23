'''
Idea is that for each element there are two possible seq to make a team:
 1. element < curr at left and element > curr at right (decreasing)
 2. element > curr at left and element < curr at right (increasing)
 
 So, if we have the count of els < curr and els > curr on both the sides, left and right
 the total number of teams that can be formed will be (for each element)
 (#els < curr on left) * (#els > curr right) + (#els > curr on left) * (#els < curr on right)
 
 also note that the rating are  unique hence no need to worry about ===
'''

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans, n = 0, len(rating)
        leftSmall = [0] * n
        rightSmall = [0] * n
        leftHigh = [0] * n
        rightHigh = [0] * n
        
        for i in range(n-1):
            for j in range(i+1, n):
                if rating[i] > rating[j]:
                    rightSmall[i] +=1
                else:
                    rightHigh[i] +=1
                    
        for i in range(n-1, 0, -1):
            for j in range(i-1, -1, - 1):
                if rating[i] > rating[j]:
                    leftSmall[i] +=1
                else:
                    leftHigh[i] +=1
        
        for i in range(n):
            ans += (leftSmall[i]) * rightHigh[i]
            ans += leftHigh[i] * rightSmall[i]
            
        return ans

# time : O(2(N**2)) ~ O(N**2) - iterating over the rating (once nested)
# space : O(4N) ~ O(N) - to store the vals < and > than the curr
        