class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedNums = {}
        frequency = [[] for i in range(len(nums)+ 1)]

        for n in nums:
            sortedNums[n] = sortedNums.get(n, 0) + 1
        for key, value in sortedNums.items():
            frequency[value].append(key)
        
        results = []

        for i in range(len(frequency) -1, 0, -1):
            for number in frequency[i]:
                results.append(number)
            if len(results) == k:
                return results


        

