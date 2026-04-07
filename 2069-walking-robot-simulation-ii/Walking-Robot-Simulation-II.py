1class Robot:
2
3    def __init__(self, width: int, height: int):
4        
5        self.width = width - 1
6        self.height = height - 1
7        self.peri = 2*(self.width+self.height)
8        self.pos = [0, 0]
9        self.dir = "East"
10
11    def step(self, num: int) -> None:
12        num = num % self.peri
13        
14        if num == 0:
15            if self.pos == [0, 0]:
16                self.dir = "South"
17            elif self.pos == [self.width, 0]:
18                self.dir = "East"
19            elif self.pos == [self.width, self.height]:
20                self.dir = "North"
21            elif self.pos == [0, self.height]:
22                self.dir = "West"
23            
24            return
25
26        while num:
27            match self.dir:
28                case "East":
29                    valid_steps = min(self.width - self.pos[0], num)
30                    self.pos[0] += valid_steps
31                    if valid_steps < num:
32                        self.dir = "North"
33            
34                case "West":
35                    valid_steps = min(self.pos[0], num)
36                    self.pos[0] -= valid_steps
37                    if valid_steps < num:
38                        self.dir = "South"
39
40                case "North":
41                    valid_steps = min(self.height - self.pos[1], num)
42                    self.pos[1] += valid_steps
43                    if valid_steps < num:
44                        self.dir = "West"
45            
46                case "South":
47                    valid_steps = min(self.pos[1], num)
48                    self.pos[1] -= valid_steps
49                    if valid_steps < num:
50                        self.dir = "East"
51    
52            num -= valid_steps
53                    
54    def getPos(self) -> List[int]:
55        return self.pos
56
57    def getDir(self) -> str:
58        return self.dir