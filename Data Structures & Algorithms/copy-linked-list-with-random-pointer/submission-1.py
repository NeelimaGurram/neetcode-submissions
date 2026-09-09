"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newList={None : None}

        current=head
        while current:
            copy=Node(current.val)
            newList[current]=copy
            current=current.next

        current=head
        while current:
            copy=newList[current]
            copy.next=newList[current.next]
            copy.random=newList[current.random]
            current=current.next
        return newList[head]