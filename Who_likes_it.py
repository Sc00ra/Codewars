#https://www.codewars.com/kata/5266876b8f4bf2da9b000362
def likes(names):
    # your code here
    if len(names) > 3:
        str = f'{names[0]}, {names[1]} and {len(names)-2} others like this'
    elif len(names) == 3:
        str = f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) == 2:
        str = f'{names[0]} and {names[1]} like this'  
    elif len(names) == 1:
        str = f'{names[0]} likes this'
    else:
        str = "no one likes this"
    return str