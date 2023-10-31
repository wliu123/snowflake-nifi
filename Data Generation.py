#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install faker


# In[2]:


from faker import Faker
import csv
import random
from decimal import Decimal
from datetime import datetime

RECORD_COUNT = 10000
fake = Faker()


# In[3]:


current_time = datetime.now().strftime("%Y%m%d%H%M%S")
print(current_time)


# In[6]:


def create_csv_file():
    with open(f'FakeDataset/customer_{current_time}.csv','w',newline='') as csvfile:
        fieldnames = ["customer_id","first_name","last_name","email","street","city","state","country"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    "customer_id":i, #fake.random_int(min=1, max=10000),
                    "first_name":fake.first_name(),
                    "last_name":fake.last_name(),
                    "email":fake.email(),
                    "street":fake.street_address(),
                    "city":fake.city(),
                    "state":fake.state(),
                    "country":fake.country()
                }
            )


# In[7]:


if __name__ == '__main__':
    create_csv_file()


# In[ ]:




