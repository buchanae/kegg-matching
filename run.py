#!/usr/bin/env python

import os
import re
import sqlite3
from jinja2 import Environment, FileSystemLoader, Template

KEGG_DIR = './keggs/'
files = [KEGG_DIR + f for f in os.listdir(KEGG_DIR)]

env = Environment(loader=FileSystemLoader('./templates/'))
template = env.get_template('table.html')

rx = re.compile(r"(\w+)~(([a-zA-Z0-9]+)_(\w+))(?:\t(\w+))?")

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("create table data (seq text, genome text, gene text, knum text)")

for file in files:
    f = open(file)
    for line in f:
        m = rx.match(line)
        c.execute("insert into data values (?, ?, ?, ?)", (m.group(1), m.group(3), m.group(2), m.group(4)))


res = c.execute("select knum, group_concat(distinct genome), group_concat(distinct gene) from data group by knum")
print template.render(rows=res)
