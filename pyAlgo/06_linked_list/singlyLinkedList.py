"""
1) Insertion ,deletion, and search for singlely-linked list;
2) Assume int type for the data in list node
author  KAIXUAN
"""
from typing import Optional


class Node:
    def __init__(self, data: int, next_node=None):
        self.data = data
        self._next = next_node


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def find_by_value(self, value: int) -> Optional[Node]:
        p = self._head
        while p and p.data != value:
            p = p._next
        return p

    def find_by_index(self, index: int) -> Optional[Node]:
        p = self._head
        positon = 0
        while p and positon != index:
            p = p._next
            positon += 1
        return p

    def insert_value_to_head(self, value: int):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_node_to_head(self, node: Node):
        if node:
            node._next = self._head
            self._head = node

    def insert_new_node_after(self, node: Node, new_node: Node):
        if not node and not new_node:
            return
        new_node._next = node._next
        node._next = new_node

    def insert_value_after(self, value: int, node: Node):
        new_node = Node(value)
        self.insert_new_node_after(node, new_node)

    def insert_node_before(self, node: Node, new_node: Node):
        if not node or not new_node or not self._head:
            return
        if self._head == node:
            insert_node_to_head(new_node)
            return
        current = self._head
        while current._next and current._next != node:
            current = current._next
        if not current._next:
            return
        new_node._next = node
        current._next = new_node

    def insert_value_before_node(self, value: int, node: Node):
        new_node = Node(value)
        self.insert_node_before(node, new_node)

    def delete_by_node(self, node: Node):
        if not self._head or not node:
            return
        if node._next:
            node.data = node._next.data
            node._next = node._next._next
            return
        # node is the last one or not in the list
        current = self._head
        while current and current._next != node:
            current = current._next
        if not current:  # not in lsit
            return
        current._next = node._next

    def delete_by_value(self, value: int):
        if not self._head or not value:
            return
        dummy = Node(value + 1)
        dummy._next = self._head

        prev, current = dummy, self._head
        while current:
            if current.data != value:
                prev._next = current
                prev = prev._next
            current = current._next
        if prev._next:
            prev._next = None
        self._head = dummy._next

    def __repr__(self) -> str:
        nums = []
        current = self._head
        while current:
            nums.append(current.data)
            current = current._next
        return '->'.join(str(num) for num in nums)

    def __iter__(self):
        node = self._head
        while node:
            yield node.data
            node = node._next

    def print_all(self):
        current = self._head
        if current:
            print(f"{current.data}", end="")
            current = current._next
        while current:
            print(f"->{current.data}", end="")
            current = current._next
        print("\n", flush=True)

    def remove_nth_from_end(self, head: Node, n: int) -> Optional[Node]:
        # 删除倒数的第n个节点
        fast = head
        count = 0
        while count < n and fast:
            fast = fast._next
            count += 1
        if not fast and count < n:
            return head
        if not fast and count == n:
            return head._next

    def merge_sorted_list(self, l1: Node, l2: Node) -> Optional[Node]:
        if l1 and l2:
            p1, p2 = l1, l2
            dummy = Node(None)
            current = dummy

            while p1 and p2:
                if p1.data <= p2.data:
                    current._next = p1
                    p1 = p1._next
                else:
                    current._next = p2
                    p2 = p2._next
                current = current._next
            current._next = p1 if p1 else p2
            return dummy._next
        return l1 or l2

    def reverse(self, head: Node) -> Optional[Node]:
        reversed_head = None
        current = head
        while current:
            reversed_head, reversed_head._next, current = current, reversed_head, current._next
        return reversed_head


if __name__ == "__main__":
    l = SinglyLinkedList()
    for i in range(15):
        l.insert_value_to_head(i)

    node6 = l.find_by_value(6)
    node1 = l.find_by_index(1)
    node9 = l.find_by_value(9)
    l.insert_value_before_node(node9, 20)
    l.insert_value_before_node(node9, 16)
    l.insert_value_before_node(node9, 16)
    l.delete_by_value(16)
    node11 = l.find_by_index(3)
    l.delete_by_node(node11)
    l.delete_by_node(l._head)
    l.delete_by_value(13)
    print(l)
    for value in l:
        print(value)
