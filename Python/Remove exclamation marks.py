#https://www.codewars.com/kata/57a0885cbb9944e24c00008e

def remove_exclamation_marks(s):
    return "".join(element for element in s if element != "!")