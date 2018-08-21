from models.customer import Customer
import mlab
from faker import Faker
from random import randint,choice
mlab.connect()

fake = Faker()
for i in range(50):
    print("Saving customer: ", i+1,"......")
    new_customer = Customer(
        name = fake.name(),
        gender = randint(0,1),  
        job = fake.job(),
        email = fake.email(),
        phone_number = fake.phone_number(),
        company = fake.company(),
        contacted = choice([True,False])
    )
    new_customer.save()