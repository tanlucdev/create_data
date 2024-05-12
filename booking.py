from faker import Faker
import pandas as pd
from datetime import datetime, timedelta
import random


faker = Faker()
row_num = 100001

dt = []
for x in range(1,row_num,1):
    random_number = random.randint(1, 99999999)
    booking_id = str(random_number).zfill(8)
    customer_id = random.randint(1,300000)
    payment_methods = [
    "Credit Card",
    "Debit Card",
    "PayPal",
    "Apple Pay",
    "Google Pay",
    "Stripe",
    "Venmo",
    "Square",
    "AliPay",
    "WeChat Pay",
    "Amazon Pay",
    "Bank Transfer",
    "Cash on Delivery (COD)",
    "Cheque Payment",
    "Mobile Wallet",
    "Prepaid Card",
    "Cryptocurrency",
    "Gift Card",
    "Money Order",
    "Paytm",
    "Skrill",
    "Neteller",
    "Western Union",
    "Zelle",
    "Klarna"
]
    payment_method = status = faker.random_element(elements=payment_methods)
    temp_cost =  int(str(random.randint(100,500)) + "000")
    status = status = faker.random_element(elements=('pending', 'completed', 'canceled'))

    start_date = faker.date_time_between_dates(datetime_start=datetime(2004, 1, 1), datetime_end=datetime(2023, 1, 1))
    random_datetime = faker.date_time_between(start_date=start_date, end_date=start_date + timedelta(days=365))

    created_at = random_datetime.isoformat(timespec='seconds')

    temp5 = faker.date_between_dates(date_start=datetime(int(created_at[:4]),int(created_at[5:7]),int(created_at[8:10])), date_end=datetime.today())
    random_datetime2 = faker.date_time_between(start_date=temp5, end_date=temp5 + timedelta(days=365))

    updated_at = random_datetime2.isoformat(timespec='seconds')
    row = {
        'booking_id':booking_id ,
        'customer_id':customer_id ,
        'payment_method':payment_method ,
        'temp_cost':temp_cost,
        'status':status,
        'created_at':created_at,
        'updated_at':updated_at ,
    }
    dt.append(row)

df = pd.DataFrame(dt)

output = 'Booking.xlsx'
df.to_excel(output, index=False)


