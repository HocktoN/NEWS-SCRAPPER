from bs4 import BeautifulSoup
import requests
from scrappers import *

# Sitelere göre kazıma araçlarımız
scrapper_tools = {"Hürriyet":hurriyet,"Sözcü":sozcu,"Cumhuriyet":cumhuriyet,"Milliyet":milliyet,"Habertürk":haberturk,"NTV":ntv,"Sabah":sabah,"Mynet":mynet,"Posta":posta,"Ensonhaber":ensonhaber}

def search(): #google news ana fonksiyon
    r = requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FuUnlHZ0pVVWlnQVAB?hl=tr&gl=TR&ceid=TR%3Atr") #haberlerin bulunduğu url
    soup = BeautifulSoup(r.content, "html5lib")
    news = soup.find_all("div",attrs={"class":"DBQmFf NclIid BL5WZb Oc0wGc xP6mwf j7vNaf"}) #haberlerin bulunduğu sıralı gruplar

    for new in news:

        source = new.find("a",attrs= {"class":"wEwyrc AVN2gc uQIVzc Sksgp slhocf"})
        source = source.get_text() #haberin hangi haber sitesine ait olduğunu alıyoruz

        link = new.find("a",attrs={"class":"VDXfz"} )   
        link = link.get("href")
        link= ("https://news.google.com"+link[1:]) # haber sitesinin adresine giden url

        
        if source in scrapper_tools: #Haber kaynağı bizim haber sitelerimizle eşleşiyorsa    
            scrapper_tools[source](link) # O kaynaktaki kazıma fonksiyonumuza url gönder ve baslat!

# UYGULAMA DURDURULANA KADAR ÇALIŞSIN VE TARAMAYA DEVAM ETSIN            
while True:
    search()


