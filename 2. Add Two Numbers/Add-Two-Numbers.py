1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(
8        self, l1: Optional[ListNode], l2: Optional[ListNode]
9    ) -> Optional[ListNode]:
10        node = ListNode(0, None)
11        result = node
12        carry = 0
13
14
15        while l1 or l2 or carry:
16            rsum = carry
17
18            if l1:
19                rsum += l1.val
20                l1 = l1.next
21
22            if l2:
23                rsum += l2.val
24                l2 = l2.next
25
26            carry = rsum // 10
27            node.next = ListNode(rsum % 10, None)
28            
29            node = node.next
30
31        return result.next