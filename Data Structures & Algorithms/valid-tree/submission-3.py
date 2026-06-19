class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Check n
        #Params: adj_nodes HM, seen set., 
        #Go through node pairs and add to adj hm, add to eachother's
        #DFS to make sure no loops with node and prev_val return True or False
        #Return dfs on 0 and-1 and check if seen set len == n, thats what checks connected
        if len(edges) > (n - 1): return False
        adj_map = defaultdict(list)
        seen = set()

        for node1, node2 in edges:
            adj_map[node1].append(node2)
            adj_map[node2].append(node1)
        
        def dfs(node, prev_node):
            if node in seen:
                return False
            seen.add(node)
            for neighbor in adj_map[node]:
                if neighbor == prev_node:
                    continue
                if dfs(neighbor, node) == False: return False
            return True

        return dfs(0, -1) and len(seen) == n
