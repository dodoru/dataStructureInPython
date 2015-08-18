# coding:utf-8

class Node():
    def __init__(self, element=None, prev=None, rear=None):
        self.element = element
        self.prev = prev
        self.rear = rear

    def __repr__(self):
        return repr(self.element)


class DoubleLinkedList():
    def __init__(self, tail=None, count=0):
        self.head = Node()
        self.tail = tail
        self.total = count

    def __repr__(self):
        description = ' DoubleLinkedList: '
        node = self.head.rear
        while node is not None:
            description += (' ' + repr(node.element))
            node = node.rear
        return description

    def is_empty(self):
        return self.head.rear is None
        # return self.total

    def append(self, element):
        node = Node(element=element)
        if self.is_empty():
            self.head.rear = node
            node.prev = self.head

            self.tail = node
            self.total += 1

        else:
            self.tail.rear = node
            node.prev = self.tail

            self.tail = node
            self.total += 1

    def find(self, element):
        index_node = self.head.rear
        while index_node:
            if index_node.element == element:
                return index_node
                # only returns the first node
            index_node = index_node.rear
        return None

    def pop_tail(self):
        tail_element = self.tail.element
        self.tail = self.tail.prev
        self.tail.rear = None
        self.total -= 1
        return tail_element

    def remove(self, element):
        index_node = self.find(element)
        if index_node:
            if index_node == self.tail:
                self.tail = self.tail.prev
                self.tail.rear = None
                self.total -= 1
            else:
                index_node.prev.rear = index_node.rear
                index_node.rear.prev = index_node.prev
                self.total -= 1
        else:
            print (" no such element")


    # delete every node while node.element==element
    def deletes(self, element):
        index_node = self.head.rear
        while index_node:
            if index_node.element == element:
                if index_node == self.tail:
                    self.tail = self.tail.prev
                    self.tail.rear = None
                    self.total -= 1
                else:
                    index_node.prev.rear = index_node.rear
                    index_node.rear.prev = index_node.prev
                    self.total -= 1
            index_node = index_node.rear


    def insert_after(self, index_element, insert_element):
        index_node = self.find(index_element)
        insert_node = Node(element=insert_element)
        if index_node:
            if index_node == self.tail:
                # self.append(insert_element)
                self.tail.rear = insert_node
                insert_node.prev = self.tail
                self.tail = insert_node
                self.total += 1
            else:
                insert_node.prev = index_node
                insert_node.rear = index_node.rear
                index_node.rear.prev = insert_node
                index_node.rear = insert_node
                self.total += 1
        else:
            print "can't find index_element."


    def insert_before(self, index_element, insert_element):
        insert_node = Node(element=insert_element)
        index_node = self.find(index_element)
        if index_node:
            insert_node.rear = index_node
            insert_node.prev = index_node.prev
            index_node.prev.rear = insert_node
            index_node.prev = insert_node
            self.total += 1
        else:
            print "can't find index_element. "


    def first_node(self):
        if self.is_empty():
            print("This is an empty double_linked_list.")
        else:
            return self.head.rear


    def last_node(self):
        if self.is_empty():
            print("This is an empty double_linked_list.")
        else:
            return self.tail


    def count(self):
        return self.total

    # reverse the link , ok
    def reverse(self):
        if self.total > 1:
            index_node = self.tail.prev
            self.tail = Node(element=self.tail.element, prev=self.head, rear=None)
            self.head.rear = self.tail

            while index_node.prev:
                # print index_node
                #
                node = Node(element=index_node.element)
                self.tail.rear = node
                node.prev = self.tail
                self.tail = self.tail.rear
                index_node = index_node.prev

    # Fixme , why results null?
    def reverse2(self):
        if self.total > 1:
            index_node = Node(element=self.tail.element, prev=self.tail.prev, rear=self.head)
            self.head.rear = index_node
            while index_node.prev:
                print index_node
                index_node.prev, index_node.rear = index_node.rear, index_node.prev
                index_node = index_node.rear
            self.tail = index_node


    # this reverse3() is exchange the elements of front and the behind
    def reverse3(self):
        if self.total > 1:
            front = self.head.rear
            behind = self.tail
            index = self.total / 2
            for i in range(index):
                front.element, behind.element = behind.element, front.element
                front = front.rear
                behind = behind.prev


def test():
    l = DoubleLinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.append(5)
    l.append(4)
    l.append(6)
    l.append(4)
    print l
    l.remove(2)
    print l
    l.remove(4)
    print l
    l.deletes(1)
    print l
    l.deletes(5)
    print l
    l.deletes(4)
    print l
    l.insert_after(3, 1)
    l.insert_after(2, 1)
    print l
    l.insert_before(4, 1)
    l.insert_before(1, 4)
    print l
    # dl = l.reverse()
    l.reverse()
    print "reverse:", l
    l.reverse3()
    print "revers3() ,", l


if __name__ == "__main__":
    test()