from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
movie_names = soup.find_all(name="h3", class_="title")
movies_list = [name.getText() for name in movie_names]
movies_list.reverse()

with open("movie_names.txt", "w") as file:
    for movie in movies_list:
        file.write(f"{movie} \n")
