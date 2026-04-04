1class Solution:
2    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
3        
4        if rows == 1:
5            return encodedText
6
7        cols = len(encodedText) // rows
8        grid = [encodedText[i*cols: (i+1)*cols] for i in range(rows)]
9        result = []
10
11        for j in range(cols):
12            for i in range(rows):
13                if(j+i) >= cols:
14                    break
15                result += grid[i][j+i]
16            
17        return "".join(result).rstrip()