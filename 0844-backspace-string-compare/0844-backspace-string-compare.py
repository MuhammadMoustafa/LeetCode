class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def removeChar(s):
            i = 0
            while i < len(s): 
                if s[i] == '#':
                    if i > 1:
                        if i+1 < len(s):
                            s = s[:i-1]+s[i+1:]
                        else:
                            s = s[:i-1]
                        i -= 2
                    else:
                        if i+1 < len(s):
                            s = s[i+1:]
                        else:
                            s = ""
                        i = -1
                i +=1      
            i = 0
            return s
        
        s = removeChar(s)
        t = removeChar(t)
        return s == t
        