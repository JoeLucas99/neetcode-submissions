class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       ## dict
      ##  put the nums in val and key is how ofte they appear
      ##  An arr of arr len of dict
      ##  ind = amnt list add nums from dict
      ##  new arr
       ## read arr backwards
      ##  add to new arr
       ##  when len of new arr = k return new arr


        numMap = {}
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)
        
        amntMap = [[] for i in range(len(nums) + 1)]
        for num, amnt in numMap.items():
            amntMap[amnt].append(num)
        
        res = []
        for i in range(len(amntMap) -1, -1, -1):
            for num in amntMap[i]:
                res.append(num)
                if len(res) == k:
                    return res
        