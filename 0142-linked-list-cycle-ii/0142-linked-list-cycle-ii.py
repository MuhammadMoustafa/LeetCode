# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listSet = set()
        p = head
        while p != None:
            if p in listSet:
                return p
            listSet.add(p)
            p = p.next

        return None