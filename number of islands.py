# apply dfs for all the cells with val = 1 and in dfs make the val = 0 
# so all the connected 1's will be 0 in a single dfs
# on uber level for each cell = 1, increament number of islands by 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans, maxRows, maxCols = 0, len(grid), len(grid[0])
        
        def dfs(r,c):
            grid[r][c] = "0"
            
            for x, y in [(r+1,c), (r-1,c),(r,c-1), (r,c+1)]:
                if 0 <= x < maxRows and 0 <= y < maxCols and grid[x][y] == "1":
                    dfs(x,y)
            return
        
        for r in range(maxRows):
            for c in range(maxCols):
                if grid[r][c] == "1":
                    ans +=1
                    dfs(r,c)
        return ans
# time : O(M*N) - to traverse all cells
# space : O(1) ~ if input is not considered, constant space is used