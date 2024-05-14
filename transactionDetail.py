from faker import Faker
import pandas as pd
import random

faker = Faker()
checkout = pd.read_excel('Checkout.xlsx')
row_num = len(checkout)

dt = []
for x in range(0,row_num,1):
    times = random.randint(1,5)
    checkout_id = x+1
    for y in range(1,times+1,1):
        ticket_id = random.randint(1,10000)

        row = {
            'checkout_id':checkout_id,
            'ticket_id':ticket_id,
        }
        dt.append(row)

df = pd.DataFrame(dt)

output = 'Transaction Detail.xlsx'
df.to_excel(output, index=False)


