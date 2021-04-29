# A permutation of integers 1,2,…,n is called beautiful if there are no adjacent elements whose difference is 1.
#
# Given n, construct a beautiful permutation if such a permutation exists.
#
# Input
#
# The only input line contains an integer n.
#
# Output
#
# Print a beautiful permutation of integers 1,2,…,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".
#
# Constraints
# 1≤n≤106
# Example 1
#
# Input:
# 5
#
# Output:
# 4 2 5 3 1
#
# Example 2
#
# Input:
# 3
#
# Output:
# NO SOLUTION


def main():

    n = int(input())
    arr = [None] * n
    count = 0

    if(n==1):
        print(1)

    if(n<4):
        print("NO SOLUTION")
        return

    for i in range(n-1,0,-2):
        arr[count] = i
        count += 1


    arr[n//2] = n
    count += 1

    if(n%2==1):
        for i in range(1,n-1,+2):
            arr[count] = i
            count +=1

    if(n%2==0):
        for i in range(2,n-1,+2):
            arr[count] = i
            count +=1

    for val in arr:
        print(val, end = " ")

if __name__ == '__main__':
    main()
