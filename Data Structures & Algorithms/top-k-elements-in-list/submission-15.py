class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntMap = {}
        for num in nums:
            cntMap[num] = cntMap.get(num, 0) + 1

        cntList = [[] for i in range(len(nums) + 1)]
        for num, cnt in cntMap.items():
            cntList[cnt].append(num)

        res = []
        for i in range(len(cntList) -1, -1, -1):
            for num in cntList[i]:
                res.append(num)
            if len(res) == k:
                return res


#HM where num:cnt
#List of len keys of empty lists
#Go through backwards and add to res list
#Return res list when len == k
        