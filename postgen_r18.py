import csv
import os
import datetime

now = datetime.datetime.now() #get current time

savepath = '/content/r18' #save in a folder in the content dir of hugo
savepath = (f''+os.getcwd()+savepath+'')

with open('datacsv/scraperr18singles.csv') as csvfile: #open the csv containing the data
    csvrows = csv.reader(csvfile, delimiter=',', quotechar='"') #define delimiter, quote characters
    for row in csvrows: #set variable per columns
        url = row[0]
        samplevid = row[1]
        title = row[2]
        mainimgurl = row[3]
        mainimgs = row[4]
        details = row[5]
        duration = row[6]
        director = row[7]
        productioncomp = row[8]
        girls = row[9]
        catogories = row[10]
        imgurls = row[11]
        imgs = row[12]
        afflinkr18 = 'NjA4LjEuMS4xLjAuMC4wLjAuMA'

        url2 = url.strip('http://www.') #remove protocol, hugo only allows relative urls
        url2 = url2.split('=')[-1]
        samplevid = samplevid.strip('http://')
        # mainimgurl = mainimgurl.strip('https://')
        mainimgurl = mainimgurl.replace('https://', '')
        imgurls = imgurls.replace("https://", "")

        urlf1 = 'http://media.r18.com/'
        urlf2 = url.split('http://www.r18.com/')[-1]
        urlfinal = urlf1+'track/'+afflinkr18+'/'+urlf2

        if url == 'url': #don't print out first line of csv (the header)
            print('meh')
        else:
            filename =url.split('=')[-1] #split id name from url
            mdcontent = savepath+'/'+filename+'.md' #add .md at the end
            with open(mdcontent, 'w') as f:
                f.write('---')
                f.write('\n')
                f.write('date: '+now.strftime("%Y-%m-%d")+'')
                f.write('\n')
                f.write('draft: false')
                f.write('\n')
                f.write('affsite: "r18"')
                f.write('\n')
                f.write('afflinkr18: "'+afflinkr18+'"') #update with affiliate code later
                f.write('\n')
                f.write('url: "'+url2+'"')
                f.write('\n')
                f.write('urloriginal: "'+url+'"')
                f.write('\n')
                f.write('urlfinal: "'+urlfinal+'"')
                f.write('\n')
                f.write('samplevid: "'+samplevid+'"')
                f.write('\n')
                f.write('title: "'+title+'"')
                f.write('\n')
                f.write('mainimgurl: "'+mainimgurl+'"')
                f.write('\n')
                f.write('mainimgs: "'+mainimgs+'"')
                f.write('\n')
                f.write('releasedate: "'+details+'"')
                f.write('\n')
                f.write('duration: '+duration+'') #number
                f.write('\n')
                f.write('productioncomp: "'+productioncomp+'"')
                f.write('\n')
                f.write('girls: '+girls+'') #list
                f.write('\n')
                f.write('categories: '+catogories+'')
                f.write('\n')
                f.write(f'imgurls: {imgurls}') #written using f string
                f.write('\n')
                f.write('imgs: '+imgs+'')
                f.write('\n')
                f.write('---')
                f.write('\n')
                f.close()
