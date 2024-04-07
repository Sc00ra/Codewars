#https://www.codewars.com/kata/578553c3a1b8d5c40300037c


def binary_array_to_number(arr):
    return sum(x * 2**i for i, x in enumerate(arr[::-1]))

binary_array_to_number([0,0,0,1])