# coding:utf-8

class Node():
    def __init__(self,element=None,prev=None,rear=None):
        self.element=element
        self.prev=prev
        self.rear=rear

    def __repr__(self):
        return repr(self.element)

class DoubleLinkedList():
    def __init__(self,tail=None,count=0):
        self.head=Node()
        self.tail=tail
        self.total=count

    def __repr__(self):
        pass


    def is_empty(self):
        return self.head.rear is Node
        # return self.total

    def append(self,element):
        node=Node(element=element)
        if self.is_empty():
            self.head.next=node
            node.prev=self.head

            self.tail=node
            self.total+=1

        else:
            self.tail.next=node
            node.prev=self.tail

            self.tail=node
            self.total+=1


    def insert_after(self):
        pass

    def insert_before(self):
        pass

    def delete(self):
        pass

    def find(self):
        pass

    def count(self):
        pass

    def first_node(self):
        pass

    def last_node(self):
        pass

