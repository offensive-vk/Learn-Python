import datetime

current_date = datetime.date.today()
print("Current date:", current_date)

current_time = datetime.datetime.now().time()
print("Current time:", current_time)

birth_date = datetime.date(2000, 5, 15)
age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
print("Your Age:", age)
