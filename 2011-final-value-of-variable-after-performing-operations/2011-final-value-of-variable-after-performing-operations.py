class Solution(object):
    def finalValueAfterOperations(self, operations):
        value=0
        for x in operations:
            if(x=="++X" or x=="X++"):
                value=value+1
            elif(x=="--X" or x=="X--"):
                value=value-1
        return value
        """
        :type operations: List[str]
        :rtype: int
        """
        