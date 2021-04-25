t = int(input())
k = 0
vowel = ['a','e','i','o','u','A','E','I','O','U']
 
while (k != t):
    string1 = input()
    n = len(string1)
    count = 0
    arr = []
    for i in range(0,n):
        arr.append((n-i)*(i+1))
    for i in range(n):
        if string1[i] in vowel:
            count += arr[i]
    print(count)
    k  += 1