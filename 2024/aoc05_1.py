#!/usr/bin/python3

import sys

rules, updates = sys.stdin.read().strip().split("\n\n")

total = 0

rulesd = {}
for rule in rules.split("\n"):
    a = int(rule.split("|")[0])
    b = int(rule.split("|")[1])
    rulesd.setdefault(a, []).append(b)

for update in updates.split("\n"):
    pages = update.split(",")
    good = True
    for x in range(len(pages)):
        if int(pages[x]) in rulesd.keys():
            checkif = all(int(item) in rulesd[int(pages[x])] for item in pages[x+1:])
            if not checkif:
                good = False
                break

            checkif = any(int(item) in rulesd[int(pages[x])] for item in pages[:x])
            if checkif:
                good = False
                break

    if good:
        total += int(pages[len(pages) // 2])

print(total)