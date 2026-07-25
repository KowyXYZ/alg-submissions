"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return 

        if head is None:
            return None

        otn = {None: None} #none maps to none

        curr = head

        while curr:
            otn[curr] = Node(curr.val)
            curr = curr.next

        curr = head #wire
        while curr :
            copy = otn[curr]
            copy.next = otn[curr.next]
            copy.random = otn[curr.random]
            curr = curr.next

        return otn[head]
