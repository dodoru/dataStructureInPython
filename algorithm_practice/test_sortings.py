# coding:utf-8

from sorting_algorithm import *


def test_BubbleSort():
    lst = random_list(4)
    print lst
    print BubbleSort(lst)

    lst = random_list(6)
    print lst
    print BubbleSort(lst)

    lst = random_list(7)
    print lst
    print BubbleSort(lst)


def test_InsertSort():
    lst = random_list(4)
    print lst
    print InsertSort(lst)
    print "*" * 15

    lst = random_list(5)
    print lst
    print InsertSort(lst)
    print "*" * 15

    lst = random_list(6)
    print lst
    print InsertSort(lst)
    print "*" * 15


def test_InsertSort2():
    lst = random_list(6)
    print lst
    print InsertSort2(lst)
    print "*" * 15

    lst = random_list(7)
    print lst
    print InsertSort2(lst)
    print "*" * 15

    lst = random_list(8)
    print lst
    print InsertSort2(lst)
    print "*" * 15


def test_ShellSort():
    lst = random_list(4)
    print lst
    print ShellSort(lst)
    print ShellSort2(lst)
    print "*" * 35

    lst = random_list(5)
    print lst
    print ShellSort(lst)
    print ShellSort2(lst)
    print "*" * 35

    lst = random_list(6)
    print lst
    print ShellSort(lst)
    print ShellSort2(lst)
    print "*" * 35

    lst = random_list(7)
    print lst
    print ShellSort(lst)
    print ShellSort2(lst)
    print "*" * 35


def test_MergeSort():
    lst = random_list(8)
    print lst
    print MergeSort(lst)
    print MergeSort2(lst)
    print "* " * 20

    lst = random_list(5)
    print lst
    print MergeSort(lst)
    print MergeSort2(lst)
    print "* " * 20

    lst = random_list(5)
    print lst
    print MergeSort(lst)
    print MergeSort2(lst)
    print "* " * 20

    lst = random_list(5)
    print lst
    print MergeSort(lst)
    print MergeSort2(lst)
    print "* " * 20


def test_QuickSort():
    lst = random_list(8)
    print lst
    print QuickSort(lst,0,7)
    print lst
    print "* " * 20

    lst = random_list(5)
    print lst
    print QuickSort(lst,0,4)
    print lst
    print "* " * 20

if __name__ == '__main__':
    # test_BubbleSort()
    # test_InsertSort2()
    # test_ShellSort()
    # test_MergeSort()
    test_QuickSort()
