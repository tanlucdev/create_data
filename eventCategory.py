import pandas as pd
from faker import Faker

faker = Faker()
dt = []
row_num = 10001

for x in range(1,row_num,1):
    row = {
        'category_id':x,
        'category_name':faker.word().capitalize() + " " + faker.word(),
    }
    dt.append(row)

df = pd.DataFrame(dt)

output = 'Category.xlsx'
df.to_excel(output, index=False)