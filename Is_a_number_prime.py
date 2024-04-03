#https://www.codewars.com/kata/5262119038c0985a5b00029f

def is_prime(num):
    if num < 2:
        return False
    x = 2
    while x*x <= num:
        if num % x == 0:
            return False
        x += 1
    return True
            


print(is_prime(99999999990911121313312321321412421))