# A simple Implementation of Linked List


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class List(object):

    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        repr_str, node = '', self.head
        while node:
            repr_str += str(node) + ' -> '
            node = node.next
        return repr_str + 'None'

    def insert(self, value):
        """ Insert a node to the end of list """
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)
        return self

    def insertAt(self, value, k):
        """ Insert a value at k position """
        if k < 0:
            raise Exception('Insert position should not be negative')
        if self.head is None and k > 0:
            raise Exception('Position k: ({}) out pf range'.format(k))
        if k == 0:
            if self.head is None:
                self.head = Node(value)
                return self
            if self.head is not None:
                node = Node(value)
                node.next = self.head
                self.head = node
                return self
        node, i = self.head, 0
        while i < k-1:
            i += 1
            node = node.next
            if node is None:
                raise Exception('Position k: ({}) out pf range'.format(k))
        next = node.next
        node.next = Node(value)
        node.next.next = next
        return self

    def deleteAt(self, k):
        """ Delete a node at index k """
        if self.head is None:
            raise Exception('Empty list')
        if k < 0:
            raise Exception('Delete position can not be negative')
        if k == 0:
            self.head = self.head.next
            return self
        i, node = 0, self.head
        while i < k-1:
            node = node.next
            i += 1
            if node.next is None:
                raise Exception('Position k: ({}) out of range'.format(k))
        if node.next is None:
            raise Exception('Position k: ({}) out of range'.format(k))
        node.next = node.next.next
        return self

    def delete(self, value):
        """ Delete the first node with value """
        if self.head is None:
            return self
        if self.head.value == value:
            self.head = self.head.next
            return self
        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return self
            node = node.next
            if node is None:
                break
        return self

    def deleteAll(self, value):
        """ Delete all nodes with the value in list """
        if self.head is None:
            return self
        while self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                return self
        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
            else:
                node = node.next
            if node is None:
                return self
        return self

    def reverse(self):
        """ Reverse the list """
        if self.head is None:
            return self
        pre, cur = None, self.head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        self.head = pre
        return self
