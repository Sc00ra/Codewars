#https://www.codewars.com/kata/5544c7a5cb454edb3c000047

def bouncing_ball(h, bounce, window):
    if h <= 0: return -1
    if bounce <=0 or bounce >= 1: return -1
    if window >= h: return -1
    count = 0


    while h>0:
        count += 1
        h = h*bounce
        if h > window:
            count += 1
        if h <= window:
            break
    return count

print(bouncing_ball(2, 0.5, 1))