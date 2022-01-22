#Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#The string 'aabcde' contains duplicate characters and should return False.

def uniq_char(s):
    return len(sat(s)) = len(s)



test_str_positive = abcde #true
test_str_negative = abcde #false
print(test_str_positive)
print(uniq_char(test_str_positive))
print(test_str_negative)
print(uniq_char(test_str_negative))