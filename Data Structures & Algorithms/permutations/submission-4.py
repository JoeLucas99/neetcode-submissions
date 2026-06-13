class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    per = perm.copy()
                    per.insert(i, num)
                    new_perms.append(per)
            perms = new_perms
        return perms