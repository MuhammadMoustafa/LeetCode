1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        keys = {
4            'U': 0,
5            'D': 0,
6            'R': 0,
7            'L': 0,
8        }
9        for move in moves:
10            keys[move] += 1
11
12        return keys['U'] == keys['D'] and keys['R'] == keys['L']