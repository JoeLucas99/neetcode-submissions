class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Use HM to track letter count
        #Compare against k
        #If the difference between maxLett and length exceeds k then move l over, 
        #subtract l's c until difference gone

        l = 0 
        lettFreq = {}
        maxf = 0
        longest = 0

        for r in range(len(s)):
            lettFreq[s[r]] = lettFreq.get(s[r], 0) + 1
            maxf = max(maxf, lettFreq[s[r]])
            while (r - l + 1) - maxf > k:
                lettFreq[s[l]] = lettFreq.get(s[l]) - 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest