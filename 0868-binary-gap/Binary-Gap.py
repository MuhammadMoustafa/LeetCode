1class Solution:
2    def binaryGap(self, n: int) -> int:
3        bin_n = bin(n)[2:]
4        last_one = 0
5        longest_dist = 0
6        for idx in range(len(bin_n)):
7            if bin_n[idx] == '1':
8                longest_dist = max(longest_dist, idx - last_one)
9                last_one = idx
10
11        return longest_dist