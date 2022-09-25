# NEWS SCRAPPER
# _PROJE HEDEFI_



- Bu projede bir çok haber kaynağından haberleri sunan "google news" sitesini mercek altına alacağız.
- Web kazıma işlemi ile sitelerden veri çekme işlemi yapacağız.
---
## CALISMA SEKLI

- Siz durdurana kadar haberleri çekmeye devam eder.
- Hataları log dosyasına kaydeder.
- Çekilen haberleri json dosyasına kaydeder.
- Haber gorsellerini MEDIA klasorune haber baslıgı adında kaydeder.
---

# _VERSION 0.0.0_
---
## GEREKLI MODULLER
- requests, bs4, json, os, unittest
---

## _app.py_
- app.py oluşturuldu. Projenin çalıştırma dosyası.
- "google news" sitesinden tüm haberleri gezerek onların "hangi haber kaynağından geldiğini" ve "url" bilgisini aldığımız bölüm.
- Bu aldığımız bilgiler örn. "Milliyet" ve "www.millet.com/haber"
- İçerisinde scrappers.py dosyasında oluşturduğumuz fonksiyonları barındıran sözlük yapımıza üstteki verileri verecek.
- Sözlük yapısı scrapper_tools= {"Milliyet":milliyet_funck} şeklinde.
- scrapper_tools["Milliyet"](haber linki) kodu bizim o siteye ait kazıma fonksiyonumuzu tetikleyecek ve kazıma işlemi başlayacak. 
- Kazıma işleminde bir hata olması durumunda hemen müdahale edebilmek için "log" lar tutulmakta.
- Hatayı hangi kaynaktan ve hangi url de hata olduğunu "logs.txt" dosyasına kaydetmeteyiz.
- Bu versiyonda 30 kayıttan ortalama 2-10 arası hata oluşmakta.
- Geliştirmeler devam ediyor.



---
## _scrappers.py_
- scrappers.py dosyası oluşturuldu.
- İçinde 10 adet sitenin veri çekme fonksiyonu bulunmakta.
- İlk fonksiyonda detaylı yorum satırları bulunmakta. Diğer fonksiyonlar aynı işlemi gördüğü için yazılmasına gerek duyulmadı.
- Güncellemelerde fonksiyonlar için bir "class" yapısı kurulacak.
- app.py dosyasından gelen "url" direkt olarak ilgili fonksiyona girerek kazıma işlemine başlanır.
- Kazımada bir hata oluşmazsa haberin dosyada olup olmadığı kontrol edilir burda da bir sorun yoksa "news.json" dosyasına haberler yazılır.
---
## _news.json_
- Elde edilen verilerin yazıldığı dosya.
---
## _LOGS/logs.txt_
- Hataları tespit edip gidermek için oluşturulmuş log dosyası.
---
## _MEDIA_
- Haberlere ait varsa gorsellerin indirilip kaydedildiği dosya. Goruntu yoksa ve ya goruntu bir videoysa kaydedilmez.
---
# _YAPILACAK YENILIKLER_
- Oluşan log'ların detaylı incelenmesi. 
- Bazı haberlerde verilerin farklı yerlerde bulunmasına çözümler getirilmesi.
- Orn. Ensonhaber sitesinden gelen verilerde çok boşluk olması gibi sorunlara çözümler.
- Tarih formatının tüm haberler için aynı forma getirilmesi.
- json dosyasına verilerin yazım şeklinin düzenlenmesi.
- log.txt dosyasına yazılan loglar hangi haber kaynagı -> haber url şeklinde şu an. Burada hatanın hangi kaynaktan hangi urlde hangi verinin çekilmesinde yaşandığını gösterecek şekilde düzenlenmesi.
- Sistemin iyileştirilmesi ve optimize edilmesi.
