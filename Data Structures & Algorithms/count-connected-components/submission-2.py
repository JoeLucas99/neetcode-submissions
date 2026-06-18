class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Make and adj_list HM, and seen arr of Falses for range(n), res int
        #Fill out adj_list
        #Make a DFS to check if for every neighbor its seen index is False.
        #   If False then make true and run dfs on the neighbor
        #Go through every node in range(n) and check if its seen index is False
        # If False, make turn True, run the DFS to make all its neighbors True, and increment res
        #Return res

        adj_map = defaultdict(list)
        seen_map = [False] * n
        res = 0

        for node1, node2 in edges:
            adj_map[node1].append(node2)
            adj_map[node2].append(node1)
        
        def dfs(node):
            for neighbor in adj_map[node]:
                if seen_map[neighbor] == False:
                    seen_map[neighbor] = True
                    dfs(neighbor)

        for node in range(n):
            if seen_map[node] == False:
                seen_map[node] = True
                dfs(node)
                res += 1
        return res
                