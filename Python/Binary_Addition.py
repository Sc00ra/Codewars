#https://www.codewars.com/kata/551f37452ff852b7bd000139
def add_binary(a,b):
    #your code here
    x = bin(a+b)
    x = x[2:]
    return x