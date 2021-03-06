#!/usr/bin/env python
# coding=utf-8

from hooky import List


class MyList(List):
    def _before_add(self, key, item):
        print('before add, key: {}, item: {}'.format(key, repr(item)))

    def _after_add(self, key, item):
        print(' after add, key: {}, item: {}'.format(key, repr(item)))

    def _before_del(self, key, item):
        print('before_del, key: {}, item: {}'.format(key, repr(self[key])))

    def _after_del(self, key, item):
        print(' after_del, key: ', key)


l = MyList(['a', 'b'])

l.append(1)

l.extend(['f', 'g', 2])

l.pop()

l[2:3] = ['c', 'd', 'e']

print(l)

l.clear()

print(l)
