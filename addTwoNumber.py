#Definition for singly-linked list.
#class ListNode(Object):
#	def __init__(self, val=0, next=None):
#		self.val=val
#		self.next=next
class Solution:
    def addTwoNumbers(self, l1, l2):
        num1=0
        for i in range(len(l1)):
            num1+=l1[i]*10**(i)
        
        num2=0
        for i in range(len(l2)):
            num2+=l2[i]*10**(i)
        
        strResult=str(num1+num2)
        
        listResult=[]
        for i in range(len(strResult)):
            listResult.insert(0,strResult[i])
        
        print(listResult)

l1=[2,4,3]
l2=[5,6,4]
obj=Solution()
obj.addTwoNumbers(l1,l2)

