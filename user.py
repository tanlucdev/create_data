from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

faker = Faker()
dt = []
row_num = 300001

for x in range(1,row_num,1):
    user_id = x
    fullname = faker.name()
    phone = faker.phone_number()
    email = faker.email()
    address = faker.address()
    level = random.randint(0,5)
    
    start_date = faker.date_time_between_dates(datetime_start=datetime(2004, 1, 1), datetime_end=datetime(2023, 1, 1))
    random_datetime = faker.date_time_between(start_date=start_date, end_date=start_date + timedelta(days=365))

    created_at = random_datetime.isoformat(timespec='seconds')

    temp5 = faker.date_between_dates(date_start=datetime(int(created_at[:4]),int(created_at[5:7]),int(created_at[8:10])), date_end=datetime.today())
    random_datetime2 = faker.date_time_between(start_date=temp5, end_date=temp5 + timedelta(days=365))

    last_login = random_datetime2.isoformat(timespec='seconds')
    row = {
        'user_id':user_id,
        'fullname':fullname,
        'phone':phone,
        'email':email,
        'address':address,
        'level':level,
        'created_at':created_at + "+00:00",
        'last_login':last_login + "+00:00",
    }
    dt.append(row)

df = pd.DataFrame(dt)

output = 'User.xlsx'
df.to_excel(output, index=False)
