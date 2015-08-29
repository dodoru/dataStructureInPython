# coding:utf-8
# 三大法宝： 头节点 多指针 删next
# 任何节点进来都用个头节点指向它  然后再删除查找都不需要特殊判断


class Node():
    def __init__(self, element=None, prev=None, next=None):
        self.element = element
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.element)


class DoubleLinkedList():
    def __init__(self, tail=None, count=0):
        self.head = None
        self.tail = tail
        self.total = count

    def __repr__(self):
        description = ' DoubleLinkedList: '
        node = self.head
        while node is not None:
            description += (' ' + repr(node.element))
            node = node.next
        return description

    def is_empty(self):
        return self.total == 0

    def append(self, element):
        node = Node(element=element)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.total += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.total += 1

    def find(self, element):
        index_node = self.head
        while index_node:
            if index_node.element == element:
                return index_node
            index_node = index_node.next
        return None

    def pop(self):
        if self.total == 0:
            return None
        elif self.total == 1:
            element = self.head
            self.head = None
            self.tail = None
            self.total -= 1
            return element
        else:
            element = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.total -= 1
            return element

    def remove(self, element):
        '''
        :param element: the first node which node.element==element
        :return : tips
        '''
        index_node = self.head
        while index_node:
            if index_node.element == element:
                self.total -= 1
                if index_node == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                if index_node == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    index_node.prev.next = index_node.next
                    index_node.next.prev = index_node.prev
                return "remove the first element values {0} successful".format(element)
            index_node = index_node.next
        return "no such element in the link."

    def deletes(self, element):
        '''
        :param element: delete nodes while node.element==element
        :return: self
        '''
        index_node = self.head
        while index_node:
            if index_node.element == element:
                self.total -= 1
                if index_node == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                elif index_node == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    index_node.prev.next = index_node.next
                    index_node.next.prev = index_node.prev
            index_node = index_node.next
            # return self

    def insert_after(self, pos_element, insert_element):
        index_node = self.head
        while index_node:
            if index_node.element == pos_element:
                self.total += 1
                node = Node(element=insert_element)
                if index_node == self.tail:
                    index_node.next = node
                    node.prev = index_node
                    self.tail = node
                else:
                    node.next = index_node.next
                    index_node.next.prev = node
                    index_node.next = node
                    node.prev = index_node
                return 'Insert OK. '
            index_node = index_node.next
        return "Can't find the position.no element values {0}".format(pos_element)

    def insert_before(self, pos_element, insert_element):
        index_node = self.tail
        while index_node:
            if index_node.element == pos_element:
                self.total += 1
                node = Node(element=insert_element)
                if index_node == self.head:
                    index_node.prev = node
                    node.next = index_node
                    self.head = node
                else:
                    node.prev = index_node.prev
                    index_node.prev.next = node
                    index_node.prev = node
                    node.next = index_node
                return 'Insert OK.'
            index_node = index_node.prev
        return "Can't find the position.no element values {0}".format(pos_element)

    def first_node_element(self):
        return self.head

    def last_node_element(self):
        return self.tail

    def count(self):
        return self.total

    '''
    @property
    def total(self):
        raise AttributeError("self.total can't be read.")
    '''

    def reverse(self):
        index_node = self.tail
        self.head = index_node
        while index_node:
            index_node.prev, index_node.next = index_node.next, index_node.prev
            self.tail = index_node
            index_node = index_node.next
            # self.tail=index.node : error,self.tail would be None


def test():
    l = DoubleLinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.append(5)
    l.append(4)
    # l.append(6)
    # l.append(4)
    print(l)
    print l.last_node_element()
    l.reverse()
    print("revers(): {}".format(l))
    print l.find(5)
    print l.find(6)
    print l.last_node_element()
    print l.pop()
    print l
    print l.remove(5)
    print l.deletes(4)
    print l.insert_before(2, 8)
    print l
    print l.insert_after(2, 7)
    print l
    print l.insert_before(5, 1)
    print l
    print l.insert_after(5, 1)
    print l
    b = DoubleLinkedList()
    b.append(1)
    b.append(2)
    print b
    b.reverse()
    print b


if __name__ == "__main__":
    test()