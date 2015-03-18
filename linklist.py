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

    ''' #这段代码的返回的是首节点的值
    def firstNode(self):
        if self.isEmpty() is True:
            return None
        #return self.head 得到的是object 的地址
        else:
            return self.head.element
    #这段代码返回的是尾节点的值
    def lastNode(self):
        if self.isEmpty() is True:
            return None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            return temp.element
    '''
    #这段代码的返回的是首节点的对象地址
    def firstNode(self):
        return self.head

    #这段代码返回的是尾节点的对象地址
    def lastNode(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        return temp

    #在链表后面插入节点元素element
    def append(self,element):
        tempNode=linkNode(element,None)
        if self.isEmpty() is True:
            self.head=tempNode
        else:
            pointNode=self.lastNode()
            pointNode.next=tempNode

    #查找链表中是否存在节点元素element
    def exist(self,element):
        if self.isEmpty() is True:
            print("Empty link")
            return  False
        else:
            pointNode=self.head
            while pointNode.element is not element:
                pointNode=pointNode.next
            return pointNode.element is element
    '''
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
    '''
    def insertAfter(self,element,nodeValue):
        tempNode=linkNode(element,None)
        if self.exist(nodeValue) is True:
            pointNode=self.head
            while pointNode.element is not nodeValue:
                pointNode=pointNode.next
            tempNode.next=pointNode.next.next
            pointNode.next=tempNode

    def insertBefore(self,element,nodeValue):
        tempNode=linkNode(element,None)
        if self.exist(nodeValue) is True:
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
        if self.isEmpty() is True:
            print("The link list is empty...")
        else:
            pointNode=self.head
            print("Show the link list:")
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
    print("the first Node : %r" %(link.firstNode()).element)
    print("the last Node : %r" %(link.lastNode()).element)

def test_firstNode():
    link=linklist()
    print("the first Node : %r" %(link.firstNode()))

def test_lastNode():
    link=linklist()
    print("the last Node : %r" %(link.lastNode()))

def test_exist():
    link=linklist()
    assert link.exist(1) is False
    link.append(1)
    assert link.exist(1) is True
    link.append(2)
    link.append(3)
    link.show()
    assert link.exist(2) is True
    assert link.exist(3) is True

def test_append():
    link=linklist()
    link.append(2)
    link.append(3)
    link.append(None)
    link.append('sd')
    #print "show the link_list : "
    link.show()
    link.count()

def test():

    #test_firstNode()
    #test_lastNode()
    test_append()
    test_exist()
    #test_isEmpty()


if __name__ =='__main__':
    test()
