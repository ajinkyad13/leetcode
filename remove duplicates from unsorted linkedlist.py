# idea is to rebuild the connections between the nodes rather than rebuilding the linked list itself.
# have a map of nodes, node as key and val if reperated (bool)
# create a dummy = 0  = prev and curr = head and  iterate over the linked list
# if the curr is not repeated, prev.next = curr, prev = curr (or prev.next)
# and # brek the prev.next and set to None so that prev.next will always be a node which is non repeating and if not always None 
# curr = curr.next
# return dummy.head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        seen = collections.defaultdict(bool)
        curr = head
        while curr:
            if curr.val not in seen:
                seen[curr.val] = True
            else:
                seen[curr.val] = False
            curr = curr.next
        
        # create dummy
        dummy = ListNode(0)
        prev, curr = dummy, head
        
        while curr:
            if seen[curr.val]:
                prev.next = curr
                prev = curr
            curr = curr.next
            prev.next = None
        return dummy.next
# time : O(N) - iterate over the linked list
# space : O(N) - to store of repeated or not
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        