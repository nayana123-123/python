import datetime
import math
import random

now=datetime.datetime.now()
print("Current date and time:",now.strftime("%Y-%m-%d%H:%M:%S"))

num=random.randint(1,100)
print("Random number generated:",num)

sqrt_num=math.sqrt(num)
print(f"The square root of {num}is{sqrt_num:.2f}")

end_of_year=datetime.datetime(now.year,12,31)
days_left=(end_of_year-now).days
print(f"Days left in the year:{days_left}")
