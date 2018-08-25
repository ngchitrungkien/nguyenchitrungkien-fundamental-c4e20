from models.service import Service
import mlab
from faker import Faker
from random import *

mlab.connect()

fake = Faker()

for i in range(20):
    print('Saving service', i + 1, '...')
    gender = randint(0,1)
    descriptions_male = ['đẹp trai','ga-lăng','thích thể thao','thích nấu ăn','chơi được nhạc cụ','hiền lành','yêu động vật','chăm chỉ','thích ca hát','thích đi phượt','thích chơi game']
    descriptions_female = ['ngoan hiền','xinh gái','thùy mị','thích nấu ăn','mignonne','thích đi phượt','lễ phép','yêu động vật','thích thể thao','thích bolero','thích shopping','thích badboy']
    image_male = ['70b2fdaecbda9c6e09a9fb83ff44f3aa.jpg', '323aaa276aa703ab46d2fdd4b852c4cf.jpg', 'DAVID-BECKHAM-on-GUY-RITCHIE-VIDEO-for-HM.png', 'fashion-man-person-247885.jpg', 'male.jpg']
    image_female = ['1535672-jenni-1508408525-318-640x480.jpg', 'emma-stone-equal-pay.jpg', 'female.jpg', 'laura-harrier-interview-1533934587.jpg', 'woman-2739786_960_720.jpg']

    if gender:
        new_service = Service(
            image = '../static/image/male/' + choice(image_male),
            name = fake.name(),
            gender = gender,
            yob = randint(1989,2000),
            height = randint(165,190),
            phone = fake.phone_number(),
            address = fake.address(),
            status = choice([True,False]),
            descriptions = sample(descriptions_male,3)
            
        )
    else:
        new_service = Service(
            image = '../static/image/female/' + choice(image_female),
            name = fake.name(),
            gender = gender,
            yob = randint(1989,2000),
            height = randint(150,175),
            phone = fake.phone_number(),
            address = fake.address(),
            status = choice([True,False]),
            descriptions = sample(descriptions_female,3),
            measurements = [randint(70,90), randint(60,70), randint(70,90)]
        )

    new_service.save()