from youtube_dl import YoutubeDL

# Sample 1: Download a single youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=qx5GoahJKX0']) #(Bài hát: Mashup Đừng Như Thói Quen - Chạm Đáy Nỗi Đau - Jaykii x Erik)



# Sample 2: Download multiple youtube videos
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=5WN19l18Eo8', 'https://www.youtube.com/watch?v=1tigZHyxUdc']) #(Bài hát:Đừng Quên Tên Anh - Hoa Vinh / Sao Em Nỡ - Jaykii )



# Sample 3: Download audio
options = {
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=cUmpJ2zwfVU']) #(Bài hát: Suýt Nữa Thì - Andez)



# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options)
dl.download(['Mashup Bùa yêu - Chạy ngay đi P.M Band'])


# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1, 
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Đừng hỏi em Mỹ Tâm'])