# straight forward, two pointer, one head (prev), secnd head.next (curr)
# if curr.next = prev.next, then  prev.next = curr.next 
# else prev = curr 
# then curr = curr.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        
        prev , curr = head, head.next
        
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
    
# time: O(N) - iterate over the nodes
# space O(1) - constant space