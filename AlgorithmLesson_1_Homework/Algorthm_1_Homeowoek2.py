#Find max number from 3 values, entered manually from a keyboard.
#Example: 124, 21, 32. Result = 124.

# 0(1)
def find max(1,2,3):
    return max(n1, n2, n3)
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n1 and n2 > n3:
        return n3


n1 = int(input('input value1:'))
n2 = int(input('input value2:'))
n3 = int(input('input value3:'))

print(find_max(n1, n2, n3))