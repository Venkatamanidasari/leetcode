# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        tail=head
        count=1
        while tail.next:
            tail=tail.next
            count+=1
        k=k%count
        tail.next=head
        temp=head
        for i in range(count-k-1):
            temp=temp.next
        res=temp.next
        temp.next=None
        return res    




        
