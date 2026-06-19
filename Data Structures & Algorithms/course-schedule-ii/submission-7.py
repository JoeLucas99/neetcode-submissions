class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Params: Seen set, cur_path sets, crs map HM, scehdule array
        #Fill the crs map hm
        #Create DFS to cehck in cur_path, seen, add, run on pre_req,check validitiy,
        # remv from path, add to seen, add to ouptut
        # Go through every crs, if false return [], else once done return schedule.

        seen, cur_path = set(), set()
        course_map = defaultdict(list)
        schedule = []

        for class1, class2 in prerequisites:
            course_map[class1].append(class2)

        def dfs(node):
            if node in cur_path:
                return False
            if node in seen:
                return True
            cur_path.add(node)
            for pre_req in course_map[node]:
                if dfs(pre_req) == False:
                    return False
            cur_path.remove(node)
            seen.add(node)
            schedule.append(node)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False: return []
        return schedule