class Solution(object):
    def minOperations(self, s):
        prev=None
        count =0
        for x in s:
            if(prev==x):
                count=count+1
                if(prev=="0"):
                    x="1"
                if(prev=="1"):
                    x="0"
            prev=x
        return min(count,len(s)-count)
        """
        :type s: str
        :rtype: int
        """
        