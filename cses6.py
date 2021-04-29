# A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:
#
# Your task is to find out the number in row y and column x.
#
# Input
#
# The first input line contains an integer t: the number of tests.
#
# After this, there are t lines, each containing integers y and x.
#
# Output
#
# For each test, print the number in row y and column x.
#
# Constraints
# 1≤t≤105
# 1≤y,x≤109
# Example
#
# Input:
# 3
# 2 3
# 1 1
# 4 2
#
# Output:
# 8
# 1
# 15

t = int(input())
n=0
arr = [0] * t

while(n!=t):
    ent = input()
    arr[n] = ent.split()
    n+=1

for a in arr:
    y = int(a[0])
    x = int(a[1])

    if (y>x and y%2 == 0):
        answer = y * y - (x) +1
        print(answer)
    if (y>x and y%2 == 1):
        answer = (y-1) * (y-1) + (x)
        print(answer)

    if(x>y and x%2 == 1):
        answer = (x * x) - (y) +1
        print(answer)

    if(x>y and x%2 == 0):
        answer = (x-1) * (x-1) + (y)
        print(answer)

    if (x==y):
        answer = (x-1) * (x-1) + (y)
        print(answer)
