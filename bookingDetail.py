from faker import Faker
import pandas as pd
import random

booking = pd.read_excel('Booking.xlsx')
booking_data = booking['booking_id']
row_num = len(booking)

dt = []
for x in range(0,row_num,1):

    times = random.randint(1,5)
    booking_id = str(booking_data[x]).zfill(8)
    for y in range(1,times+1,1):
        ticket_type_id = random.randint(1,10000)
        quantity = random.randint(1,10)
        row = {
            'booking_id':booking_id,
            'ticket_type_id':ticket_type_id,
            'quantity':quantity
        }
        dt.append(row)

df = pd.DataFrame(dt)

output = 'Booking Detail.xlsx'
df.to_excel(output, index=False)

