# idea is to apply dfs starting from every cell with value > 0 
# so while applying he dfs, record cur cell val an make the cell = 0
# and apply dfs, so we make sure that we don't visit the cell again
# in depth of the dfs, we visit a cell with val > 0, apply the prev logic and again apply dfs on that cell
# so we are appling DFS**2
# if it's end of dfs return the val and add that to the parent dfs ans
# put bak the recorded value for further dfs

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxRows, maxCols = len(grid), len(grid[0])
        
        def dfs(r,c):
            # get curr val and make the cell =0
            currVal, ans, grid[r][c] = grid[r][c], 0, 0
            
            # check all the adjacent cells of curr cell and apply dfs if val > 0
            for x, y in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                if 0 <= x < maxRows and 0 <=  y < maxCols and grid[x][y] >0:
                    ans = max(ans, dfs(x,y))
                    
            grid[r][c] = currVal
            return ans + currVal
        
        ans = 0
        for r in range(maxRows):
            for c in range(maxCols):
                # only appy dfs to cells with val > 0
                if grid[r][c] > 0:
                    ans = max(ans, dfs(r,c))
                    
        return ans
    
# time : O(M**2 * N**2) - we aply dfs for all the cells with val > 0 so DFS **2
# space : O(1) ~ if we dont conside the input