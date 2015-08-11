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
        description=' DoubleLinkedList: '
        node=self.head.rear
        while node:
            description+=(''+repr(node.element))
            node=node.rear
        return description

    def is_empty(self):
        # return self.head.rear is None
        return self.total

    def append(self, element):
        node = Node(element=element)
        if self.is_empty():
            self.head.next = node
            node.prev = self.head

            self.tail = node
            self.total += 1

        else:
            self.tail.next = node
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

    # delete every node while node.element==element
    def delete(self, element):
        if self.tail.element == element:
            self.tail = self.tail.prev
            self.tail.rear = None
            self.total -= 1
        else:
            index_node = self.head.rear
            while index_node:
                if index_node.element == element:
                    index_node.prev.rear = index_node.rear
                    index_node.rear.prev = index_node.prev
                    self.total -= 1
                    # if return , only delete one, else delete all.
                else:
                    index_node = index_node.rear

    # remove only the first node while node.element==element
    def remove(self, element):
        if self.tail.element == element:
            self.tail = self.tail.prev
            self.tail.rear = None
            self.total -= 1
        else:
            index_node = self.find(element)
            if index_node:
                index_node.prev.rear = index_node.rear
                index_node.rear.prev = index_node.prev
                self.total -= 1
            else:
                print("no such element. ")

    def insert_after(self, index_element, insert_element):
        insert_node = Node(element=insert_element)
        if self.tail.element == index_element:
            self.tail.rear = insert_node
            insert_node.prev = self.tail
            self.tail = insert_node
        else:
            index_node = self.find(index_element)
            if index_node:
                insert_node.prev = index_node
                insert_node.rear = index_node.rear
                index_node.rear.prev = insert_node
                index_node.rear = insert_node
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
