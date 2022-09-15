# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    root = None
    tail = None
    while True:
        curr_min_node = None
        min_node_idx = -1
        for idx in range(len(lists)):
            curr_node = lists[idx]
            if curr_node is not None and curr_node.val < curr_min_node.val:
                curr_min_node = curr_node
                min_node_idx = idx

        if curr_min_node is None:
            break
        if root is None:
            root = curr_min_node
            tail = root
        else:
            tail.next = curr_min_node
            tail = tail.next
            lists[min_node_idx] = curr_min_node.next

    return root


def transform_array_to_linked_list(array):
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
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


def test_merge_k_lists():
    arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
    linked_lists = [transform_array_to_linked_list(array) for array in arrays]
    result = merge_k_lists(linked_lists)
    print(transform_linked_list_to_array(result))


if __name__ == "__main__":
    test_merge_k_lists()
