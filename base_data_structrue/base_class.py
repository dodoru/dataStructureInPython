# coding:utf-8

# test_super() todo: __metaclass__ super()

__metaclass__ = type  # super() 只能在新式类种起作用


class Bird():
    def __init__(self):
        self.hungery = True
        self.yahu = 'yahu'


class Duck(Bird):
    def __init__(self):
        super(Duck, self).__init__()
        # Bird.__init__(self)
        self.sound = 'gua'


def test1():
    a = Duck()
    print isinstance(a, Duck), a.sound, a.yahu
    print issubclass(Duck, Bird), Duck
    print issubclass(Bird, Duck), Duck


# todo __getattr__(self,name)
class Replay():
    def __getattr__(self, name):
        def play(*args):
            f = "{0}{1}".format(name, tuple(args))
            print(f)

        return play


def test2():
    a = Replay()
    a.fuck()
    a.fuck(2, 3, 4, 5)
    a.fuck(1, 23, 5, "silly billy")


# todo: __iter__可迭代 next()迭代器
class fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration
        return self.a

    def __iter__(self):
        return self


def test3():
    fib = fibs()
    print fib
    print list(fib)


if __name__ == '__main__':
    # test1()
    # test2()
    test3()



