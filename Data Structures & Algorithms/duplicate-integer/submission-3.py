#Given an array of nums, return true if there are duplcicates. 
# Flase if none.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupset = set() #Create new set. To store vals from Nums.

        for i in nums: #Iterate through nums
           
            if i in dupset: 
                return True
  #If i is alr in the dupset then return true.
    # Bc a dup has been found.              
            dupset.add(i) 
            #If not, for every i add it to the dupset.
        return False
        #Return false if you get through the whole array and 
        # don't encounter any dups in the dupset.