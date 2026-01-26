#Move zeros to the end of the array
# Brute force
arr = [1,0,2,3,2,0,0,4,5,1]
n = len(arr)
temp = []

for i in range(n):
    if(arr[i] != 0):
        temp.append(arr[i])
for i in range(len(temp)):
    arr[i] = temp[i]
for i in range(len(temp),n):
    arr[i] = 0
print(arr)


# Optimal
arr = [1,0,2,3,2,0,0,4,5,1]
n = len(arr)
zero = 0

for i in range(n):
    if(arr[i] == 0):
        zero = i
        break
for j in range(zero+1,n):
    if(arr[j] != 0):
        arr[zero],arr[j] = arr[j],arr[zero]
        zero += 1

print(arr)


# Linear Search
arr = [1,2,4,5,6,7,8,9,10,4567,67,45,35]
target = 45
for i in range(len(arr)):
    if(arr[i] == target):
        print("Found")
        break

 
# Union of two sorted arrays
arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5,6]

s = set()

for i in arr1:
    s.add(i)

for j in arr2:
    s.add(j)

union = [0]*len(s)
j = 0
for i in s:
    union[j] = i
    j += 1
print(union)


# Optimal
arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5,6]

n = len(arr1)
m = len(arr2)
res = []
i = j = 0

while i<n and j<m:

    if arr1[i] == arr2[j]:
        if not res or res[-1] != arr1[i]:
            res.append(arr1[i])
        j += 1
        i += 1

    elif arr1[i]<arr2[j]:
        if not res or res[-1] != arr1[i]:
            res.append(arr1[i])
        i+=1
    
    else:
        if not res or res[-1] != arr2[j]:
            res.append(arr2[j])
        j+=1

while i < n:
    if not res or res[-1] != arr1[i]:
        res.append(arr1[i])
    i+=1

while j < m:
    if not res or res[-1] != arr2[j]:
        res.append(arr2[j])
    j += 1

print(res)



# Intersection
arr1 = 