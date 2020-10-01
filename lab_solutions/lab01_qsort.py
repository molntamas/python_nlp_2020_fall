#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Patrick Nanys <patrick.nanys@2000@gmail.com>
#
# Distributed under terms of the MIT license.


def swap(l, idx1, idx2):
    temp = l[idx1]
    l[idx1] = l[idx2]
    l[idx2] = temp


def qsort(l, start, end):
    if end-start <= 1:
        return
    pivot_idx = start
    pivot = l[pivot_idx]
    for i in range(start+1, end):
        current_idx = i
        if l[current_idx] < l[pivot_idx]:
            while current_idx > pivot_idx:
                swap(l, current_idx-1, current_idx)
                current_idx -= 1
            pivot_idx += 1
    qsort(l, 0, pivot_idx)
    if pivot_idx < len(l)-1:
        qsort(l, pivot_idx+1, end)


def main():
    l = [10, -1, 2, 11, 0]

    qsort(l, 0, len(l))

    assert (l == [-1, 0, 2, 10, 11])

    print("Tests passed.")


if __name__ == '__main__':
    main()
