1class Solution:
2    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
3        n = len(A)
4
5        a_set = set()
6        b_set = set()
7
8        C = []
9        
10        for i in range(n):
11            a_set.add(A[i])
12            b_set.add(B[i])
13
14            result = 0
15            if A[i] in b_set:
16                result += 1
17            if B[i] in a_set:
18                result += 1
19            
20            if A[i] == B[i]:
21                result -= 1
22
23            if i == 0:
24                C.append(result)
25            else:    
26                C.append(C[-1] + result)
27
28        return C
29
30
31
32