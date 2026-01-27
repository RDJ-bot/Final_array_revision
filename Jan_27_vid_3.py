# Finding missing element in an array (Brute Force)
arr = [1,2,4,5]
n = len(arr)
flag = False

for i in range(1,n+1):
    flag = False
    for j in range(n):
        if i == arr[j]:
            flag = True
            break
    if(flag == False):
        print(i)
        break


# Better solution
arr = [1,2,4,5]
n = 5
hashing = [0]*(n+1)

for i in range(len(arr)):
    hashing[arr[i]] += 1

for i in range(1,n):
    if hashing[i] == 0:
        print(i)


# Optimal
arr = [1,2,4,5]
n = 5
sums = 0

for i in range(len(arr)):
    sums += arr[i]
act = n*(n+1)//2

print(act-sums)

# Optimal
arr = [1,2,4,5]
n = 5
xor1 = xor2 = 0

for i in range(1,n+1):
    xor1 = xor1 ^ i

for i in range(n-1):
    xor2 = xor2 ^ arr[i]

print(xor1 ^ xor2)