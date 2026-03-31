class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sortedList = [[] for i in range(len(nums) + 1)]
        for num, amnt in freq.items():
            sortedList[amnt].append(num)
        
        res = []
        for i in range(len(sortedList) -1, -1, -1):
            for num in sortedList[i]:
                res.append(num)
                if len(res) == k:
                    return res