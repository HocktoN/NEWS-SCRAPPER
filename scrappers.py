from bs4 import BeautifulSoup
import requests
import json
import os

def milliyet(link):

    try:
        # HABER LINKININ KARSILANMASI VE ICERIGININ PARSE ISLEMI
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html5lib") 

        # KAYNAK
        kaynak = "Milliyet" 

        # ORIGINAL LINK
        original_link = r.url

        # HABER BASLIGI
        title = soup.find("h1",attrs={"class":"nd-article__title"}).get_text() 

        # HABER TARIHI
        time = soup.find("div",attrs={"class":"nd-article__info-block"}).get_text()[:18] 

        # HABER KISA ICERIK
        shortContent = soup.find("h2",attrs={"class":"nd-article__spot"}).get_text() 

        # HABER ICERIK
        content = ""
        content1 = soup.find("div",attrs={"class":"nd-content-column"}) #içerik
        content1 = content1.find_all("p")
        for text in content1:
            content = content + text.text

        # HABER GORSELI   
        try:
            image = soup.find("div",attrs={"class":"nd-article__spot-img"}) 
            image = image.find("img")['data-src']

            #GORSELIN ADI HABER BASLIGI OLACAK SEKILDE "MEDIA" DOSYASINA KAYIT ISLEMI
            filename = (f'MEDIA/{title}.jpg')
            img_data = requests.get(image).content

            #GORSEL KLASORDE YOKSA KAYDET
            if not os.path.exists(filename):
                with open(f'MEDIA/{title}.jpg', 'wb') as handler: 
                    handler.write(img_data)

        # EGER GORSEL ALINMADIYSA
        except:
            image = "Goruntu alinamadi. Ana gorsel video olabilir."

        # VERILERDEN BIR SOZLUK OLUSTURMA
        dicti = {"Kaynak":kaynak,"Title":title,"Short Content":shortContent,"Content":content,"Time":time,"Original Link":original_link,"Image":image}

        # VERILERIN YAZILACAGI JSON DOSYASINI KONTROL
        with open("news.json", "r",encoding=("utf-8")) as outfile: 
            x = outfile.read() #okunması
                
            json_object = json.dumps(dicti,indent=4) #verileri içinde barındıran sözlüğün json dönüşümü

            # VERILER ICINDE YOKSA KAYDET
            if json_object not in x: 

                with open("news.json", "a",encoding="utf-8") as outfile: #"append" modunda acılması
                            
                    outfile.write(json_object) #dosyaya haberi yaz.
                    print("Yeni haber kaydedildi!")

    # HATA VARSA FALSE DON VE HATANIN KAYNAĞINI VE LİNKİNİ LOG DOSYASINA KAYDET               
    except:
            message = (f"{kaynak} sitesinden haber çekme fonksiyonunda veri çekmede hata var. Sikintili link : {original_link} . Geri bildirim oluşturulmuştur.\n")

            with open("LOGS/logs.txt","r",encoding="utf-8") as file: #Kod sürekli çalışacağından dolayı aynı kaydı tutmaması için  LOG dosyasını kontrol yapıyoruz.
                detail = file.read()

                if message not in detail: #eğer mesaj loglarda yoksa 
                    with open("LOGS/logs.txt","a",encoding="utf-8") as file: #log mesajını dosyaya yaz.
                        file.write(message)

                        print("Hata oluştu. LOGS/logs.txt dosyasini kontrol ediniz!")
            return False
    # HATA YOKSA TRUE 
    return True

def sozcu(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html5lib")

        kaynak = "Sozcu"

                
        original_link = r.url

        title = soup.find("div",attrs={"class":"col-lg-8 content mb-4"})
        title = title.find("h1").get_text()

        time = soup.find("time").text

        shortContent = soup.find("h2",attrs={"class":"spot"}).get_text()

        content = ""
        content1 = soup.find("div",attrs={"class":"col-lg-8 content mb-4"})
        content1 = content1.find_all("p")
        for p in content1:
            content = content+ p.text
            
        try:
            image = soup.find("div",attrs={"class":"main-img _16x9"})
            image = image.find("div",attrs={"class":"img-holder"})
            image = image.find("img")['src']

            filename = (f'MEDIA/{title}.jpg')
            img_data = requests.get(image).content

            if not os.path.exists(filename):
                with open(f'MEDIA/{title}.jpg', 'wb') as handler: 
                    handler.write(img_data) 
            
        except:
            image = "Goruntu alinamadi. Ana gorsel video olabilir."

        dicti = {"Kaynak":kaynak,"Title":title,"Short Content":shortContent,"Content":content,"Time":time,"Original Link":original_link,"Image":image}

        with open("news.json", "r",encoding=("utf-8")) as outfile:
            x = outfile.read()
                
            json_object = json.dumps(dicti,indent=4)

            if json_object not in x:

                with open("news.json", "a",encoding="utf-8") as outfile:
                            
                    outfile.write(json_object)
                    print("Yeni haber kaydedildi!")
    except:
            message = (f"{kaynak} sitesinden haber çekme fonksiyonunda veri çekmede hata var. Sikintili link : {original_link} . Geri bildirim oluşturulmuştur.\n")

            with open("LOGS/logs.txt","r",encoding="utf-8") as file: #Kod sürekli çalışacağından dolayı aynı kaydı tutmaması için kontrol yapıyoruz.
                detail = file.read()

                if message not in detail: #eğer 
                    with open("LOGS/logs.txt","a",encoding="utf-8") as file: #log mesajını dosyaya yaz.
                        file.write(message)

                        print("Hata oluştu. LOGS/logs.txt dosyasini kontrol ediniz!")
            return False        
    return True

def hurriyet(link):

    try:
    
        r = requests.get(link)

        soup = BeautifulSoup(r.content, "html5lib")

        kaynak = "Hürriyet"
        original_link = r.url

        title = soup.find("h1",attrs={"class":"news-detail-title"}).text

        time = soup.find("time").text

        shortContent = soup.find("div",attrs={"class":"news-content__inf"})
        shortContent = shortContent.find("h2").text

        content = soup.find("div",attrs={"class":"news-content readingTime"})

        content = content.find("p").text


        try:
            image = soup.find("div",attrs={"class":"news-media"})
            image = image.find("img")['src']
            filename = (f'MEDIA/{title}.jpg')
            img_data = requests.get(image).content

            if not os.path.exists(filename):
                with open(f'MEDIA/{title}.jpg', 'wb') as handler: 
                    handler.write(img_data)         
        except:
            image= "Gorsel alinamadi ve ya ana görsel bir video."

        dicti = {"Kaynak":kaynak,"Title":title,"Short Content":shortContent,"Content":content,"Time":time,"Original Link":original_link,"Image":image}

        with open("news.json", "r",encoding=("utf-8")) as outfile:
            x = outfile.read()
            
            json_object = json.dumps(dicti,indent=4)

            if json_object not in x:

                with open("news.json", "a",encoding="utf-8") as outfile:
                        
                    outfile.write(json_object)
                    print("Yeni haber kaydedildi!")
    except:
            message = (f"{kaynak} sitesinden haber çekme fonksiyonunda veri çekmede hata var. Sikintili link : {original_link} . Geri bildirim oluşturulmuştur.\n")

            with open("LOGS/logs.txt","r",encoding="utf-8") as file: #Kod sürekli çalışacağından dolayı aynı kaydı tutmaması için kontrol yapıyoruz.
                detail = file.read()

                if message not in detail: #eğer 
                    with open("LOGS/logs.txt","a",encoding="utf-8") as file: #log mesajını dosyaya yaz.
                        file.write(message)

                        print("Hata oluştu. LOGS/logs.txt dosyasini kontrol ediniz!")
            return False
    return True

def haberturk(link):

    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html5lib")

        kaynak = "Haberturk"

        original_link = r.url

        title = soup.find("h1",attrs={"class":"title"}).get_text()


        time = soup.find("span",attrs={"class":"date"}).get_text()[:18]


        shortContent = soup.find("h2",attrs={"class":"spot-title"}).get_text()

        try:
            content = ""
            content1 = soup.find("article",attrs={"class":"content type1"})
            content1 = content1.find_all("p")
            for text in content1:
                content = content + text.text
        except:
            try:
                content1 = soup.find("article",attrs={"class":"content type1"})
                content = content1.find("p").text
            except:
                pass

        try:
            image = soup.find("div",attrs={"class":"img"})
            image = image.find("img")['src']
            filename = (f'MEDIA/{title}.jpg')
            img_data = requests.get(image).content

            if not os.path.exists(filename):
                with open(f'MEDIA/{title}.jpg', 'wb') as handler: 
                    handler.write(img_data) 


        except:
            image = "Goruntu alinamadi ve ya ana görsel bir video."


        dicti = {"Kaynak":kaynak,"Title":title,"Short Content":shortContent,"Content":content,"Time":time,"Original Link":original_link,"Image":image}


        
        with open("news.json", "r",encoding=("utf-8")) as outfile:
            x = outfile.read()
                
            json_object = json.dumps(dicti,indent=4)

            if json_object not in x:

                with open("news.json", "a",encoding="utf-8") as outfile:
                            
                    outfile.write(json_object)
                    print("Yeni haber kaydedildi!")
    except:
            message = (f"{kaynak} sitesinden haber çekme fonksiyonunda veri çekmede hata var. Sikintili link : {original_link} . Geri bildirim oluşturulmuştur.\n")

            with open("LOGS/logs.txt","r",encoding="utf-8") as file: #Kod sürekli çalışacağından dolayı aynı kaydı tutmaması için kontrol yapıyoruz.
                detail = file.read()

                if message not in detail: #eğer 
                    with open("LOGS/logs.txt","a",encoding="utf-8") as file: #log mesajını dosyaya yaz.
                        file.write(message)

                        print("Hata oluştu. LOGS/logs.txt dosyasini kontrol ediniz!")
            return False
    return True

def cumhuriyet(link):

    try:

        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html5lib")

        kaynak = "Cumhuriyet"

        original_link = r.url

        title = soup.find("h1",attrs={"class":"baslik"}).get_text()


        time = soup.find("div",attrs={"class":"yayin-tarihi"}).get_text()


        shortContent = soup.find("h2",attrs={"class":"spot"}).get_text()


        content = ""
        content1 = soup.find("div",attrs={"class":"col-sm-8 col-md-8 col-lg-8"})
        content1 = content1.find_all("p")
        for text in content1:
            content = content + text.text
                    
        try:
            image = soup.find("div",attrs={"class":"col-sm-8 col-md-8 col-lg-8"})
            image = image.find("img")['src']
            image = "https://www.cumhuriyet.com.tr"+image

            filename = (f'MEDIA/{title}.jpg')
            img_data = requests.get(image).content

            if not os.path.exists(filename):
                with open(f'MEDIA/{title}.jpg', 'wb') as handler: 
                    handler.write(img_data)         

        except:
            image = "Goruntu alinamadi ve ya ana gorsel bir video."
        

        dicti = {"Kaynak":kaynak,"Title":title,"Short Content":shortContent,"Content":content,"Time":time,"Original Link":original_link,"Image":image}

        with open("news.json", "r",encoding=("utf-8")) as outfile:
            x = outfile.read()
                
            json_object = json.dumps(dicti,indent=4)

            if json_object not in x:

                with open("news.json", "a",encoding="utf-8") as outfile:
                            
                    outfile.write(json_object)
                    print("Yeni haber kaydedildi!")
    except:
            message = (f"{kaynak} sitesinden haber çekme fonksiyonunda veri çekmede hata var. Sikintili link : {original_link} . Geri bildirim oluşturulmuştur.\n")

            with open("LOGS/logs.txt","r",encoding="utf-8") as file: #Kod sürekli çalışacağından dolayı aynı kaydı tutmaması için kontrol yapıyoruz.
                detail = file.read()

                if message not in detail: #eğer 
                    with open("LOGS/logs.txt","a",encoding="utf-8") as file: #log mesajını dosyaya yaz.
                        file.write(message)

                        print("Hata oluştu. LOGS/logs.txt dosyasini kontrol ediniz!")
            return False
    return True

def ntv(link):

    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html5lib")

        kaynak = "NTV"

        original_link = r.url

        title = soup.find("h1",attrs={"class":"category-detail-title"}).get_text()

        time = soup.find("p",attrs={"class":"news-info-text--first"})
        time = time.find_all("span")[-1].text

        shortContent = soup.find("h2",attrs={"class":"category-detail-sub-title"}).get_text()

        content = ""
        content1 = soup.find("div",attrs={"class":"category-detail-content-inner"})
        content1 = content1.find_all("p")
        for text in content1:
            content = content + text.text
            
        try:
            image = soup.find("picture",attrs={"class":"native-lazy"})
            image = image.find("img")['data-src']

            filename = (f'MEDIA/{title}.jpg')
            img_data = requests.get(image).content

            if not os.path.exists(filename):
                with open(f'MEDIA/{title}.jpg', 'wb') as handler: 
                    handler.write(img_data) 
        except:
            image = "Goruntu alinamadi ve ya ana görsel bir video."

        dicti = {"Kaynak":kaynak,"Title":title,"Short Content":shortContent,"Content":content,"Time":time,"Original Link":original_link,"Image":image}

        with open("news.json", "r",encoding=("utf-8")) as outfile:
            x = outfile.read()
                
            json_object = json.dumps(dicti,indent=4)

            if json_object not in x:

                with open("news.json", "a",encoding="utf-8") as outfile:
                            
                    outfile.write(json_object)
                    print("Yeni haber kaydedildi!")
    except:
            message = (f"{kaynak} sitesinden haber çekme fonksiyonunda veri çekmede hata var. Sikintili link : {original_link} . Geri bildirim oluşturulmuştur.\n")

            with open("LOGS/logs.txt","r",encoding="utf-8") as file: #Kod sürekli çalışacağından dolayı aynı kaydı tutmaması için kontrol yapıyoruz.
                detail = file.read()

                if message not in detail: #eğer 
                    with open("LOGS/logs.txt","a",encoding="utf-8") as file: #log mesajını dosyaya yaz.
                        file.write(message)

                        print("Hata oluştu. LOGS/logs.txt dosyasini kontrol ediniz!")
            return False
    return True

def sabah(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html5lib")

        kaynak = "Sabah"
        original_link = r.url

        title= soup.find("h1",attrs={"class":"pageTitle"}).get_text()

        time = soup.find("span",attrs={"class":"textInfo align-center"})
        time = time.find_all("span")[0].text[14:]

        try:
            shortContent = soup.find("h2",attrs={"class":"spot view20"}).get_text()
        except:
            try: 
                shortContent = soup.find("div",attrs={"class":"col-sm-12 view5"})
                shortContent = shortContent.find("h2",attrs={"class":"spot"}).get_text()
                
            except:
                pass

        content = ""

        contentt = soup.find_all("div",attrs={"class":"galleryItem"})

        for cont in contentt:
            content = content+(cont.find("p").text)

        if content == "":
            contentt = soup.find("div",attrs={"class":"newsDetailText"}).get_text()
            content = contentt
            
        try:
            image = soup.find("figure",attrs={"class":"newsImage"})
            image = image.find("img")
            image = image['src']
            filename = (f'MEDIA/{title}.jpg')
            img_data = requests.get(image).content

            if not os.path.exists(filename):
                with open(f'MEDIA/{title}.jpg', 'wb') as handler: 
                    handler.write(img_data) 
        
        except:
            image = "Goruntu alinmadi ve ya ana gorsel bir video."


        dicti = {"Kaynak":kaynak,"Title":title,"Short Content":shortContent,"Content":content,"Time":time,"Original Link":original_link,"Image":image}


        with open("news.json", "r",encoding=("utf-8")) as outfile:
            x = outfile.read()
                
            json_object = json.dumps(dicti,indent=4)

            if json_object not in x:

                with open("news.json", "a",encoding="utf-8") as outfile:
                            
                    outfile.write(json_object)
                    print("Yeni haber kaydedildi!")
    except:
            message = (f"{kaynak} sitesinden haber çekme fonksiyonunda veri çekmede hata var. Sikintili link : {original_link} . Geri bildirim oluşturulmuştur.\n")

            with open("LOGS/logs.txt","r",encoding="utf-8") as file: #Kod sürekli çalışacağından dolayı aynı kaydı tutmaması için kontrol yapıyoruz.
                detail = file.read()

                if message not in detail: #eğer 
                    with open("LOGS/logs.txt","a",encoding="utf-8") as file: #log mesajını dosyaya yaz.
                        file.write(message)

                        print("Hata oluştu. LOGS/logs.txt dosyasini kontrol ediniz!")
            return False
    return True

def mynet(link):

    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html5lib")

        kaynak = "Mynet"

        original_link = r.url

        title= soup.find("h1",attrs={"class":"post-title mb-3"}).get_text()

        time = soup.find("span",attrs={"class":"created-date"}).text[:-1]

        shortContent = soup.find("h2",attrs={"class":"post-spot mb-0 pt-2 pb-2"}).get_text()

        content = ""

        contentt = soup.find("div",attrs={"class":"detail-content-inner"})
        contentt = contentt.find_all("p")


        for cont in contentt:
            content = content+ cont.text
            
        try:
            image = soup.find("img",attrs="img-responsive")['src']
            filename = (f'MEDIA/{title}.jpg')
            img_data = requests.get(image).content

            if not os.path.exists(filename):
                with open(f'MEDIA/{title}.jpg', 'wb') as handler: 
                    handler.write(img_data) 
        except:
            image = "Goruntu alinamadi ve ya ana gorsel bir video."
        
        dicti = {"Kaynak":kaynak,"Title":title,"Short Content":shortContent,"Content":content,"Time":time,"Original Link":original_link,"Image":image}

        with open("news.json", "r",encoding=("utf-8")) as outfile:
            x = outfile.read()
                
            json_object = json.dumps(dicti,indent=4)

            if json_object not in x:

                with open("news.json", "a",encoding="utf-8") as outfile:
                            
                    outfile.write(json_object)
                    print("Yeni haber kaydedildi!")
    except:
            message = (f"{kaynak} sitesinden haber çekme fonksiyonunda veri çekmede hata var. Sikintili link : {original_link} . Geri bildirim oluşturulmuştur.\n")

            with open("LOGS/logs.txt","r",encoding="utf-8") as file: #Kod sürekli çalışacağından dolayı aynı kaydı tutmaması için kontrol yapıyoruz.
                detail = file.read()

                if message not in detail: #eğer 
                    with open("LOGS/logs.txt","a",encoding="utf-8") as file: #log mesajını dosyaya yaz.
                        file.write(message)

                        print("Hata oluştu. LOGS/logs.txt dosyasini kontrol ediniz!")
            return False
    return True

def ensonhaber(link):

    try:

        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html5lib")

        kaynak = "Ensonhaber"

        original_link = r.url

        title= soup.find("h1",attrs={"class":"c-title"}).get_text().replace(" ","")

        time = []
        for ultag in soup.find_all('div', {'class': 'c-date'}):
            for litag in ultag.find_all('li'):
                time.append(litag.text)
                
        time = time[0]
                
        shortContent = soup.find("div",attrs={"class":"c-desc"}).get_text()

        content = ""

        contentt = soup.find("article",attrs={"class":"body"})
        contentt = contentt.find_all("p")

        for i in contentt:
            content = content+ i.text

        try:
            image = soup.find("figure",attrs={"class":"headline-img"})
            image = image.find("img")['src']

            filename = (f'MEDIA/{title}.jpg')
            img_data = requests.get(image).content

            if not os.path.exists(filename):
                with open(f'MEDIA/{title}.jpg', 'wb') as handler: 
                    handler.write(img_data) 
        except:
            image = "Goruntu alinamadi ve ya ana gorsel bir video."

        dicti = {"Kaynak":kaynak,"Title":title,"Short Content":shortContent,"Content":content,"Time":time,"Original Link":original_link,"Image":image}

        with open("news.json", "r",encoding=("utf-8")) as outfile:
            x = outfile.read()
                
            json_object = json.dumps(dicti,indent=4)

            if json_object not in x:

                with open("news.json", "a",encoding="utf-8") as outfile:
                            
                    outfile.write(json_object)
                    print("Yeni haber kaydedildi!")
    except:
            message = (f"{kaynak} sitesinden haber çekme fonksiyonunda veri çekmede hata var. Sikintili link : {original_link} . Geri bildirim oluşturulmuştur.\n")

            with open("LOGS/logs.txt","r",encoding="utf-8") as file: #Kod sürekli çalışacağından dolayı aynı kaydı tutmaması için kontrol yapıyoruz.
                detail = file.read()

                if message not in detail: #eğer 
                    with open("LOGS/logs.txt","a",encoding="utf-8") as file: #log mesajını dosyaya yaz.
                        file.write(message)

                        print("Hata oluştu. LOGS/logs.txt dosyasini kontrol ediniz!")
            return False
    return True

def posta(link):

    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html5lib")

        kaynak = "Posta"

        original_link = r.url

        title= soup.find("h1",attrs={"class":"rhd-article-title"}).get_text()

        time = soup.find("span",attrs={"class":"rhd-time-box-text rgc_date"}).text

        shortContent = soup.find("h2",attrs={"class":"rhd-article-spot"}).get_text()

        content = ""

        contentt = soup.find_all("h3",attrs={"class":"description"})
        for i in contentt:
            content = content+ i.text

        try:
            image = soup.find("div",attrs={"class":"_picture"})
            image = image.find("img")['data-src']

            filename = (f'MEDIA/{title}.jpg')
            img_data = requests.get(image).content

            if not os.path.exists(filename):
                with open(f'MEDIA/{title}.jpg', 'wb') as handler: 
                    handler.write(img_data) 
        except:
            image = "Goruntu alinamadi ve ya ana görsel bir video."

        dicti = {"Kaynak":kaynak,"Title":title,"Short Content":shortContent,"Content":content,"Time":time,"Original Link":original_link,"Image":image}

        with open("news.json", "r",encoding=("utf-8")) as outfile:
            x = outfile.read()
                
            json_object = json.dumps(dicti,indent=4)

            if json_object not in x:

                with open("news.json", "a",encoding="utf-8") as outfile:
                            
                    outfile.write(json_object)
                    print("Yeni haber kaydedildi!")
    except:
            message = (f"{kaynak} sitesinden haber çekme fonksiyonunda veri çekmede hata var. Sikintili link : {original_link} . Geri bildirim oluşturulmuştur.\n")

            with open("LOGS/logs.txt","r",encoding="utf-8") as file: #Kod sürekli çalışacağından dolayı aynı kaydı tutmaması için kontrol yapıyoruz.
                detail = file.read()

                if message not in detail: #eğer 
                    with open("LOGS/logs.txt","a",encoding="utf-8") as file: #log mesajını dosyaya yaz.
                        file.write(message)

                        print("Hata oluştu. LOGS/logs.txt dosyasini kontrol ediniz!")
            return False
    return True

    