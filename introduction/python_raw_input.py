#https://www.hackerrank.com/challenges/python-raw-input
def read():
    s = input("Please input a string: ")
    return s

input_string = read()
string_length = len(input_string)
if (string_length >= 1 & string_length <= 500):
    print(input_string)
