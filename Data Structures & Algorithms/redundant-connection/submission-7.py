class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # The point is to find the first cycle, not just any
        # Params: n = len(edges), adj_map HM
        # Make dfs to check for cycle and return true or false. T = Cycle, F = No Cycle
        # Go through all VE, append them to list, make new seen bool arr, if dfs True return that n1,n2
        # If the whole thing passes return empty list
        n = len(edges)
        adj_map = defaultdict(list)

        def dfs(node, prev):
            if seen[node]:
                return True
            seen[node] = True
            for neigh in adj_map[node]:
                if neigh == prev:
                    continue
                if dfs(neigh, node) == True:
                    return True
            return False

        for n1, n2 in edges:
            adj_map[n1].append(n2)
            adj_map[n2].append(n1)
            seen = [False] * (n + 1)
            if dfs(n1, -1) == True:
                return [n1, n2]
        return []
