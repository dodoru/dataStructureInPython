# -*- coding:utf-8 -*-
class linkNode(object):
    def __init__(self,element=None,next=None):
        self.element=element
        self.next=next

class linklist():
    def __init__(self):
        self.head=None

    def __repr__(self):
        description = ' '
        node = self
        while node is not None:
            description += (repr(node.element) + '  ')
            node = node.next
        return description

    def isEmpty(self):
        return self.head is None
        #return self.element is None and self.next is None

    def insertAfter(self,element,nodeValue):
        tempNode=linkNode(element,None)
        if self.isEmpty():
            print("Empty link no one after")
        else:#####################这段有问题
            pointNode=self.head
            while pointNode.element is not nodeValue:
                pointNode=pointNode.next
            tempNode.next=pointNode.next.next
            pointNode.next=tempNode

    def insertBefore(self,element,nodeValue):
        tempNode=linkNode(element,None)
        if self.isEmpty():
            print("Empty link no one before")
        elif self.head.element is nodeValue:
            tempNode.next=self.head
            self.head=tempNode
        else:#####################这段有问题
            pointNode=self.head
            while pointNode.next is not nodeValue:
                pointNode=pointNode.next
            tempNode.next=pointNode.next
            pointNode.next=tempNode

    def delete(self,element):
        if self.isEmpty():
            print "Empty link_list..."
        elif self.head.element is element:
            self.head=self.head.next
        else:
            pointNode=self.head
            while pointNode.next.element is not element:
                pointNode=pointNode.next
            pointNode.next=pointNode.next.next


    def count(self):
        num=0
        pointNode=self.head
        while pointNode is not None:
            pointNode=pointNode.next
            num+=1
        print("the length of linklist is %d "%num)
        return num

    def show(self):
        pointNode=self.head
        while pointNode is not None:
            print (pointNode.element)
            pointNode=pointNode.next


def test_isEmpty():
    link=linklist()
    print(link.isEmpty())
    node=linkNode(1,None)
    link.head=node
    print(link.isEmpty())
    link.insertBefore(2,1)
    link.show()
    print(link.isEmpty())
    #link.insertBefore(3,1)
    link.insertBefore(5,2)
    link.show()
    print(link.isEmpty())
    link.insertAfter(3,2)
    link.show()
    print(link.isEmpty())
    #link.insertAfter(4,3)
    link.delete(2)
    link.show()


#def test()
'''
    link=linkNode()
    print(link.isEmpty())


def test_case():
    link=linkNode()
    print(link.isEmpty())
    link.insert(1)
    for i in range(2,10):
        link.insert(i)
    link.show()
    link.delete(3)
    link.show()
    print(link.isEmpty())
'''
def test():
    test_isEmpty()
    #test_insert()

if __name__ =='__main__':
    test()

'''
E:\Python27\python.exe "E:/my document/python/linklist.py"
True
False
2
1
False
5
2
1
False
5
2
3
False
5
3

Process finished with exit code 0

'''
