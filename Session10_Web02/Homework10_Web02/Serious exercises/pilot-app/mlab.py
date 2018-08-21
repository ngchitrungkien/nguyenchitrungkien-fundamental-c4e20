import mongoengine

#mongodb://user1:Kien1812@ds125912.mlab.com:25912/muadongkhonglanh

host = "ds125912.mlab.com"
port = 25912
db_name = "muadongkhonglanh"
user_name = "user1"
password = "Kien1812"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

