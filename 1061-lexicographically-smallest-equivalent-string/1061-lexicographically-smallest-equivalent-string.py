class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        listSet = [] 
        dic = {}

        for idx, c1 in enumerate(s1):
            c2 = s2[idx]
            
            c1List = c2List = None
            for s in listSet:
                if c1 in s and c2 in s:
                    c1List = c2List = s
                    break
                if c1 in s:
                    c1List = s
                    if c2List:
                        break
                if c2 in s:
                    c2List = s
                    if c1List:
                        break


            if c1List and c1List == c2List:
                listSet.remove(c1List)
                listSet.append(c1List | c2List)
                continue

            if c1List:
                listSet.remove(c1List)
            else:
                c1List = set(c1)
            
            if c2List:
                listSet.remove(c2List)
            else:
                c2List = set(c2)

            listSet.append(c1List | c2List)

        for s in listSet:
            sortedList = sorted(list(s))
            key = sortedList[0]
            for c in sortedList:
                dic[c] = key
                        
        result = ""

        for c in baseStr:
            if c in dic:
                result += dic[c]
            else:
                result += c

        return result