# flyod cycle detection
# two pointers, one is fast and other is slow,
# fast p, goes two steps at a time and slow goes one step at a time
# if they meet at some point there is a cycle
# else no cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        sp , fp = head, head
        
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            if sp == fp:
                return True
        return False
    
'''
time : O(N) : if no cycle
       O(N + K) ~ O(N) (if there is a cycle)where K is the extra steps that fast pointer ran for which is a constant (K is the cyclic length) we could say K is N*constant so finally O(N)
Space: O(1): constant space used here
''' 
         