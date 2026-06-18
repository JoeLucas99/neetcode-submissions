class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Params: Seen set, cur_path sets, crs map HM, scehdule array
        #Fill the crs map hm
        #Create DFS to cehck in cur_path, seen, add, run on pre_req,check validitiy,
        # remv from path, add to seen, add to ouptut
        # Go through every crs, if false return [], else once done return schedule

        crs_map = defaultdict(list)
        seen, cur_path = set(), set()
        schedule = []

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
            schedule.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False: return []
        return schedule
