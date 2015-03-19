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
    def firstNodeValue(self):
        if self.isEmpty() is True:
            return None
        #return self.head 得到的是object 的地址
        else:
            return self.head.element
    #这段代码返回的是尾节点的值
    def lastNodeValue(self):
        if self.isEmpty() is True:
            return None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            return temp.element
    '''
    # 这段代码的返回的是首节点的对象地址
    def firstNode(self):
        return self.head

    # 这段代码返回的是尾节点的对象地址
    def lastNode(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        return temp

    # 在链表后面插入节点元素element
    def append(self,element):
        tempNode=linkNode(element,None)
        if self.isEmpty() is True:
            self.head=tempNode
        else:
            pointNode=self.lastNode()
            pointNode.next=tempNode

    # 判断链表中是否存在节点元素element
    def exist(self,element):
        if self.isEmpty() is True:
            print("Tip 1: Empty link and no element exist...")
            return  False
        else:
            pointNode=self.head
            while pointNode.element is not element:
                pointNode=pointNode.next
            return pointNode.element is element

     # 查找链表中是否存在节点元素element
    def find(self,element):
        if self.isEmpty() is True:
            print("Tip 2. Empty link and no element found...")
        else:
            pointNode=self.head
            while pointNode.element is not element:
                pointNode=pointNode.next
            if pointNode is not None:
                print("while nodeValue=element %r,the address of the node is %r "%(element, pointNode))
                return pointNode
            else:
                print("No Node value is element %r"%element)
                return None

    # 在指定的节点值的后面插入元素，但是当特定的节点值有重复，那么只在排在第一个的特定节点值后面插入元素
    def insertAfter(self,element,nodeValue):
        tempNode=linkNode(element,None)
        if self.isEmpty():
            print("Tip 3: Empty link no one after")
        else:
            pointNode=self.head
            while pointNode.element is not nodeValue:
                pointNode=pointNode.next
            # 应当判断是否list存在 nodeValue
            if pointNode is None:
                print("Tip 4 : there is no element(%r) in the list"%nodeValue)
            else:
                tempNode.next=pointNode.next
                #tempNode.next=pointNode.next.next 这样是错的
                pointNode.next=tempNode

    # 在指定的节点值的前面插入元素，但是当特定的节点值有重复，那么只在排在第一个的特定节点值前插入元素
    def insertBefore(self,element,nodeValue):
        tempNode=linkNode(element,None)
        if self.isEmpty():
            print("Tip 5 : Empty link no one before")
        elif self.head.element is nodeValue:
            tempNode.next=self.head
            self.head=tempNode
        else:
            pointNode=self.head
            while pointNode.next.element is not nodeValue:
                pointNode=pointNode.next
            # 应当判断是否list存在 nodeValue
            if pointNode is None:
                print("Tip 6 : there is no element(%r) in the list"%nodeValue)
            else:
                tempNode.next=pointNode.next
                pointNode.next=tempNode
    '''
    def insertAfter(self,element,nodeValue):
        tempNode=linkNode(element,None)
        if self.exist(nodeValue) is True:
            pointNode=self.head
            while pointNode.element is not nodeValue:
                pointNode=pointNode.next
            tempNode.next=pointNode.next
            pointNode.next=tempNode

    def insertBefore(self,element,nodeValue):
        tempNode=linkNode(element,None)
        if self.exist(nodeValue) is True:
            pointNode=self.head
            while pointNode.next.element is not nodeValue:
                pointNode=pointNode.next
            tempNode.next=pointNode.next
            pointNode.next=tempNode
    '''
    def delete(self,element):
        if self.isEmpty():
            print "Tip 7 : Empty link_list..."
        elif self.head.element is element:
            self.head=self.head.next
        else:
            pointNode=self.head
            while pointNode.next.element is not element:
                pointNode=pointNode.next
            pointNode.next=pointNode.next.next

    #
    def reverse(self):
        # return reversed(self) # 不能这样子
        if self.isEmpty() is True:
            print("Tip 8: Empty link list ...")
        else:
             # this is a silly way but still failed
            reversed_list=linklist()
            pointNode=self.head
            reversed_list.head=pointNode
            while pointNode.next is not None:
                reversed_list.insertBefore(pointNode.next.element,pointNode.element)
                pointNode=pointNode.next
            return reversed_list
        '''
            reversed_list=linklist()
            pointNode=self.head
            reversed_list.head=pointNode
            while pointNode.next is not None:
                reversed_list.head.element=pointNode.element
                pointNode=pointNode.next
                reversed_list.head=pointNode
            return reversed_list
        '''
        '''
            tempNode=reversed_list.head
            pointNode=self.head
            while pointNode.next is not None:
                tempNode.element=pointNode.element
                pointNode=pointNode.next
                tempNode.next=pointNode
            reversed_list.head=tempNode
            return reversed_list
        '''

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

# test use case

def test_firstNode():
    link=linklist()
    # print("the first Node : %r" %(link.firstNode()))
    link.append(1)
    print("the last Node's element: %r" %(link.firstNode()))

def test_lastNode():
    link=linklist()
    # print("the last Node : %r" %(link.lastNode()))
    link.append(2)
    print("the last node's element : %r" %(link.firstNode()).element)

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

    link.show()  # test linklist.show()
    link.count() # test linklist.count()

def test_isEmpty():
    link=linklist()
    assert link.isEmpty() is True
    link.append(1)
    assert link.isEmpty() is False
    link.delete(1)
    assert link.isEmpty() is True

def test_all():
    link=linklist()
    print(link.isEmpty())
    node=linkNode(1,None)
    link.head=node

    print(link.isEmpty())
    link.delete(1)
    print(link.isEmpty())
    link.append(1)
    link.insertBefore(2,1)
    link.show()


    print(link.isEmpty())
    link.insertBefore(3,1) #
    link.insertBefore(5,2)
    link.show()

    print(link.isEmpty())
    link.insertAfter(3,2)
    link.show()
    print("the first node's element : %r" %(link.firstNode()).element)
    print("the last node's element : %r" %(link.lastNode()).element)

    print(link.isEmpty())
    link.insertAfter(4,3)
    link.delete(2)
    link.show()
    print("the first node's element : %r" %(link.firstNode()).element)
    print("the last node's element : %r" %(link.lastNode()).element)
    link.count()

    link.reverse()
    link.show()

def test():
    test_append()
    test_exist()
    test_firstNode()
    test_lastNode()
    test_isEmpty()
    test_all()


if __name__ =='__main__':
    test()
