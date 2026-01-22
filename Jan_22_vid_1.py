# largest number (brute force)
arr = [1,2,3,4,4,5,3,2,1,9,8,7]
n = len(arr)

for i in range(n):
    mini = i
    for j in range(i+1,n):
        if(arr[mini] > arr[j]):
            mini = j
    arr[mini],arr[i] = arr[i],arr[mini]

print(arr[n-1])


# optimal approach
arr = [1,2,3,4,4,5,3,2,1,9,8,7]
n = len(arr)
largest = arr[0]

for i in range(1,n):
    if(arr[i] > largest):
        largest = arr[i]

print(largest)



#second largest (brute-force approach)
arr = [1,2,3,4,4,5,3,2,1,9,8,9,7]
n = len(arr)

for i in range(n):
    mini = i
    for j in range(i,n):
        if(arr[mini] > arr[j]):
            mini = j
    arr[mini],arr[i] = arr[i],arr[mini]

largest = arr[n-1]
second = -1
for i in range(n-1,-1,-1):
    if(arr[i] != largest):
        second = arr[i]
        break

print(second)


# better solution
arr = [1,2,3,4,4,5,3,2,1,9,8,7]
n = len(arr)

largest = arr[0]
second = -1

for i in range(n):
    if(arr[i]>largest):
        largest = arr[i]

for i in range(n):
    if(arr[i] > second and arr[i] < largest):
        second = arr[i]

print(second)


# optimal approach
arr = [1,2,3,4,5,7,4,3,4,6,8,9,10,50,40,35]
n = len(arr)

largest = arr[0]
second = -1

for i in range(n):
    if(arr[i] > largest):
        second = largest
        largest = arr[i]
    elif(arr[i] > second and arr[i] < largest):
        second = arr[i]

print(largest)
print(second)



# Check if array is sorted
arr = [1,2,3,4,5,6,7,9,8]
n = len(arr)
flag = True

for i in range(1,n):
    if(arr[i] < arr[i-1]):
        flag = False
        break

if(flag):
    print("Sorted")
else:
    print("Not sorted")



# Remove duplicates in place from sorted array (brute force approach)
arr = [1,1,1,2,2,2,3,3,3]
s = set(arr)
index = 0

for i in s:
    arr[index] = i
    index += 1

print(index)
print(arr)


# optimal approach
arr = [1,1,1,2,2,3,3,3]
n = len(arr)

i = 0
for j in range(1,n):
    if(arr[i] != arr[j]):
        arr[i+1] = arr[j]
        i += 1

print(i+1)
print(arr)