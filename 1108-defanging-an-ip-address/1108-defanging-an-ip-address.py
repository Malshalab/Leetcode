class Solution(object):
    def defangIPaddr(self, address):
        answer=address.replace(".","[.]")
        return(str(answer))
        """
        :type address: str
        :rtype: str
        """
        