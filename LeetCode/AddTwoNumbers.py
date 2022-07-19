# https://leetcode.com/problems/add-two-numbers/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = 0
        start = ListNode()
        current = start
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            new_node = ListNode((x + y + left) % 10)
            current.next = new_node
            current = new_node
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if x + y + left > 9:
                left = (x + y + left) // 10
            else:
                left = 0
        if left != 0:
            new_node = ListNode((left) % 10)
            current.next = new_node
        return start.next
            
            
            
        