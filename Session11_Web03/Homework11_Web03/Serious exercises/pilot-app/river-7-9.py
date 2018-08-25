from mongoengine import *
#mongodb://admin:admin@ds021182.mlab.com:21182/c4e
host = "ds021182.mlab.com"
port = 21182
db_name = "c4e"
user_name = "admin"
password = "admin"
connect(db_name, host=host, port=port, username=user_name, password=password)

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

rivers = River.objects(continent__contains = "S. America", length__lt = 1000)
print()

print('Rivers in S.America continent with length less than 1000 km:')
for river in rivers:
    print(river.name, river.continent, river.length, sep = '\t')