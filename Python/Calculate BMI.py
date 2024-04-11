#https://www.codewars.com/kata/57a429e253ba3381850000fb

def bmi(weight, height):
    return "Underweight" if weight/height**2 <= 18.5 else "Normal" if  weight/height**2 <= 25 else "Overweight" if weight/height**2 <= 30 else "Obese"