# Maximum Consecutive Ones
arr = [1,1,0,1,1,1,1,0,1,1]
n = len(arr)
maxi = 0
count = 0

for i in range(n):
    if(arr[i] == 1):
        count += 1
        maxi = max(maxi,count)
    else:
        count = 0

print(maxi)


# Element that appaers once
arr = [1,1,2,3,3,4,4]
n = len(arr)
hashing = [0]*((n//2)+2)

for i in range(n):
    hashing[arr[i]] += 1

for i in hashing:
    if i == 1:
        print(hashing[i])
        break

# Optimal
arr = [1,1,2,3,3,4,4]
n = len(arr)
xor = 0
for i in range(n):
    xor = xor^arr[i]
print(xor)