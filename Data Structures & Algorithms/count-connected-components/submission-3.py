class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Make and adj_list HM, and seen arr of Falses for range(n), res int
        #Fill out adj_list
        #Make a DFS to check if for every neighbor its seen index is False.
        #   If False then make true and run dfs on the neighbor
        #Go through every node in range(n) and check if its seen index is False
        # If False, make turn True, run the DFS to make all its neighbors True, and increment re

        res = 0
        adj_map = defaultdict(list)
        seen = [False] * n

        for n1, n2 in edges:
            adj_map[n1].append(n2)
            adj_map[n2].append(n1)

        def dfs(node):
            for neighbor in adj_map[node]:
                if seen[neighbor] == False: 
                    seen[neighbor] = True
                    dfs(neighbor)

        for node in range(n):
            if seen[node] == False:
                seen[node] = True
                dfs(node)
                res += 1

        return res