# You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
#
# Input
#
# The only input line contains a string of n characters.
#
# Output
#
# Print one integer: the length of the longest repetition.
#
# Constraints
# 1≤n≤106
# Example
#
# Input:
# ATTCGGGA
#
# Output:
# 3

seq = input()

max = 0
counter = 0

for i in range(0,len(seq)-1):
    if(seq[i]==seq[i+1]):
        counter += 1
    if(seq[i]!=seq[i+1]):
        if(counter>=max):
            max = counter
        counter = 0

if(counter>max):
    print(counter+1)
else:
    print(max+1)
