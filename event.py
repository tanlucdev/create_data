from faker import Faker
import pandas as pd
from datetime import datetime, timedelta
import random


faker = Faker()
row_num = 100001

dt = []
for x in range(1,row_num,1):
    id = x
    name = faker.catch_phrase()
    occur_date = faker.date_between(start_date='-20y', end_date='+1y').strftime('%Y-%m-%d')
    occur_time= str(faker.random_int(min = 1, max = 12)) + ':' + str(faker.random_int(min = 0, max = 55, step=5)) + " " + faker.am_pm() + " - " + str(faker.random_int(min = 1, max = 12)) + ':' + str(faker.random_int(min = 0, max = 55, step=5)) + " " + faker.am_pm()
    location = faker.company()
    address = faker.address()
    introduction = faker.paragraph(nb_sentences=random.randint(50,200))
    banner = faker.image_url(width=200, height=200)

    if(int(occur_date[0:4]) >= int(datetime.now().year)):
        status = faker.random_element(elements=('Pending', 'Published'))
    else:
        status = faker.random_element(elements=('Pending', 'Ended', 'Published'))

    start_date = faker.date_time_between_dates(datetime_start=datetime(2004, 1, 1), datetime_end=datetime(2023, 1, 1))
    random_datetime = faker.date_time_between(start_date=start_date, end_date=start_date + timedelta(days=365))

    created_at = random_datetime.isoformat(timespec='seconds')

    temp5 = faker.date_between_dates(date_start=datetime(int(created_at[:4]),int(created_at[5:7]),int(created_at[8:10])), date_end=datetime.today())
    random_datetime2 = faker.date_time_between(start_date=temp5, end_date=temp5 + timedelta(days=365))

    updated_at = random_datetime2.isoformat(timespec='seconds')


    author_id = random.randint(1,row_num - 1)
    category_id  = random.randint(1,10000)
    row = {
        'id':id,
        'name':name,
        'occur_date':occur_date,
        'occur_time':occur_time,
        'location':location,
        'address':address,
        'introduction':introduction,
        'banner':banner,
        'status':status,
        'created_at':created_at+'+00:00',
        'updated_at':updated_at+'+00:00',
        'author_id':author_id,
        'category_id':category_id,
    }
    dt.append(row)

df = pd.DataFrame(dt)

output = 'Event.xlsx'
df.to_excel(output, index=False)


