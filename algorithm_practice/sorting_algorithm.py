# coding:utf-8
from random import randint



def random_list(num):
    list=[]
    i=0
    while i<num:
        list.append(randint(0,250))
        i+=1
    return list

def BubbleSort(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            print list[i],list[j]
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
    return list

def InsertSort(list):
    pass

def ShellSort(list):
    pass

def MergeSort(list):
    pass

def HeapSort(list):
    pass

def QuickSort(list):
    pass

def testBubbleSort():
    lst=random_list(4)
    print lst
    print BubbleSort(lst)

    lst=random_list(6)
    print lst
    print BubbleSort(lst)

    lst=random_list(7)
    print lst
    print BubbleSort(lst)


if __name__=='__main__':
    testBubbleSort()
