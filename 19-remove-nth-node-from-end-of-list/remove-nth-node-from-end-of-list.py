# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # curr=head
        # cur=head
        
        # l=0
        # while curr:
        #     l+=0
        #     curr=curr.next
        # node_to_remove=l-n

        # for i in range(node_to_remove):
        #     cur = cur.next
        
        # prev.next=cur.next

        # return head


        dummy = ListNode(0, head)  # Add dummy to handle edge cases (like removing head)
        cur = dummy
        curr = dummy
                                
        # Move 'curr' n+1 steps ahead
        for _ in range(n + 1):
            curr = curr.next
                                                                    
        # Move both 'cur' and 'curr' until 'curr' reaches the end
        while curr:
            cur = cur.next
            curr = curr.next
                                                                                                                    
        # Remove the nth node from the end
        cur.next = cur.next.next
        return dummy.next
        