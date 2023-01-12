class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        result = [0]*n

        def dfs(root, parent):
            cur_label = labels[root]
            label_dict = Counter({cur_label:1})
            
            for node in graph[root]:
                if node != parent:
                    label_dict += dfs(node, root)
              
            
            result[root] = label_dict[cur_label]
            return label_dict

        dfs(0, -1)
        return result

