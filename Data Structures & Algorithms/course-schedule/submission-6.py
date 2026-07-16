class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Make a HM to store all crs pre_req pairs and set to keep track of cur_pre_reqs
        #Make DFS to check off all pairs for cycle, return bool and rmv pre_reqs
        #Run DFS

        seen_set = set()
        crs_map = defaultdict(list)
        cur_path = set()

        for crs, prereq in prerequisites:
            crs_map[crs].append(prereq)

        def dfs(crs):
            if crs in seen_set: return True
            if crs in cur_path: return False
            cur_path.add(crs)
            for prereq in crs_map[crs]:
                if dfs(prereq) == False: return False
            cur_path.remove(crs)
            seen_set.add(crs)
        
        for crs in range(numCourses):
            if dfs(crs) == False: return False
        return True