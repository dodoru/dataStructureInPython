class Node():

    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    def __repr__(self):
        return repr(self.element)


class Stack():

    def __init__(self):
        self.head = Node()

    def __repr__(self):
        description = 'Stack:'
        node = self.head.next
        while node is not None:
            description += (' ' + repr(node.element))
            node = node.next
        return description

    def push(self, element):
        self.head.next = Node(element, self.head.next)

    def stack_empty(self):
        return self.head.next is None

    def pop(self):
        node = self.head.next
        if not self.stack_empty():
            self.head.next = node.next
        return node


def testStackEmpty():
    s = Stack()
    assert s.stack_empty() == True
    s.push(1)
    assert s.stack_empty() == False
    s.pop()
    assert s.stack_empty() == True


def testPush():
    s = Stack()
    s.push(1)
    assert s.head.next.element == 1
    s.push(2)
    assert s.head.next.element == 2 and s.head.next.next.element == 1


def testPop():
    s = Stack()
    s.push(1)
    assert s.pop().element == 1
    s.push(2)
    s.push(3)
    assert s.pop().element == 3


def testStackCreation():
    testStackEmpty()
    testPush()
    testPop()


def testNodeCreation():
    n = Node()
    assert n.element == None and n.next == None
    n.element = 3
    n.next = Node(4)
    assert n.next.element == 4 and n.element == 3


def test():
    testStackCreation()
    testNodeCreation()


if __name__ == '__main__':
    test()
