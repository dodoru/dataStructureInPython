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


"""
解决n*m 所有的情况。
基本思路是，把它划分三份，左上角三角形的矩阵，中间平行四边形的矩阵，右下角三角形的矩阵。
"""


def create_array_nm(n, m):
    arr = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = randint(0, MAX_NUM)
    return arr


def diagonal_left_top(arr):
    '''
    :return 把左上角矩三角形的矩阵遍历出来放在 diag
    diag: 存取左上角的多维数列
    part: 每一次斜线取的数列
    i: 因为每次斜线的 点坐标（x,y） 的和为恒定值，依次递增
    j: 每次斜线都是从第一行开始取数的
    '''
    diag = []
    n = len(arr)
    m = len(arr[0])
    k = min(n, m)
    for i in range(k):
        part = []
        for j in range(i + 1):
            part.append(arr[j][i - j])
        diag.append(part)
    return diag


def diagonal_middle(arr):
    '''
    :return 当n!=m, 把遍历的中间的平行四边形矩阵内容（不包括左上角三角形的底边）遍历出来放在 diag
    diag: 存取左上角的多维数列
    part: 每一次斜线取的数列
    i: 因为每次斜线的 点坐标（x,y） 的和为恒定值，依次递增
    j: 每次斜线都是从第一行开始取数的
    '''
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


def diagonal_right_bottom(arr):
    '''
    :return 把右下角矩形遍历出来放在 diag
    diag: 存取右下角三角形矩阵的多维数列，当n=n,不包含左上角三角形
    part: 每一次斜线取的数列
    i: 因为每次斜线的 点坐标（x,y）的和为恒定值，依次递增
    j: 每次斜线都是从第2行开始取数的，因为第一行已经被左上角三角形矩阵或者中间平行四边形矩阵遍历过了。
    '''
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
        for i in range(m, m + n):
            part = []
            for j in range(i - m + 1, n):
                # fixme OK ,test ok
                part.append(arr[j][i - j])
            diag.append(part)
    return diag


def diagonal_snake(arr):
    left_top = diagonal_left_top(arr)
    middle = diagonal_middle(arr)
    right_bottom = diagonal_right_bottom(arr)
    return left_top + middle + right_bottom


def test_nm():
    a = create_array_nm(7, 3)
    # test (2,4)(3,4)(4,4)(5,4)(6,4)(7,4) etc OK
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
