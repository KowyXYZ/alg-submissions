# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        dummy = ListNode()

        storage = []

        curr = head

        final = []
        
        res = []
        while curr:
            storage.append(curr.val)
            curr = curr.next

        # if len(storage) % k == 0:
        #     final = [storage[i : i + k] for i in range(0, len(storage), k)]
        #     for i in final:
        #         i.reverse()
        # else:
        #     final = [storage[:k][::-1] + storage[k:]]   

        final = [storage[i : i + k] for i in range(0, len(storage), k)]
        print(final)
        for i in final:
            if len(i) == k:
                 i.reverse()
           



        
        for num in final:
            for j in num:
                res.append(j)
            

        newcurr = dummy

        for i in res:
            newcurr.next = ListNode(i)
            newcurr = newcurr.next
       
        return dummy.next