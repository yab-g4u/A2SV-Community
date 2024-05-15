# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = fast = head

        # Find the meeting point of slow and fast pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # If there is no cycle, return None
        if not fast or not fast.next:
            return None

        # Reset slow to the head and move both pointers one step at a time
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
