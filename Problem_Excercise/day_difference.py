
from datetime import date

first_date = date(2017, 10, 2)
last_date = date(2017, 10, 21)

delta = last_date - first_date

print(delta.days)