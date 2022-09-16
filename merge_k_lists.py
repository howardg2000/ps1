# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # The first node of the resulting list
    root = None
    # The last node of the current list
    tail = None
    while True:
        curr_min_node = None
        min_node_idx = -1
        for idx in range(len(lists)):
            curr_node = lists[idx]
            # Determine if this is the node with the lowest value so far
            if curr_node is not None and (curr_min_node is None or
                                          curr_node.val < curr_min_node.val):
                curr_min_node = curr_node
                min_node_idx = idx

        # No more nodes to add
        if curr_min_node is None:
            break
        if root is None:
            # Initialize head of list
            root = curr_min_node
            tail = root
        else:
            # Add to tail of list
            tail.next = curr_min_node
            tail = tail.next
        # Update the head the relevant list so we start at the next item of the linked list
        lists[min_node_idx] = curr_min_node.next

    return root


def transform_array_to_linked_list(array):
    """Transform a python array of ints to a linked list."""
    if array:
        head = ListNode(array[0])
        tail = head
        for num in array[1:]:
            tail.next = ListNode(num)
            tail = tail.next
        return head
    else:
        return None


def transform_linked_list_to_array(head):
    """Transform a linked list into a python array of ints."""
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


def test_merge_k_lists():
    """Test on test case [[1, 4, 5], [1, 3, 4], [2, 6]]
    Output: [1, 1, 2, 3, 4, 4, 5, 6]
    
    Explanation:
    Simple sorting of the concatenated list
    """
    arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
    linked_lists = [transform_array_to_linked_list(array) for array in arrays]
    result = merge_k_lists(linked_lists)
    print(transform_linked_list_to_array(result))


if __name__ == "__main__":
    test_merge_k_lists()
