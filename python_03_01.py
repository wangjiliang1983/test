#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tup = 4, 5, 6
print("tup = 4, 5, 6 is:",tup)

nested_tup = (4,5,6), (7,8)
print("nested_tup is", nested_tup)

tup = tuple([4,0,2])
print("new_tup is",tup)

tup_string = tuple('string')
print("tup string is", tup_string)
print("The tup_string[0] is", tup_string[0])

tup_append = tuple(['foo', [1,2], True])
print("tup_append is", tup_append)
tup_append[1].append(3)
print("tup_append is", tup_append)

seq = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in seq:
    print('a={0}, b={1},c={2}'.format(a,b,c))

a = (1,2,2,2,3,4,2)
print("a.count is",a.count(2))

a_list = [2,3,7,None]
tup_list = ('foo', 'bar', 'baz')
b_list = list(tup_list)
print(b_list)
b_list[1] = 'peekaboo'
print(b_list)
b_list.append('dwarf')
print(b_list)
b_list.insert(1,'red')
print(b_list)
b_list.pop(2)
print(b_list)
b_list.remove('foo')
print(b_list)

gen = range(10)
print(gen)
print("list gen is", list(gen))

some_list = ['foo', 'bar', 'baz']
mapping = {}
for i,v in enumerate(some_list):
    mapping[v] = i
print(mapping)

print('Sorted mapping is', sorted([7, 1, 2, 6, 0, 3, 2]))

seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)
print(list(zipped))
seq3 = [False, True]
print(list(zip(seq1, seq2, seq3)))
for i, (a,b) in enumerate(zip(seq1, seq2)):
    print('{0}: {1}, {2}'.format(i,a,b))

pitchers = [('Nolan', 'Ryan'), ('Roger', 'clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers)
print(first_names)
print(last_names)

print(list(reversed(range(10))))


empty_dict = {}
d1 = {'a' : 'Some value', 'b' : [1, 2, 3, 4]}
print(d1)

d1[7] = 'an integer'

print(d1)
print(d1['b'])

d1[5] = 'some value'
print(d1)
d1['dummy'] = 'another value'
print(d1)
del d1[5]
print(d1)
ret = d1.pop('dummy')
print(ret)
print(d1)
print(d1.keys())
print(list(d1.values()))