class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def createAdjList(edges):
            adj_lst = [[] for _ in range(n)]
            for edge in edges:
                adj_lst[edge[0]].append(edge[1])
                adj_lst[edge[1]].append(edge[0])
            return adj_lst

        adj = createAdjList(edges)

        def dfs(node, parent):
            totalTime = 0
            childTime = 0

            for child in adj[node]:
                if child == parent: continue
                childTime = dfs(child, node)

                if(childTime or hasApple[child]): totalTime += childTime + 2

            return totalTime
        
        
        return dfs(0, None)
