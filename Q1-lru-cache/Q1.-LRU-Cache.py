1class Node:
2    def __init__(self, key, value):
3        self.key = key
4        self.value = value
5        self.prev = None
6        self.next = None
7
8    def __str__(self):
9        return f"[key = {self.key}, value = {self.value}]"
10
11    def __repr__(self):
12        return f"[key = {self.key}, value = {self.value}]"
13
14class LRUCache:
15
16    def __init__(self, capacity: int):
17        self.head = Node(0, 0)
18        self.tail = Node(0, 0)
19        
20        self.head.next = self.tail
21        self.tail.prev = self.head
22
23        self.capacity = capacity
24        self.cache = {}
25       
26
27    def _add_to_head(self, node):
28        node.next = self.head.next
29        self.head.next.prev = node
30        node.prev = self.head
31        self.head.next = node
32
33    def _remove_node(self, node):
34        next_node = node.next
35        prev_node = node.prev
36
37        prev_node.next = next_node
38        next_node.prev = prev_node
39
40    def get(self, key: int) -> int:
41        if key in self.cache:
42            node = self.cache[key]
43            self._remove_node(node)
44            self._add_to_head(node)
45            return self.cache[key].value
46
47        else:
48            return -1
49        
50    def put(self, key: int, value: int) -> None:
51        
52        # print(f"key = {key}, value = {value} => cache = ",self.cache)
53        if key in self.cache:
54            self.cache[key].value = value
55            node = self.cache[key]
56            self._remove_node(node)
57            self._add_to_head(node)
58            return
59
60        if len(self.cache) == self.capacity:
61            node_to_remove = self.tail.prev
62            self._remove_node(node_to_remove)
63            del self.cache[node_to_remove.key]
64            
65        ## first time
66        node = Node(key, value)
67        self._add_to_head(node)
68        self.cache[key] = node
69        
70
71# Your LRUCache object will be instantiated and called as such:
72# obj = LRUCache(capacity)
73# param_1 = obj.get(key)
74# obj.put(key,value)