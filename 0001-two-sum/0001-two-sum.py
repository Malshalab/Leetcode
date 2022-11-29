class Solution(object):
    def twoSum(self, nums, target):
        pointerOne=0
        pointerTwo=len(nums)-1
        
        while (pointerTwo>pointerOne):
            sum=nums[pointerOne]+nums[pointerTwo]
            if(sum==target):
                return [pointerOne,pointerTwo]
            pointerTwo-=1
            if (pointerTwo==pointerOne):
                pointerOne+=1
                pointerTwo=len(nums)-1
         
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        