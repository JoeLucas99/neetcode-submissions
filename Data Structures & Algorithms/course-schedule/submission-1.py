class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Make a HM to store all crs pre_req pairs and set to keep track of cur_pre_reqs
        #Make DFS to check off all pairs for cycle, return bool and rmv pre_reqs
        #Run DFS

        crs_map = defaultdict(list)
        seen = set()

        for crs, pre in prerequisites:
            crs_map[crs].append(pre)

        def dfs(crs):
            if crs in seen:
                return False
            if len(crs_map[crs]) == 0:
                return True
            seen.add(crs)
            for pre_preq in crs_map[crs]:
                if not dfs(pre_preq):
                    return False
            seen.remove(crs)
            crs_map[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
            