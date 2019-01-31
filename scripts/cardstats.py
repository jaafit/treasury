#!/usr/bin/python

import csv

with open('../cards/civcitizen.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    provides = {}
    demands = {}
    prevAge = 'I'

    for row in reader:
        if row['age*'] != prevAge:
            print "\nAge ",prevAge
            print 'Provides:',
            for p in provides:
                print "(%s: %s)"%(p, provides[p]),
            print
            print "Demands:",
            for d in demands:
                print "(%s: %s)"%(d, demands[d]),
            print
        prevAge = row['age*']

        for p in ['provides1*=blank', 'provides2*=blank', 'provides3*=blank']:
            if row[p]:
                provides.setdefault(row[p], 0)
                provides[row[p]] +=1
        demands.setdefault(row['demands=blank'], 0)
        demands[row['demands=blank']] += 1

