from mongoengine import *
#design DB
class Service(Document): #ten collection chu bat dau nen viet hoa #(Document) la bat buoc
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()