#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_msg(ms):

    def printer(nm, fm):
        data = ms.format(n=nm, f=fm)
        return data
    return printer


if __name__ == '__main__':
    d = "dear {f} {n} you have done a great job"
    another = print_msg(d)
    print(another("Gloria", "Labron"))

