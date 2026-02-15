1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        ar = [True if l == "1" else False for l in a[::-1]]
4        br = [True if l == "1" else False for l in b[::-1]]
5
6        bigger = ar if len(ar) >= len(br) else br
7        smaller = br if len(br) <= len(ar) else ar
8
9        result = ""
10        carry = False
11        for i in range(len(smaller)):
12            r1 = bigger[i] ^ smaller[i] ^ carry
13            carry = (bigger[i] & smaller[i]) | (bigger[i] & carry) | (smaller[i] & carry)
14            result += str(int(r1))
15
16        for i in range(len(smaller), len(bigger)):
17            r1 = bigger[i] ^ carry
18            carry = bigger[i] & carry
19            result += str(int(r1))
20        
21        if carry:
22            result += str(int(carry))
23
24        return result[::-1]