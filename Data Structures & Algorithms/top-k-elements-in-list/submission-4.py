class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0 ) + 1

        occurence = [[] for i in range(len(nums) + 1)]
        for num, cnt in freq.items():
            occurence[cnt].append(num)
        
        res = []
        for i in range(len(occurence) -1, -1, -1):
            for num in occurence[i]:
                res.append(num)
                if len(res) == k:
                    return res


        
        