class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        persons = set(range(1, n+1))
        count = [-inf]+[0]*n
        for t in trust:
            persons.discard(t[0])
            count[t[1]] += 1
            
        judge, judge_count = max(enumerate(count), key=itemgetter(1))
        if judge_count == n-1 and judge in persons:
            return judge
        else:
            return -1
            
        
        