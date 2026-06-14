"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph_copy = {None:None}
        
        def dfs(node):
            if node in graph_copy:
                return graph_copy[node]
            new_node = Node(val = node.val)
            graph_copy[node] = new_node
            for neigh in node.neighbors:
                new_node.neighbors.append(dfs(neigh))
            return new_node
        return dfs(node) if node else None