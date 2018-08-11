from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"
html_content = urlopen(url).read()

soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("ul", class_=None)
li_list = ul.find_all("li")
data = []
for li in li_list:
    top_itunes = {}
    name = li.h3.a
    artist = li.h4.a
    top_itunes["Song's name"] = name.string    
    top_itunes["Artists"] = artist.string
    data.append(top_itunes)
pyexcel.save_as(records=data, dest_file_name="itunes_top_songs.xlsx")