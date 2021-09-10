from datetime import date
from datetime import datetime

today = date.today()

# yesterday = '2021-09-06'

date_and_time_as_text = '06/09/2021 00:00'
yesterday = datetime.strptime(date_and_time_as_text, '%d/%m/%Y %H:%M')

print("Today's date:", today)
print("--------------------")
print("Yesterday date is:", yesterday)

# Current date in different formats
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)


# https://www.programiz.com/python-programming/datetime/current-datetime
# https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python?gclid=Cj0KCQjwm9yJBhDTARIsABKIcGbUPJ82SWTIxU2QOdACqahRlqq2LDRvyVy4SuRu9szTuSYdy4RwjXkaAppFEALw_wcB
