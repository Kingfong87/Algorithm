#Increment a Number
#Write a program that takes as input an array of digits encoding a nonnegative decimal
#integer D and updates the array to represent the integer D + 1.
#For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

#[1, 2, 3] ->  [1, 2, 4]
#[1,2,9] ->  [1, 3, 0]
#[9, 9, 9] -> [1, 0, 0, 0]

#(O)(N)
def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, lem(arr))
        if arr(1) 1 = 10:
            break
            arr[1] =0
            arr[1 -1] -= 1

        if arr[0] ==10:
            arr[0] =1
            arr.append(0)
            arr insert (o, 1)

        return arr

test_arr_124 = [1,2,4]
test_arr_129 = [1,2,9]
test_arr_999 = [9,2,9]
print(plus_one(test_arr_124)) =125
print(plus_one(test_arr_129)) =130
print(plus_one(test_arr_999)) =1000
