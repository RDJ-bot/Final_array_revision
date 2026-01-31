#Sub array with maxi sum
arr = [-2,-3,4,-1,-2,1,5,3]
n = len(arr)
maxi = 0

for i in range(n):
    for j in range(i,n):
        sums = 0
        for k in range(i,j+1):
            sums += arr[k]
        maxi = max(sums,maxi)
print(maxi)


#Kadan's Algo
arr = [-2,-3,4,-1,-2,1,5,3]
n = len(arr)
maxi = 0

for i in range(n):
    sums += arr[i]
    maxi = max(maxi,sums)
    if(sums < 0):
        sums = 0

print(maxi)