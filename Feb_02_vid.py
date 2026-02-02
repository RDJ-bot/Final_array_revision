#Majority element in  an array (Brute_Force)
arr = [2,2,3,3,1,2,2]
n = len(arr)
largest = arr[0]

for i in range(1,n):
    if(arr[i] > largest):
        largest = arr[i]

hashing = [0]*(largest+1)
for i in range(n):
    hashing[arr[i]] += 1

for i in range(len(hashing)):
    if(hashing[i] > n//2):
        print(i)

#Better Solution
arr = [2,2,3,3,1,2,2]
n = len(arr)

for i in range(n):
    count = 0
    for j in range(n):
        if(arr[i] == arr[j]):
            count += 1
    if(n//2 < count):
        print(arr[i])
        break

# Optimal
arr = [2,2,3,3,1,2,2]
n = len(arr)
count = 0
ele = 0

for i in range(n):
    
    if count == 0:
        count = 1
        ele = arr[i]
    elif arr[i] == ele:
        count += 1
    else:
        count -= 1

c1 = 0
for i in range(n):
    if(arr[i] == ele):
        c1 += 1
if(n//2 < c1):
    print(ele)


#Rearrange positives and negatives (Brute)
arr = [3,1,-2,-5,2,-4]
n = len(arr)

pos = []
neg = []

for i in range(n):
    if(arr[i] > 0):
        pos.append(arr[i])
    else:
        neg.append(arr[i])

for i in range(len(pos)):
    arr[2*i] = pos[i]
    arr[(2*i)+1] = neg[i]

print(arr)


#Optimal
arr = [3,1,-2,-5,2,-4]
n = len(arr)
ans = [0]*n
posIndex = 0
negIndex = 1

for i in range(n):
    if(arr[i] < 0):
        ans[negIndex] = arr[i]
        negIndex += 2
    else:
        ans[posIndex] = arr[i]
        posIndex += 2

print(ans)