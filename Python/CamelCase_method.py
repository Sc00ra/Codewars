# https://www.codewars.com/kata/587731fda577b3d1b0001196
def camel_case(s):
    s = s.split()
    string = ""
    for element in s:
        element = element[0].upper() + element[1:]
        string += element
    return string

