#https://www.codewars.com/kata/576bb71bbbcf0951d5000044

def count_positives_sum_negatives(arr):
    return ([len([element for element in arr if element >0])  ,sum(element for element in arr if element <=0)] if arr != [] else [])

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))