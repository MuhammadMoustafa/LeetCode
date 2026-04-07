1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")
4