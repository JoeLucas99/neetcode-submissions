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


# Why does cntList = [[] for i in range(len(nums) + 1)] work and cntList = [[] for i in range(len(nums))]
# not work?
# What do the -1's mean in "for i in range(len(cntList) -1, -1, -1):"

#Space O(n) because were making a hm of len(nums) 
#Time O(n) becuase were always capped at loops the size of the input array
