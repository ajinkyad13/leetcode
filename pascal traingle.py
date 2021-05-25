# DP question, basically the current output row is dependent on the last row in the triangle
# so, get the last row in the triangle and iterate over it and get sum of all the consecutive 2 numbers starting from index 1 to len(last row) - 2


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1], [1,1]]
        if numRows == 1: return [out[0]]
        if numRows == 2: return out
        
        while numRows > 2:
            temp = [1]
            for i in range(len(out[-1]) - 1):
                temp.append(out[-1][i] + out[-1][i+1])
            temp.append(1)
            out.append(temp)
            numRows -=1
        return out
    
# time : O(N**2) - where N is the numRows
# space : O(N**2) - to store the calulcated values