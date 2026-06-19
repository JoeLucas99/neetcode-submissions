class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Make a HM to store all crs pre_req pairs and set to keep track of cur_pre_reqs
        #Make DFS to check off all pairs for cycle, return bool and rmv pre_reqs
        #Run DFS

        seen, cur_path = set(), set()
        course_map = defaultdict(list)

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
            return True
        
        for course in range(numCourses):
            if dfs(course) == False: return False
        return True