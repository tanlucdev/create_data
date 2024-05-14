import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import random

faker = Faker()
dt = []
row_num = 200001

for x in range(1,row_num,1):
    ticket_type_id = x
    ticket_type_name = faker.word().capitalize() + " Ticket"
    event_id = random.randint(1,100001)
    price = int(str(random.randint(500,2000)) + "000")
    n_sold = random.randint (0,1000)
    n_stock = random.randint (1000,2000)
    is_selling = faker.random_element(elements=('true', 'false'))

    start_date = faker.date_time_between_dates(datetime_start=datetime(2004, 1, 1), datetime_end=datetime(2023, 1, 1))
    random_datetime = faker.date_time_between(start_date=start_date, end_date=start_date + timedelta(days=365))

    created_at = random_datetime.isoformat(timespec='seconds')

    temp5 = faker.date_between_dates(date_start=datetime(int(created_at[:4]),int(created_at[5:7]),int(created_at[8:10])), date_end=datetime.today())
    random_datetime2 = faker.date_time_between(start_date=temp5, end_date=temp5 + timedelta(days=365))

    updated_at = random_datetime2.isoformat(timespec='seconds')
    row = {
        'ticket_type_id':ticket_type_id,
        'ticket_type_name':ticket_type_name,
        'event_id':event_id ,
        'price':price,
        'n_sold':n_sold,
        'n_stock' :n_stock,
        'is_selling' :is_selling,
        'created_at' :created_at + "+00:00",
        'updated_at' :updated_at + "+00:00",
    }
    dt.append(row)

df = pd.DataFrame(dt)

output = 'Ticket Type.xlsx'
df.to_excel(output, index=False)