#https://www.codewars.com/kata/5583090cbe83f4fd8c000051
def digitize(n):
    return (lambda x : x[::-1])(list(map(int,str(n)))) 