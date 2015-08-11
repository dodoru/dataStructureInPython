# coding:utf-8
from random import randint


def random_list(num):
    lst = []
    i = 0
    while i < num:
        list.append(randint(0, 250))
        i += 1
    return lst


def BubbleSort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            print lst[i], lst[j]
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                print lst
    return lst


def InsertSort(lst):
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[i]:
            j -= 1
        lst.insert(j, lst[i])
        lst.pop(i + 1)


def ShellSort(lst):
    pass


def MergeSort(lst):
    pass


def HeapSort(lst):
    pass


def QuickSort(lst):
    pass


def testBubbleSort():
    lst = random_list(4)
    print lst
    print BubbleSort(lst)
    print "*" * 10

    lst = random_list(6)
    print lst
    print BubbleSort(lst)

    lst = random_list(7)
    print lst
    print BubbleSort(lst)


if __name__ == '__main__':
    testBubbleSort()

