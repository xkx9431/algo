class Node():
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        '''
        node 节点的数据返回
        '''
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class SinglyLinkedList():
    def __init__(self):
        self.__head = None

    def find_by_value(self, value):
        node = self.__head
        while node != None and node.data != value:
            node = node.next
        return node

    def find_by_index(self, index):
        node = self.__head
        pos = 0
        while node != None and pos != index:
            node = node.next
            pos += 1
        return node

    def insert_to_head(self, value):
        node = Node(value)
        node.next = self.__head
        self.__head = node

    def insert_after(self, value, node):
        if node == None:
            return
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def insert_before(self, node, value):
        new_node = Node(value)
        if not self.__head or not node or not new_node:
            return

        if node == self.__head:
            self.insert_to_head(value)
            return

        cur = self.__head
        while cur.next and cur.next != node:
            cur = cur.next
        if not cur.next:
            return
        new_node.next = node
        cur.next = new_node

    def __iter__(self):
        node = self.__head
        while node:
            yield node.data
            node = node.next

    def delete_by_node(self, node):
        if not self.__head:
            return

        if self.__head == node:
            self.__head = node.next

        cur = self.__head
        while cur and cur.next != node:
            cur = cur.next
        if not cur:  # not fount node
            return
        cur.next = node.next

    def delete_by_value(self, value):
        node = self.find_by_value(value)
        self.delete_by_node(node)

    def delete_last_N_node(self, n):
        """
        删除链表中倒数第N个节点.
        主体思路：
            设置快、慢两个指针，快指针先行，慢指针不动；当快指针跨了N步以后，快、慢指针同时往链表尾部移动，
            当快指针到达链表尾部的时候，慢指针所指向的就是链表的倒数第N个节点
        参数:
            n:需要删除的倒数第N个序数
        """

        fast = slow = self.__head
        step = 1
        while step < n:
            fast = fast.next
            step += 1
        while fast.next != None:
            tmp = slow
            fast = fast.next
            slow = slow.next

        tmp.next = fast.next

    def find_mid_node(self):
        '''
        查找链表中的中间节点.
        主体思想:
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，则当快指针到达链表尾部的时候，慢指针指向链表的中间节点
        返回:
            node:链表的中间节点
        '''

        fast = slow = self.__head
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def create_node(self, value):
        '''创建一个存储value值的Node节点.
        参数:
            value:将要存储在Node节点中的数据
        返回:
            一个新的Node节点
        '''
        return Node(value)

    def print_all(self):
        node = self.__head
        if not node:
            print('list is empty')
        while node.next:
            print(str(node.data) + '-->', end='')
            node = node.next
        print(str(node.data))

    def has_ring(self):
        fast = slow = self.__head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False


def main():
    l = SinglyLinkedList()
    for i in range(10):
        l.insert_to_head(i)
    l.print_all()

    mid_node = l.find_mid_node()
    print(mid_node)

    node1 = l.find_by_value(1)
    l.insert_before(node1, 10)
    print('after insert 10 befor value = 1 node')
    l.print_all()

    l.delete_last_N_node(2)
    print('after  delete last 2 node')
    l.print_all()

    print(l.has_ring())

    ring_end = l.find_by_value(10)
    ring_start = l.find_by_index(1)
    ring_end.next = ring_start

    print("after  set  rings , the linked_list should be have ring ?/n")
    print(l.has_ring())


main()
