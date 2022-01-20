#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def recursion(arr, num):
    if num <= 1:
        return arr[0]
    else:
        arr1 = arr[0:len(arr) // 2]
        arr2 = arr[len(arr) // 2:len(arr)]
        res = int(recursion(arr1, len(arr1)))
        res += int(recursion(arr2, len(arr2)))
        return res


if __name__ == '__main__':
    arr = input('Введите числа через пробел: ')
    arr = arr.split()
    print(f'Sum = {recursion(arr, len(arr))}')