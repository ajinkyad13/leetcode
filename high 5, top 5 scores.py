## iterarte over ethe list and get scores of each student in a dic, use id as key and heap as scores 
# after adding scores for each student, check if the scores > 5
# if yes, heappop, else add

import collections
import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = collections.defaultdict(list)
        
        for item in items:
            heapq.heappush(scores[item[0]], item[1])
            if len(scores[item[0]]) > 5:
                heapq.heappop(scores[item[0]])
        
        return [[ids, sum(scores[ids])//5] for ids in sorted(scores.keys())]
    
# time : O(NlogN) - to make a heap and iterate over the list 
# space : O(N) - to store the scores of each student