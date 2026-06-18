class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Make a HM to store all crs pre_req pairs and set to keep track of cur_pre_reqs
        #Make DFS to check off all pairs for cycle, return bool and rmv pre_reqs
        #Run DFS

        crs_map = defaultdict(list)
        cur_path, seen = set(), set()

        for crs, pre_req in prerequisites:
            crs_map[crs].append(pre_req)
        
        def dfs(crs):
            if crs in cur_path: return False
            if crs in seen: return True
            cur_path.add(crs)
            for pre_req in crs_map[crs]:
                if dfs(pre_req) == False: return False
            cur_path.remove(crs)
            seen.add(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False: return False
        return True
            