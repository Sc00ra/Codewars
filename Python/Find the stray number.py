#https://www.codewars.com/kata/57f609022f4d534f05000024

def stray(arr):
    return [element for element in arr if arr.count(element)==1][0]

print(stray([1, 1, 1, 1, 1, 1, 2]))