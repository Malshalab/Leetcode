class Solution(object):
    def strStr(self, haystack, needle):
        
        if haystack.find(needle)!=-1:
            return haystack.index(needle)
        else:
            return(-1)