import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# start by defining the options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # it's more scalable to work in headless mode
# normally, selenium waits for all resources to download
# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none'
# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
# pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
url = 'https://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
list_ele = soup.find_all('td', class_="titleColumn")
ratings = [r.text.strip() for r in soup.find_all('td', class_="ratingColumn imdbRating")[:10]]
result = {'Movie_name': [],
          'Year_of_release': [],
          'Rating': ratings,
          'Summary': []}
for movie_link in list_ele[:10]:
    movie_name = movie_link.find('a').text.strip()
    result['Movie_name'].append(movie_name)

    split_name = movie_name.split(' ')
    my_string = f'{split_name[0]}'

    for i in split_name[1:]:
        my_string = my_string + "+" + i
    url2 = "https://www.google.com/search?q=" + my_string + "+summary"
    driver.get(url2)
    time.sleep(2)

    html = driver.page_source
    soup2 = BeautifulSoup(html, 'html.parser')
    summary = soup2.find("div", class_="Z0LcW k37FLe t2b5Cf")
    try:
        result['Summary'].append(summary.text)
    except Exception as error:
        result['Summary'].append(error)
    year = movie_link.find('span', class_="secondaryInfo").text.strip()
