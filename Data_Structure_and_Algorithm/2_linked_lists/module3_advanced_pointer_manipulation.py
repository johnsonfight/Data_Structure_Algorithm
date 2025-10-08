"""
Module 3: Advanced Pointer Manipulation - Interactive Practice
===============================================================

Master merging, partitioning, and complex node operations!

Key Problems:
- LC 21: Merge Two Sorted Lists
- LC 23: Merge k Sorted Lists
- LC 19: Remove Nth Node From End
- LC 83: Remove Duplicates from Sorted List
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    """
    LC 21: Merge Two Sorted Lists

    Merge two sorted lists into one sorted list.

    Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
    """
    # TODO: Use dummy node, compare values, link nodes
    pass

def mergeKLists(lists):
    """
    LC 23: Merge k Sorted Lists

    Merge k sorted lists using min-heap.

    Example:
    Input: [[1,4,5],[1,3,4],[2,6]]
    Output: 1->1->2->3->4->4->5->6
    """
    # TODO: Use heap to track smallest nodes
    pass

def removeNthFromEnd(head, n):
    """
    LC 19: Remove Nth Node From End of List

    Remove nth node from end in one pass.

    Example:
    Input: 1->2->3->4->5, n = 2
    Output: 1->2->3->5
    """
    # TODO: Two pointers with n gap, dummy node
    pass

def deleteDuplicates(head):
    """
    LC 83: Remove Duplicates from Sorted List

    Delete duplicates in sorted list.

    Example:
    Input: 1->1->2->3->3
    Output: 1->2->3
    """
    # TODO: Compare current with next, skip duplicates
    pass

if __name__ == "__main__":
    print("Module 3: Advanced Pointer Manipulation")
    print("Focus on: Merging, partitioning, nth from end")
