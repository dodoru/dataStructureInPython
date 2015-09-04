# coding:utf-8

'''
一个点阵，n*n

如何按对角线输出
'''
MAX_NUM = 20
from random import randint


def create_array_nn(n):
    arr = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = randint(0, MAX_NUM)
    return arr


def show_array(arr):
    for a in arr:
        print a


def print_line(arr):
    '''
    :return a[0][0],a[1][1],a[1][0]
    '''
    for i in range(len(arr)):
        for j in range(i, -1, -1):
            print j
            print arr[i][j]


def diagonal_nn(arr):
    '''
    :return a[0][0],a[0][1],a[1][0].....
    : a[y_pos][x_pos]
    '''
    # print left-top triangle
    diag = []
    for i in range(0, len(arr)):
        part = []
        for j in range(0, i + 1):
            # print arr[j][i - j]
            part.append(arr[j][i - j])
        diag.append(part)

    # print right-bottle triangle
    for i in range(len(arr), len(arr) * 2):
        part = []
        for j in range(i - len(arr) + 1, len(arr)):
            # print arr[j][i - j]
            part.append(arr[j][i - j])
        diag.append(part)
    return diag


def test_nn():
    a = create_array_nn(5)
    show_array(a)
    print "_" * 20

    b = diagonal_nn(a)
    show_array(b)
    print "_" * 20


############## n*n 测试正常 #################
def create_array_nm(n, m):
    arr = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = randint(0, MAX_NUM)
    return arr


def diagonal_left_top(arr):
    diag = []
    n = len(arr)
    m = len(arr[0])
    k = min(n, m)
    for i in range(k):
        part = []
        for j in range(i + 1):
            part.append(arr[j][i - j])
        diag.append(part)
    # diag.pop() # last value is []
    return diag


def diagonal_right_bottom(arr):
    diag = []
    n = len(arr)
    m = len(arr[0])
    if n > m:
        for i in range(n, m + n):
            part = []
            for j in range(i - m + 1, n):
                # print j, i - j
                part.append(arr[j][i - j])
            diag.append(part)
    else:
        for i in range(m, m + n - 1):
            part = []
            for j in range(i - n - 1, n):
                # fixme
                part.append(arr[j][i - j])
            diag.append(part)
    # diag.pop() # last is []
    return diag


def diagonal_middle(arr):
    diag = []
    n, m = len(arr), len(arr[0])
    mini, maxi = min(n, m), max(n, m)
    if n > m:
        for i in range(m, n):
            part = []
            for j in range(m - 1, -1, -1):
                part.append(arr[i - j][j])
            diag.append(part)
    else:
        for i in range(n, m):
            part = []
            for j in range(n):
                part.append(arr[j][i - j])
            diag.append(part)
    return diag


def diagonal_nm(arr):
    '''
    arr[n][m],n!=m
    :param arr: list of number matrix
    :return a[0][0],a[0][1],a[1][0]
    '''
    diag = []
    n = len(arr)
    m = len(arr[0])
    if n > m:
        for i in range(0, m):
            part = []
            for j in range(0, i + 1):
                # print arr[j][i-j]
                part.append(arr[j][i - j])
            diag.append(part)
        for i in range(m, n):
            part = []
            for j in range(m - 1, -1, -1):
                # print arr[i-j][j]
                part.append(arr[i - j][j])
            diag.append(part)

        diag += diagonal_right_bottom(arr)
    elif n == m:
        diag = diagonal_nn(arr)
    else:
        for i in range(0, n):
            for j in range(0, m - 1):
                print i, j
    return diag


def diagonal_snake(arr):
    left_top = diagonal_left_top(arr)
    middle = diagonal_middle(arr)
    right_bottom = diagonal_right_bottom(arr)
    return left_top + middle + right_bottom


def test_nm():
    
    # a = create_array_nm(8, 5) # n>m OK
    # a = create_array_nm(6, 8) # n<m & m-n=2 OK
    # a = create_array_nm(6, 9) # false Fixme
    a = create_array_nm(6, 8)
    show_array(a)
    print "_" * 30
    '''
    b = diagonal_nm(a)
    show_array(b)
    print "_" * 30
    c = diagonal_left_top(a)
    show_array(c)
    print "_" * 30
    c = diagonal_right_bottom(a)
    show_array(c)
    print "_" * 30
    '''
    s = diagonal_snake(a)
    show_array(s)


if __name__ == "__main__":
    # test_nn()  # OK
    test_nm()
