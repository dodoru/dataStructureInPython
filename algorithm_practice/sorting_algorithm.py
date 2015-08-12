# coding:utf-8

from random import randint

MAXNUM=500

def random_list(num):
    list = []
    i = 0
    while i < num:
        list.append(randint(0, MAXNUM))
        i += 1
    return list


'''
冒泡排序：稳定，时间复杂度 O(n^2) 
冒泡排序方法是最简单的排序方法。
这种方法的基本思想是，将待排序的元素看作是竖着排列的“气泡”，较小的元素比较轻，从而要往上浮。
在冒泡排序算法中我们要对这个“气泡”序列处理若干遍。
一般地，第i遍处理时，不必检查第i高位置以上的元素，因为经过前面i-1遍的处理，它们已正确地排好序。  
'''


def BubbleSort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            print lst[i], lst[j]
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


'''
插入排序：稳定，时间复杂度 O(n^2)
经过i-1遍处理后,L[1..i-1]己排好序。第i遍处理仅将L[i]插入L[1..i-1]的适当位置，使得L[1..i] 又是排好序的序列。
要达到这个目的，我们可以用顺序比较的方法。
首先比较L[i]和L[i-1]，如果L[i-1]≤ L[i]，则L[1..i]已排好序，第i遍处理就结束了；
否则交换L[i]与L[i-1]的位置，继续比较L[i-1]和L[i-2]，直到找到某一个位置j(1≤j≤i-1)，使得L[j] ≤L[j+1]时为止。
'''


def InsertSort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        pos = i
        for j in range(i - 1, -1, -1):
            if lst[j] > temp:
                lst[j + 1] = lst[j]
                # print j,lst
                pos = j
        lst[pos] = temp
        # print i,lst
    return lst


def InsertSort2(lst):
    for i in range(1, len(lst)):
        pos = i
        for j in range(i - 1, -1, -1):
            if lst[j] > lst[i]:
                pos = j
        lst.insert(pos, lst[i])
        lst.pop(i + 1)
    return lst


'''
希尔排序：不稳定，时间复杂度 平均时间 O(nlogn) 最差时间O(n^s) 1<s<2 
在直接插入排序算法中，每次插入一个数，使有序序列只增加1个节点，并且对插入下一个数没有提供任何帮助。
如果比较相隔较远距离（称为 增量）的数，使得数移动时能跨过多个元素，则进行一次比较就可能消除多个元素交换。
算法先将要排序的一组数按某个增量d分成若干组，每组中记录的下标相差d.对每组中全部元素进行排序，
然后再用一个较小的增量对它进行，在每组中再进行排序。当增量减到1时，整个要排序的数被分成一组，排序完成。 
'''


def ShellSort(lst):
    distance = len(lst) / 2
    while distance > 0:
        for i in range(distance, len(lst)):
            temp = lst[i]
            j = i
            while j >= distance and temp < lst[j - distance]:
                lst[j] = lst[j - distance]
                # print 'j', j, lst
                j -= distance
            lst[j] = temp
            # print "temp:", temp, lst
        distance /= 2
        # print "distance:", distance, lst
    return lst


def ShellSort2(lst):
    distance = len(lst) / 2
    while distance > 0:
        for i in range(distance, len(lst)):
            pos = i
            for j in range(i + 1, len(lst), -distance):
                if lst[i] < lst[j]:
                    pos = j
            lst.insert(pos, lst[i])
            lst.pop(i + 1)
        distance /= 2
    return lst


def MergeSort(list):
    pass




def QuickSort(list):
    pass



'''
堆排序：不稳定，时间复杂度 O(n log n)
堆排序是一种树形选择排序，在排序过程中，将A[n]看成是完全二叉树的顺序存储结构，
利用完全二叉树中双亲结点和孩子结点之间的内在关系来选择最小的元素。

'''
def HeapSort(list):
    pass




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


if __name__ == '__main__':
    # test_BubbleSort()
    # test_InsertSort2()
    test_ShellSort()
