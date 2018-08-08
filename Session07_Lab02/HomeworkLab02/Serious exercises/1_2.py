from youtube_dl import YoutubeDL

Name_the_song = input("Enter a song's name: ")
Artist = input("Enter an artist: ")

options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options)
dl.download([str(Name_the_song) + "-" + str(Artist)])


