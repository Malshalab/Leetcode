# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    

    def isPalindrome(self, head):
        current_node = head
        count=0
        reversedList=[]
     
        while current_node is not None:
            count = count + 1
            info=current_node.val
            reversedList.append(info)
            current_node = current_node.next
        
        return reversedList == reversedList[::-1]
            
    
           
        