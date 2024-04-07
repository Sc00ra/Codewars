#https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
   
    if seconds == 0:
        return "now"
    minutes = 0
    hours = 0
    days = 0
    years = 0
    final = []
    while seconds >= 60:
        seconds -= 60
        minutes += 1
        if minutes >=60:
            minutes = 0
            hours += 1
            if hours >=24:
                hours = 0
                days += 1
                if days >=365:
                    days = 0
                    years +=1
    data = [('year',years), ('day',days),('hour',hours),('minute',minutes),('second',seconds)]
    
    for name, count in data:
        if count > 1:
            name +='s'
        if count > 0:
            final.append(f"{count} {name}")   
    if len(final) > 1:
        return ', '.join(final[:-1]) + ' and ' + final[-1]
    else:
        return final[0]


print(format_duration(3662))