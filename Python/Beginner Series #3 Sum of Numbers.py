#https://www.codewars.com/kata/55f2b110f61eb01779000053
def get_sum(a,b):
    suma = 0    
    for i in range(min(a,b),max(a,b)+1):
        suma += i
    return suma

print(get_sum(0,1))