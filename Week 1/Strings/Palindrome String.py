'''
Palindrome String
Given a string S, check if it is palindrome or not.

Input:
The first line contains 'T' denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line contains the length of the string and the second line contains the string S.

Output:
For each testcase, in a new line, print "Yes" if it is a palindrome else "No". (Without the double quotes)

Constraints:
1 <= T <= 30
1 <= N <= 100

Example:
Input:
1
4
abba
Output:
Yes
'''

#code
testcases = int(input())
for case in range(testcases):
    length = int(input())
    str_inp = input()
    pal = False
    for idx in range(length//2):
        if str_inp[idx] == str_inp[-(idx+1)]:
            pal = True
            continue
        else:
            pal = False
            break
    if pal:
        print("Yes")
    else:
        print("No")