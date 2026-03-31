class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        numsList = [[] for i in range(len(nums) + 1)]
        for num, amnt in freq.items():
            numsList[amnt].append(num)
        
        res = []
        for i in range(len(numsList) -1, -1, -1):
            for num in numsList[i]:
                res.append(num)
                if len(res) == k:
                    return res
        