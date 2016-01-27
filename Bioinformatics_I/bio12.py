#!/usr/bin/env python
# __author__ = Di
#1 Implement pattern count

"""1: CODE CHALLENGE: Implement PatternCount (reproduced below).
     Input: Strings Text and Pattern.
     Output: Count(Text, Pattern)."""
def patterncount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i: i+len(pattern)] == pattern:
            count += 1
    return count

"""f = open('/Users/ar-di.sha/Desktop/dataset_2_6.txt', 'r')
lines = f.readlines()
text = lines[0].rstrip()
pattern = lines[1].rstrip()
print(patterncount(text, pattern))"""


"""2. CODE CHALLENGE: Solve the Frequent Words Problem.
      Input: A string Text and an integer k
      Output: All most frequent k-mers in Text.
      This algorithm runs in O(n^2)"""
def frequentword(text, k):
    frequentpattern = []
    count = [0] * (len(text)-k+1)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        count[i] = patterncount(text, pattern)
    maxCount = max(count)
    for i in range(len(text)-k+1):
        if count[i] == maxCount:
            frequentpattern.append(text[i:i+k])
    return set(frequentpattern)


f = open('/Users/ar-di.sha/Desktop/dataset_2_9.txt', 'r')
lines = f.readlines()
text = lines[0].rstrip()
k = int(lines[1].rstrip())
output = frequentword(text,k)
print(" ".join(map(str, output)))




