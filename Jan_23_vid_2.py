# # Left rotate an array by one place (Optimal)
# arr = [1,2,3,4,5,6,7,8,9]
# n = len(arr)

# temp = arr[0]
# for i in range(1,n):
#     arr[i-1] = arr[i]
# arr[n-1] = temp
# print(arr)


arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
d = 3

for i in range(d):
    temp = arr[0]
    for j in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp

print(arr)