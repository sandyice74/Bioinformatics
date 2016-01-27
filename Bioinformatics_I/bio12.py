#!/usr/bin/env python
# __author__ = Di
#1 Implement pattern count


def patterncount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i: i+len(pattern)] == pattern:
            count += 1
    return count

f = open('/Users/ar-di.sha/Desktop/dataset_2_6.txt', 'r')
lines = f.readlines()
text = lines[0].rstrip()
pattern = lines[1].rstrip()
print(patterncount(text, pattern))

