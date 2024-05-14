from faker import Faker
import pandas as pd
from datetime import datetime, timedelta
import random
import string

faker = Faker()
dt = []
row_num = 200001

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

for x in range(1,row_num,1):
    ticket_id = x
    ticket_type_id = random.randint(1,10000)

    ticket_code = generate_random_string(4) + "-" + generate_random_string(4) + "-" + generate_random_string(4) + "-" + generate_random_string(4)

    status = faker.random_element(elements=('Available', 'Sold'))

    start_date = faker.date_time_between_dates(datetime_start=datetime(2004, 1, 1), datetime_end=datetime(2023, 1, 1))
    random_datetime = faker.date_time_between(start_date=start_date, end_date=start_date + timedelta(days=365))

    created_at = random_datetime.isoformat(timespec='seconds')

    temp5 = faker.date_between_dates(date_start=datetime(int(created_at[:4]),int(created_at[5:7]),int(created_at[8:10])), date_end=datetime.today())
    random_datetime2 = faker.date_time_between(start_date=temp5, end_date=temp5 + timedelta(days=365))

    expiry = random_datetime2.isoformat(timespec='seconds')

    row = {
        'ticket_id':ticket_id,
        'ticket_type_id' : ticket_type_id,
        'ticket_code':ticket_code,
        'expiry':expiry+"+00:00",
        'status':status,
        'created_at':created_at+ "+00:00",
    }
    dt.append(row)


df = pd.DataFrame(dt)

output = 'Ticket.xlsx'
df.to_excel(output, index=False)