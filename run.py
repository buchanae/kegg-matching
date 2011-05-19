#!/usr/bin/env python

import re
import sqlite3

FILES = ("USDA207_KEGG.txt", "USDA257_KEGG.txt")

rx = re.compile(r"(\w+)~(([a-zA-Z0-9]+)_(\w+))(?:\t(\w+))?")

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("create table data (seq text, genome text, gene text, knum text)")

for file in FILES:
    f = open(file)
    for line in f:
        m = rx.match(line)
        c.execute("insert into data values (?, ?, ?, ?)", (m.group(1), m.group(3), m.group(2), m.group(4)))


res = c.execute("select knum, group_concat(distinct genome), group_concat(distinct gene) from data group by knum")
for r in res:
    print "{0} {1} {2}".format(r[0], r[1], r[2])
