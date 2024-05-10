#https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b


def human_years_cat_years_dog_years(human_years):
    return [human_years, (15+9+4*(human_years-2) if human_years >2 else 24 if human_years == 2 else 15),(15+9+5*(human_years-2) if human_years >2 else 24 if human_years == 2 else 15)]