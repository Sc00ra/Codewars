#https://www.codewars.com/kata/583710ccaa6717322c000105

def simple_multiplication(number) :
    return (lambda x : x*8 if x % 2 == 0 else x*9)(number)