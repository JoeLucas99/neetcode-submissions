class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        placement = [[] for i in range(len(nums) + 1)]
        for num, amnt in freq.items():
            placement[amnt].append(num)

        res = []
        for i in range(len(placement) -1, -1, -1):
            for num in placement[i]:
                res.append(num)
                if len(res) == k:
                    return res
        