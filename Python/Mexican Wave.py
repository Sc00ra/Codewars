#https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

def wave(people):
    mv = []
    for i in range(0,len(people)):
        if people[i] != ' ':
            mv.append(people[0:i] + people[i].upper() + people[i+1:])
    return mv

print(wave("hello"))