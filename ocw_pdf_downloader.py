import bs4 as bs
import urllib.request
import requests

source_url = str(input("Enter the source URL (web page with list of files) : "))
content = urllib.request.urlopen(source_url).read()
lxml_content = bs.BeautifulSoup(content,'lxml')

links = []
for url in lxml_content.find_all('a'):
    links.append(url.get('href'))

for link in links:
    if(len(link)>3):
        if(link[-3:] == 'pdf'):
            print(link)
            file_url = "https://ocw.mit.edu" + link
            file_name = ""
            i = len(file_url) - 1
            while(i>=0 and file_url[i]!='/'):
                file_name = file_url[i] + file_name
                i -= 1

            r = requests.get(file_url, stream=True)
            with open(file_name,"wb") as pdf:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        pdf.write(chunk)
