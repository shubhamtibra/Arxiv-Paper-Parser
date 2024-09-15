import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

search_phrases = ["holonomic+functions", "ore+algebra", "weyl+algebra", "D-finite+functions", "differential+equations+with+polynomial+coefficients"]
#If there is no such folder, the script will create one automatically
folder_location = r'./holonomic/'
if not os.path.exists(folder_location):os.mkdir(folder_location)
for search_phrase in search_phrases:
    for start in range(0, 2000, 200):
        got_result = False
        url = f"https://arxiv.org/search/?query=%22{search_phrase}%22&searchtype=abstract&abstracts=show&order=&size=200&start={start}"
        response = requests.get(url)
        soup= BeautifulSoup(response.text, "html.parser")
        pdf_links = soup.find_all("a", string='pdf')
        for link in pdf_links:
        #Name the pdf files using the last portion of each link which are unique in this case
            filename = os.path.join(folder_location,link['href'].split('/')[-1]) + ".pdf"
            with open(filename, 'wb') as f:
                get_url = urljoin(url,link['href'])
                f.write(requests.get(get_url).content)
            got_result = True
        if not got_result:
            break