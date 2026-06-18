class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # The point is to find the first cycle, not just any
        # Params: n = len(edges), adj_map HM
        # Make dfs to check for cycle and return true or false. T = Cycle, F = No Cycle
        # Go through all VE, append them to list, make new seen bool arr, if dfs True return that n1,n2
        # If the whole thing passes return empty list
        n = len(edges)
        adj_map = defaultdict(list)

        def dfs(node, parent):
            if seen[node]:
                return True
            seen[node] = True
            for neighbor in adj_map[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    return True
            return False

        for node1, node2 in edges:
            adj_map[node1].append(node2)
            adj_map[node2].append(node1)
            seen = [False] * (n + 1)
            if dfs(node1, -1):
                return [node1, node2]
        return []
