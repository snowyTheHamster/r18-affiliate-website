import csv
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

# os.chdir('.') # set directory here


#gets list of single page urls
with open('scraperr18.csv') as csvfile: #feed the csv with list of urls
# with open('practice.csv') as csvfile:
    t = open('scraperr18singles.csv', "a+") #creates a file to save data
    csvrows = csv.reader(csvfile, delimiter=',', quotechar='"')
    #add header row once
    # t.write('\"url\",\"samplevid\",\"title\",\"mainimgurl\",\"mainimgs\",\"details\",\"duration\",\"director\",\"productioncomp\",\"girls\",\"catogories\",\"imgurls\",\"imgs\"')
    t.write("\n")
    for row in csvrows:
        row = row[0]

        #runs scraper per url
        url = row
        result = requests.get(url, stream=True)
        if result.status_code == 200:
            soup = BeautifulSoup(result.content, "html.parser")

            #pull out each field
            dm_title = soup.h1.text
            dm_title = dm_title.replace('"', '\'')
            dm_title = dm_title.strip()

            try:
                dm_samplevidurl = soup.find(class_="js-view-sample")["data-video-high"]
            except:
                dm_samplevidurl = '----'

            dm_imagemainurl = soup.find(itemprop="image")['src'].strip()
            dm_imagemain = dm_imagemainurl.split('/')[6].strip()
            
            dm_details = soup.find(itemprop="dateCreated").text.strip()
            dm_duration = soup.find(itemprop="duration").text.strip()
            dm_duration = dm_duration.split('min')[0]
            dm_director = soup.find(itemprop="director").text.strip()
            dm_productionCompany = soup.find(itemprop="productionCompany").text.strip()

            #get list of actresses
            dm_gals = []
            dm_actress = soup.find_all(itemprop="actors")
            for dm_gal in dm_actress:
                girls = dm_gal.find_all("span", attrs={"itemprop": "name"})
                for dm_gal in girls:
                    dm_gal = (dm_gal.text)
                    dm_gals.append(dm_gal)
            dm_gals = str(dm_gals)

            #get list of categories
            dm_cats = []
            dm_category = soup.find_all(class_="pop-list")
            for dm_cat in dm_category:
                catts = dm_cat.find_all("a", attrs={"itemprop": "genre"})
                for dm_cat in catts:
                    dm_cat = (dm_cat.text).strip()
                    dm_cats.append(dm_cat)
            dm_cats = str(dm_cats)

            #get the large sample images
            dm_imgurls = []
            dm_imgs = []
            divi = soup.find(class_="js-owl-carousel")
            children = divi.findChildren("img" , recursive=True)
            for dm_gallery in children:
                dm_imagelisturl = dm_gallery['data-src']
                dm_imagelist = dm_imagelisturl.split('/')[6]
                dm_imgurls.append(dm_imagelisturl)
                dm_imgs.append(dm_imagelist)
            dm_imgurls = str(dm_imgurls)
            dm_imgs = str(dm_imgs)

            #get the pages url
            theid = row.split('id=')[1]
            theid = theid.split('/')[0]
            baseurl = 'http://www.r18.com/videos/vod/movies/detail/-/id='
            dm_pageurl = baseurl+theid
            print('done scraping: %s' % dm_pageurl)

            t.write('\"'+dm_pageurl+'\",\"'+dm_samplevidurl+'\",\"'+dm_title+'\",\"'+dm_imagemainurl+'\",\"'+dm_imagemain+'\",\"'+dm_details+'\",\"'+dm_duration+'\",\"'+dm_director+'\",\"'+dm_productionCompany+'\",\"'+dm_gals+'\",\"'+dm_cats+'\",\"'+dm_imgurls+'\",\"'+dm_imgs+'\"')
                
            t.write("\n")

            sleep(randint(1,2))

    t.close()
