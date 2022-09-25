import unittest
from scrappers import *

# FONKSIYONLARI TRY EXEPT İÇİNE ALDIM. BİR ERROR OLUŞMASI DURUMUNDA FALSE DÖNECEK YOKSA TRUE DONECEK
# LINKLERIMIZ SUREKLI DINAMIK OLARAK DEGISTIGI ICIN VE HER SAYFANIN ICERIGI DINAMIK OLDUGU ICIN KENDI LOGLAMA STRATEJIMI GELISTIRDIM
# BU SAYEDE UYGULAMA CALISIRKEN HATALARI GOREBILIYORUZ 


# BU KISIMDA VERDIGIMIZ GIRDI LINKLERINE GORE FOKSIYONLARIN TRUE DONMESINI TEST EDIYORUZ

class MyTest(unittest.TestCase):
    def testPosta(self):
        self.assertEqual(posta("https://www.posta.com.tr/ekonomi/eyt-ve-taserondan-sonra-yeni-mujde-sirada-vergi-dilimi-var-2563128"),True)

    def testMilliyet(self):
        self.assertEqual(milliyet("https://www.milliyet.com.tr/dunya/putinden-seferberlik-karari-kararnameyi-imzaladi-6830290"),True)
    
    def testHurriyet(self):
        self.assertEqual(hurriyet("https://www.hurriyet.com.tr/sporarena/stefan-kuntz-yuzumuze-yumrugu-yedik-nakavt-olmadik-42142713"),True)
    
    def testSozcu(self):
        self.assertEqual(sozcu("https://www.sozcu.com.tr/2022/gundem/soylunun-mitinginde-gokkusagi-renkli-semsiye-kapattirildi-7381891/"),True)
    
    def testEnsonhaber(self):
        self.assertEqual(ensonhaber("https://www.ensonhaber.com/3-sayfa/gaziosmanpasada-eski-elti-dehseti-yasandi"),True)
    
    def testNtv(self):
        self.assertEqual(ntv("https://www.ntv.com.tr/egitim/bursluluk-parasi-ne-zaman-yatacak-2022-2023-meb-iokbs-burs-ucreti-ne-kadar,C5iZXyauD0mj-kZ4-FaTgA"),True)
    
    def testCumhuriyet(self):
        self.assertEqual(cumhuriyet("https://www.cumhuriyet.com.tr/siyaset/meral-aksener-sarayda-agirlandi-o-serefsiz-geregini-yapamadim-ozur-dilerim-1984875"),True)
    
    def testSabah(self):
        self.assertEqual(sabah("https://www.sabah.com.tr/galeri/yasam/son-dakika-thodex-davasinda-flas-gelisme-faruk-fatih-ozere-isyan-etti-tek-basina-zor-yapar"),True)
    
    def testMynet(self):
        self.assertEqual(mynet("https://www.mynet.com/pence-kilit-sehidi-piyade-ustegmen-serkan-erkus-a-son-veda-acili-kardes-herkese-nasip-olmaz-110107003882"),True)
    
    def testHaberturk(self):
        self.assertEqual(haberturk("https://www.haberturk.com/besiktas-ta-yasandi-ters-yon-diye-ambulansa-yol-vermedi-3523277"),True)
         
unittest.main(argv=[''], verbosity=2, exit=False)