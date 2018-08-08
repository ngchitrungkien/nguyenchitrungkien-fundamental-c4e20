from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db["posts"]

new_post = {
    "title" : "Tâm sự mỏng...",
    "author" : "Kiên 18 tuổi",
    "content" : "Khi bạn có quá nhiều sự lựa chọn, bạn không biết mình muốn gì. Khi bạn biết mình cần gì thì cũng là lúc bạn không còn sự lựa chọn!",
    "note" : "Nguyễn Chí Trung Kiên - C4E20 - Điều mà mình muốn nhắn gửi đến các khóa sau là dòng tâm sự mỏng ở trên :)) Hãy lựa chọn theo chính đam mê của bản thân, đừng để bản thân cảm thấy hối hận khi đã chọn sai hướng. Chúc các bạn thành công khi đồng hành cùng mái nhà Techkids tuyệt vời này ;)) "
}
posts.insert_one(new_post)