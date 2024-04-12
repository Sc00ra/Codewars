def is_triangle(a, b, c):
    return min(a,b,c) + (a+b+c - min(a,b,c) - max(a,b,c)) > max(a,b,c)
