class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCnt = {}
        for num in nums:
            numCnt[num] = numCnt.get(num, 0) + 1
        bigNum, bigCnt = 0, 0
        for num, cnt in numCnt.items():
            if cnt > bigCnt:
                bigNum = num
                bigCnt = max(bigCnt, cnt)
        return bigNum