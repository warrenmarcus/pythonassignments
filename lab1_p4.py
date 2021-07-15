# Warren Green
# 006314031
#funcion declaration
def find_cummulative_sum():
    arr2 = []

    i = 0
    while i < len(arr):
        k= 0
        x = 0
        while k<=i:
            x += arr[k]
            k += 1
        arr2.append(x)
        i +=1
    print("\nThe cummulative sum:\n\t",  arr2)



#initial array
arr = [1, 3, 5, 7, 9]

# prints initial array
print("\noriginal array:\n\t", arr)

# calls the function that manipulates the array
find_cummulative_sum()
