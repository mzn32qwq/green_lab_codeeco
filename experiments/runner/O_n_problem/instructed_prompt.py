#################################

# Instructed Prompt:

#################################

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        getting solution from llama3.1
        """

# Helper function to convert a list to a linked list
def list_to_linked_list(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Helper function to convert a linked list back to a list
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == '__main__':

    for i in range(1_000):

        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        head = list_to_linked_list(input_list)

        swapped_head = Solution().swapPairs(head)

        result_list = linked_list_to_list(swapped_head)
