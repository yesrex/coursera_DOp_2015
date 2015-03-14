#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def detail(items,DPtable,K,n):
    if n==0:
        return []
    if DPtable[n][K] > DPtable[n-1][K]:
        return detail(items,DPtable,K-items[n-1].weight,n-1)+[1]
    else:
        return detail(items,DPtable,K,n-1)+[0]

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)
    DPtable = [[0]*(capacity+1)]
    for item in items:
        buf = []
        for i in range(capacity+1):
            if i < item.weight:
                buf.append(DPtable[item.index][i])
            else:
                buf.append( max( (DPtable[item.index][i-item.weight] + item.value), DPtable[item.index][i]))
        DPtable.append(buf)
    #print DPtable
    #taken = detail(items,DPtable,capacity,len(items))
    value = DPtable[-1][-1]
    tmpk=capacity
    for i in reversed(range(1,len(items)+1)):
        if DPtable[i][tmpk]>DPtable[i-1][tmpk]:
            tmpk = tmpk - items[i-1].weight
            taken[i-1]=1
        else: 
            taken[i-1]=0
            
    #print value
    """for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight"""
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

