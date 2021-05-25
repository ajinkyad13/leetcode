# idea is to maintain prev and next node in each step
# and make curr.next = prev
# prev = curr
# curr = nextNode
# return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
    
# time : O(N) to iterate over the linkedList
# space : O(1) constant space is used here