# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = []
        dummy = ListNode()

        for i in lists:
            curr = i 
            while curr:
                merged.append(curr.val)
                curr = curr.next

        merged.sort()
        
        if not merged:
            return None

        newcurr = dummy

        for num in merged:
            newcurr.next = ListNode(num)
            newcurr = newcurr.next

        return dummy.next
