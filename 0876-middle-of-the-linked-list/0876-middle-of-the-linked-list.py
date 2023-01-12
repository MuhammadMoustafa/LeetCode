# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        
        slowP = head
        fastP = head
        
        while fastP.next != None:
            slowP = slowP.next
            if fastP.next.next != None:
                fastP = fastP.next.next
            else:
                break                
                
        return slowP
            