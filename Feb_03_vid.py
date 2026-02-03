# Alternate pos and neg

arr = [1,1,-2,-2,3,3,-2,-4,-5,-7]
n = len(arr)
pos = []
neg = []
res = [0]*n

for i in range(n):
    if(arr[i] < 0):
        neg.append(arr[i])
    else:
        pos.append(arr[i])

if(len(pos) < len(neg)):
    for i in range(len(pos)):
        res[2*i] = pos[i]
        res[(2*i)+1] = neg[i]
    index = len(pos)*2
    for i in range(len(pos),len(neg)):
        res[index] = neg[i]
        index += 1

else:
    for i in range(len(neg)):
        res[2*i] = pos[i]
        res[(2*i)+1] = neg[i]
    index = len(neg)*2
    for i in range(len(neg),len(pos)):
        res[index] = pos[i]
        index += 1


print(res)

