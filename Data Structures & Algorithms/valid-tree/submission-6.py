class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Check n
        #Params: adj_nodes HM, seen set., 
        #Go through node pairs and add to adj hm, add to eachother's
        #DFS to make sure no loops with node and prev_val return True or False
        #Return dfs on 0 and-1 and check if seen set len == n, thats what checks connected

        seen, cur_path = set(), set()
        adj_list = defaultdict(list)

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        
        def dfs(node, prev_val):
            if node in cur_path: return False
            if node in seen: return True
            cur_path.add(node)
            seen.add(node)
            for neigh in adj_list[node]:
                if neigh == prev_val: continue
                if dfs(neigh, node) == False: return False
            cur_path.remove(node)
            return True
        
        return dfs(0, -1) and n == len(seen)