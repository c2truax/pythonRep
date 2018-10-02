#1 
def countDown(num):
    arr=[]
    for x in range(num,-1,-1):
        arr.append(x)
    return arr
print(countDown(5))

#2**********
def pr(arr):
    print(arr[0])
    return arr[1]
print(pr([3,5]))

#3
def first(arr):
    sum= arr[0]+len(arr)
    return sum
print(first([1,2,3,4]))

#4
def valGreat(arr):
    if len(arr) < 2:
        return false
    newArr =[]
    for count in range(len(arr)):
        if arr[1] < arr[count]:
            newArr.append(arr[count])
    print(len(newArr))
    return newArr
valGreat([1,2,3,4])

#5
def lengthAndValue(size,val):
    newArr= []
    for count in range(size):
        newArr.append(val)
    return newArr
lengthAndValue(4,7)

