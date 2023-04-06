import random
import datetime
for i in range(10):
 a="sinthanaikaga silanimidam","osho","pavai htamil nool"
 slection=start_date = datetime.date(2022, 2, 24)  # import random
 end_date = datetime.date(2022, 3, 7)  # import datetime
 random_duration = random.randrange((end_date - start_date).days)
 random_date = start_date + datetime.timedelta(random_duration)
 print(random_date)
print(i)

