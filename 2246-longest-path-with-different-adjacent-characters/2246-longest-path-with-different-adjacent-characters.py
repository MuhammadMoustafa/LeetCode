class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        if len(parent) == 1: return 1
        
        children = defaultdict(list)
        for idx, val in enumerate(parent):
            children[val].append(idx)
        
        global maxPath
        maxPath = 0

        def dfs(root):
            global maxPath
            if len(children[root]) == 0:
                if s[root] != s[parent[root]]: 
                    maxPath = max(maxPath, 1)
                    return 1
                else: return 0
            
            result = [0]
            for child in children[root]:
                if s[root] != s[child]:
                    result.append(dfs(child))
                else:
                    dfs(child)
            
            maxPath = max(maxPath, sum(nlargest(2, result)) + 1)
            return max(result) + 1

        dfs(0)
        return maxPath