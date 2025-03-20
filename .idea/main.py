from bs4 import BeautifulSoup
import requests
import warnings

warnings.simplefilter("ignore",DeprecationWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def parse():
    url = 'https://www.imdb.com/chart/top/'
    page = requests.get(url,headers=headers)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    movies = soup.findAll('h3', class_='ipc-title__text')
    ratings = soup.findAll('span', class_='ipc-rating-star--rating')

    movie_dict = {}
    i = 0
    for movie, rating in zip(movies, ratings):
        if i==0:
            i+=1
            continue
        title = movie.text
        rate = rating.text
        movie_dict[title] = rate
        i+=1

    for title, rate in movie_dict.items():
        print(f"{title}: {rate}")

if __name__ == '__main__':
    movies = parse()