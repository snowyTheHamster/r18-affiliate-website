import requests
from bs4 import BeautifulSoup

## t = open("scraperr18b.csv", "w+") ##generate to advanced csv

i = 1
while i < 418:
    url = "http://www.r18.com/videos/vod/movies/list/pagesize=120/price=all/sort=new/type=all/page="+str(i)+"/"
    result = requests.get(url, stream=True)
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "html.parser")
        # print(soup.prettify)

        ll = soup.find_all("li", {"class": "item-list"})
        for item in ll:
            t.write(item.a["href"])
            #print(item.img["src"])
            #print(item.dt.text)
            
            t.write("\n") ##generate to csv
        i += 1
t.close() ##generate to csv