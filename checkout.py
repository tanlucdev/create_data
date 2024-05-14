from faker import Faker
import pandas as pd
from datetime import datetime, timedelta
import random


faker = Faker()

booking = pd.read_excel('Booking.xlsx')
booking_data = booking['booking_id']
row_num = len(booking)

dt = []
for x in range(0,row_num,1):
    checkout_id = x+1

    booking_id = booking_data[x]

    tax = round(random.uniform(0.001, 0.01), 3)

    total = int(str(random.randint(500,2000)) + "000")

    start_date = faker.date_time_between_dates(datetime_start=datetime(2004, 1, 1), datetime_end=datetime(2023, 1, 1))
    random_datetime = faker.date_time_between(start_date=start_date, end_date=start_date + timedelta(days=365))

    created_at = random_datetime.isoformat(timespec='seconds')

    temp5 = faker.date_between_dates(date_start=datetime(int(created_at[:4]),int(created_at[5:7]),int(created_at[8:10])), date_end=datetime.today())
    random_datetime2 = faker.date_time_between(start_date=temp5, end_date=temp5 + timedelta(days=365))

    updated_at = random_datetime2.isoformat(timespec='seconds')
    
    row = {
        'checkout_id' :checkout_id,
        'booking_id':booking_id,
        'tax' :tax,
        'total' :total,
        'created_at' :created_at + "+00:00",
        'updated_at' :updated_at + "+00:00",
    
    }
    dt.append(row)

df = pd.DataFrame(dt)

output = 'Checkout.xlsx'
df.to_excel(output, index=False)


