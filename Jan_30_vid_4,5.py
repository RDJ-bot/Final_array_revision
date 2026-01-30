# Longest sub-array with given sum k (Brute Force)
arr = [1,2,3,1,1,1,1,4,2,3]
n = len(arr)

sums = 0
target = 5 
maxi = 0

for i in range(n):
    for j in range(i,n):
        sums = 0
        for k in range(i,j+1):
            sums += arr[k]
        if(sums == target):
            maxi = max(maxi,j-i+1)

print(maxi)


# Better
arr = [1,2,3,1,1,1,1,4,2,3]
n = len(arr)

sums = 0
maxi = 0
target = 5

for i in range(n):
    sums = 0
    for j in range(i,n):
        sums += arr[j]
        if sums == target:
            maxi = max(maxi,j-i+1)
print(maxi)



# Optimal
arr = [1,2,3,1,1,1,1,4,3,2]
n = len(arr)

left = 0
sums = 0
maxi = 0
target = 4

for right in range(n):
    sums += arr[right]
    if(sums == target):
        maxi = max(maxi,right-left+1)
    while sums > target:
        sums -= arr[left]
        left += 1

print(maxi)



#Two sum(Brute)
arr = [2,5,6,8,11]
n = len(arr)
target = 14
flag = False

for i in range(n):
    for j in range(i+1,n):
        if(arr[i]+arr[j] == target):
            print(arr[i], arr[j])
            print("Yes")
            flag = True
            break
    if(flag):
        break


#Better
arr = [2,6,5,8,11]
n = len(arr)
target = 14
dic = {} 

for i in range(n):
    comp = target - arr[i]
    if comp in dic:
        print(dic[comp],i)
        break
    dic[arr[i]] = i


#Optimal
arr = [2,5,6,8,11]
n = len(arr)
target = 14
arr.sort
left = 0
right = n-1

while left < right:
    sums = arr[left] + arr[right]
    if sums == target:
        print("Yes")
        break
    elif sums > target:
        right -=1
    else:
        left += 1