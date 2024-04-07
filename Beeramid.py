#https://www.codewars.com/kata/51e04f6b544cf3f6550000c1
import math
def beeramid(bonus, price):
    beers = math.floor(bonus/price)
    x = 1
    count = 0
    while beers>0:
        count +=1
        beers -= x**2
        x+=1
        if beers < x ** 2:
            break
    return count


print(beeramid(454, 5))
