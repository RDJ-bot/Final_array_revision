# rotate an array to d-places (Brute - Force)
arr = [1,2,3,4,5,6,7,8,9]
k = 13
n = len(arr)
k = k % n

for i in range(k):
    temp = arr[0]
    for j in range(1,n):
        arr[j-1] = arr[j]
    arr[n-1] = temp

print(arr)


#better
arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
k = 3
temp = arr[:k]

for i in range(k,n):
    arr[i-k] = arr[i]
for i in range(n-k,n):
    arr[i] = temp[i-(n-k)]

print(arr)


# optimal
arr = [1,2,3,4,5,6,7,8,9]
k = 3
k = k%n
n = len(arr)

arr[:k] = arr[:k][::-1]
arr[k:] = arr[k:][::-1]
arr[:] = arr[:][::-1]

print(arr)



