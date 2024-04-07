#https://www.codewars.com/kata/576757b1df89ecf5bd00073b

def tower_builder(n_floors):
    tower = []
    empty = " "
    stars = "*"
    number_stars = 1
    empty_count = n_floors-1
    for i in range(0,n_floors):
        string = empty*empty_count + number_stars*stars + empty*empty_count
        tower.append(string)
        number_stars+=2
        empty_count-=1
    return tower


print(tower_builder(1))