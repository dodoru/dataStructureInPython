class Node():
    def __init__(self, element=None, next=None, prev=None):
        self.element = element
        self.next = next
        self.prev = prev

    def __repr__(self):
        return repr(self.element)


class LinkedList():
    def __init__(self, tail=None, count=0):
        self.head = Node()
        self.tail = tail
        self.count = count

    def is_empty(self):  # O(1)
        return self.head.next is None

    def insert_after(self, item, node):  # O(n)
        temp_node = self.head
        insert_item = Node(item)
        if temp_node.next is None and node.element is None:
            temp_node.next = insert_item
            insert_item.prev = temp_node
            self.count += 1
            self.tail = insert_item
            return
        while temp_node.next is not None:
            temp_node = temp_node.next
            if temp_node is node:
                if node is self.tail:
                    self.tail = insert_item
                    node.next = insert_item
                    insert_item.prev = node
                else:
                    insert_item.prev = node
                    insert_item.next = node.next
                    node.next.prev = insert_item
                    node.next = insert_item
                self.count += 1
                return
        print("Can not find the node --- insert_after")

    def insert_before(self, item, node):  # O(n)
        temp_node = self.head
        insert_item = Node(item)
        if self.head.next is None and node.element is None:
            self.head.next = insert_item
            insert_item.prev = self.head
            self.tail = insert_item
            self.count += 1
            return
        while temp_node.next is not None:
            if temp_node.next is node:
                if temp_node is self.head:
                    insert_item.next = temp_node.next
                    temp_node.next.prev = insert_item
                    insert_item.prev = self.head
                    self.head.next = insert_item
                else:
                    insert_item.next = temp_node.next
                    insert_item.prev = temp_node
                    temp_node.next.prev = insert_item
                    temp_node.next = insert_item
                self.count += 1
                return
            temp_node = temp_node.next
        print("Can not find the node --- insert_before")

    def delete(self, element):  # O(n)
        temp_node = self.head.next
        while temp_node is not None:
            if temp_node.element == element:
                if temp_node == self.head.next and temp_node == self.tail:
                    self.head.next = None
                    self.tail = None
                elif temp_node == self.head.next:
                    self.head.next = temp_node.next
                    temp_node.next.prev = self.head
                elif temp_node == self.tail:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev
                else:
                    temp_node.prev.next = temp_node.next
                    temp_node.next.prev = temp_node.prev
                self.count -= 1
                return
            temp_node = temp_node.next
        print("Can not find the element --- delete(element)")

    def find(self, item):  # O(n)
        temp_node = self.head.next
        while temp_node is not None:
            if temp_node.element is item:
                return temp_node
            temp_node = temp_node.next
        return None

    def length(self):  # O(1)
        return self.count

    def first_node(self):  # O(1)
        if self.is_empty():
            print("The linked list is empty --- firstNode")
        else:
            return self.head.next

    def last_node(self):  # O(1)
        if self.is_empty():
            print("The linked list is empty --- lastNode")
        else:
            return self.tail

    def append(self, item):  # O(1)
        insert_item = Node(item)
        if self.is_empty():
            self.head.next = insert_item
            insert_item.prev = self.head
            self.tail = insert_item
            self.count += 1
        else:
            self.tail.next = insert_item
            insert_item.prev = self.tail
            self.tail = insert_item
            self.count += 1

    def reverse(self):  # O(n\2)
        front = self.head.next
        rear = self.tail
        if front is None:
            return
        if (self.length() % 2) == 1:
            while front is not rear:
                temp = front.element
                front.element = rear.element
                rear.element = temp
                front = front.next
                rear = rear.prev
        else:
            while front.next is not rear:
                temp = front.element
                front.element = rear.element
                rear.element = temp
                front = front.next
                rear = rear.prev
            temp = front.element
            front.element = rear.element
            rear.element = temp


def testNodeCreation():
    n = Node(element=10)
    assert n.element == 10


def testLinkedListInsert_after():
    testList = LinkedList()
    testList.insert_before(1, Node())
    assert testList.first_node().element == 1 and testList.last_node().element == 1
    testList.insert_after(2, testList.head.next)
    assert testList.first_node().element == 1 and testList.last_node().element == 2


def testLinkedListInsert_before():
    testList = LinkedList()
    testList.insert_before(1, Node())
    assert testList.first_node().element == 1 and testList.last_node().element == 1
    testList.insert_before(2, testList.head.next)
    assert testList.first_node().element == 2 and testList.last_node().element == 1


def testLinkedListFind():
    testList = LinkedList()
    testList.insert_before(1, Node())
    testList.insert_after(2, testList.head.next)
    assert testList.find(2) == testList.tail and testList.find(3) == None


def testLinkedListAppend():
    testList = LinkedList()
    testList.append(4)
    assert testList.first_node().element == 4 and testList.last_node().element == 4
    testList.append(5)
    assert testList.first_node().element == 4 and testList.last_node().element == 5


def testLinkedListReverse():
    testList = LinkedList()
    testList.insert_after(1, Node())
    testList.insert_after(2, testList.tail)
    testList.insert_after(3, testList.tail)
    testList.reverse()
    assert testList.first_node().element == 3 and testList.last_node().element == 1
    testList.insert_after(4, testList.tail)
    testList.reverse()
    assert testList.first_node().element == 4 and testList.last_node().element == 3 and \
           testList.first_node().next.element == 1 and testList.last_node().prev.element == 2


def testLinkedListLength():
    testList = LinkedList()
    testList.insert_before(1, Node())
    assert testList.length() == 1
    testList.insert_after(111, testList.head.next)
    assert testList.length() == 2


def testLinkedListDelete():
    testList = LinkedList()
    testList.insert_before(1, Node())
    testList.insert_after(2, testList.head.next)
    testList.delete(2)
    assert testList.first_node().element == 1 and testList.last_node().element == 1


def testLinkedListFirst_node():
    testList = LinkedList()
    testList.insert_before(1, Node())
    testList.insert_after(2, testList.head.next)
    assert testList.first_node() == testList.head.next


def testLinkedListLast_node():
    testList = LinkedList()
    testList.insert_before(1, Node())
    testList.insert_after(2, testList.head.next)
    assert testList.last_node() == testList.tail


def testLinkedListCreation():
    testLinkedListInsert_after()
    testLinkedListInsert_before()
    testLinkedListFind()
    testLinkedListLength()
    testLinkedListDelete()
    testLinkedListFirst_node()
    testLinkedListLast_node()
    testLinkedListAppend()
    testLinkedListReverse()


def test():
    testNodeCreation()
    testLinkedListCreation()
    print 1


if __name__ == '__main__':
    test()
