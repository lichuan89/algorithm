#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""


class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, v): 
        self.stack.append(v)
        if self.min_stack == [] or v <= self.min_stack[-1]:
            self.min_stack.append(v)

    def pop(self):
        v = self.stack[-1]
        del self.stack[-1]
        if v == self.min_stack[-1]:
            del self.min_stack[-1]
        return v

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]

    def empty(self):
        return self.stack != []

if __name__ == "__main__":
    s = MinStack()
    s.push(5)
    print s.top(), s.min()
    s.push(3)
    print s.top(), s.min()
    s.push(3)
    print s.top(), s.min()
    s.push(6)
    print s.top(), s.min()
    s.push(2)
    print s.top(), s.min()
    s.pop()
    print s.top(), s.min()
    s.pop()
    print s.top(), s.min()
    s.pop()
    print s.top(), s.min()
    s.pop()
    print s.top(), s.min()
