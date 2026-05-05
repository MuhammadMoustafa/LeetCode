1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        if k == 0:
9            return head
10
11        n = 0
12        node_list = []
13        cur_pointer = head
14        while cur_pointer != None:
15            node_list.append(cur_pointer)
16            cur_pointer = cur_pointer.next
17            n += 1
18            
19        if n == 0:
20            return head
21
22        k = k % n
23        
24        if k == 0:
25            return head
26
27        to_rotate = node_list[-k:]
28        node_list[n-k-1].next = None
29
30        for node in to_rotate[::-1]:
31            node.next = head
32            head = node
33
34        return head
35            