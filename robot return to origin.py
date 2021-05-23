# idea is to check if opposite directions have same number of occurances

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic = {"R":0, "L":0, "U": 0, "D": 0}
        for move in moves:
            dic[move] += 1
        return (dic["R"] == dic["L"] and dic["U"] == dic['D'])

# time : O(N) - to iterate over the moves
# space : O(4) ~ O(1) - constant space 