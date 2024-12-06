#!/usr/bin/python3

import sys

def correct(pages):
    for x in range(len(pages)):
        if int(pages[x]) in rulesd.keys():
            checkif = all(int(item) in rulesd[int(pages[x])] for item in pages[x+1:])
            if not checkif:
                return False

            checkif = any(int(item) in rulesd[int(pages[x])] for item in pages[:x])
            if checkif:
                return False

    return True

def solve(pages):
    while(1):
        for x in range(1, len(pages)):
            if not int(pages[x]) in rulesd.keys():
                continue

            if any(int(item) in rulesd[int(pages[x])] for item in pages[:x]):
                pages[x], pages[x-1] = pages[x-1], pages[x]

            if correct(pages):
                return int(pages[len(pages) // 2])

rules, updates = sys.stdin.read().strip().split("\n\n")

total = 0

rulesd = {}
for rule in rules.split("\n"):
    a = int(rule.split("|")[0])
    b = int(rule.split("|")[1])
    rulesd.setdefault(a, []).append(b)

for update in updates.split("\n"):
    pages = update.split(",")
    if correct(pages): # Skip correct updates
        continue

    total += solve(pages)

print(total)