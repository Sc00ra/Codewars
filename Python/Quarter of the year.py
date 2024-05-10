#https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/
def quarter_of(month):
    return 1 if month in range(1,4) else 2 if month in range(3,7) else 3 if month in range(6,10) else 4