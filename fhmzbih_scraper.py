import bs4
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Access environment variables using os.environ
url = os.environ.get('FHMZBIH')

proxies = {
    'http': 'http://93.157.196.58:8080'
    # 'https': 'http://proxyprovider.com:2000',
}

AQ_value = requests.get(url, proxies=proxies)
AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')

i = 0
with open('index.html', 'w') as f:
    for x in AQ_value_soup.select('tr td'):
        f.write(str(i)+" "+str(x) + "\n")
        i = i+1

class Sarajevo:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')

        self.bjelave_pm10 = AQ_value_soup.select('tr td')[26].text
        self.bjelave_pm25 = AQ_value_soup.select('tr td')[27].text
        self.ivan_sedlo_pm10 = AQ_value_soup.select('tr td')[34].text        
        self.ivan_sedlo_pm25 = AQ_value_soup.select('tr td')[35].text
        self.vijecnica_pm10 = AQ_value_soup.select('tr td')[43].text
        self.vijecnica_pm25 = AQ_value_soup.select('tr td')[44].text
        self.otoka_pm10 = AQ_value_soup.select('tr td')[51].text
        self.otoka_pm25 = AQ_value_soup.select('tr td')[52].text
        self.ilidza_pm10 = AQ_value_soup.select('tr td')[59].text
        self.ilidza_pm25 = AQ_value_soup.select('tr td')[60].text
        self.vogosca_pm10 = AQ_value_soup.select('tr td')[67].text
        self.vogosca_pm25 = AQ_value_soup.select('tr td')[68].text
        self.hadzici_pm10 = AQ_value_soup.select('tr td')[75].text
        self.hadzici_pm25 = AQ_value_soup.select('tr td')[76].text
        self.ilijas_pm10 = AQ_value_soup.select('tr td')[83].text
        self.ilijas_pm25 = AQ_value_soup.select('tr td')[84].text

class Kakanj:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')

        self.doboj_pm10 = AQ_value_soup.select('tr td')[93].text
        self.doboj_pm25 = AQ_value_soup.select('tr td')[94].text

class Jajce:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')

        self.harmani_pm10 = AQ_value_soup.select('tr td')[112].text
        self.harmani_pm25 = AQ_value_soup.select('tr td')[113].text

class Travnik:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')

        self.centar_pm10 = AQ_value_soup.select('tr td')[121].text
        self.centar_pm25 = AQ_value_soup.select('tr td')[122].text

class Livno:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')

        self.centar_pm10 = AQ_value_soup.select('tr td')[148].text
        self.centar_pm25 = AQ_value_soup.select('tr td')[149].text

class Bihac:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')

        self.nova_cetvrt_pm10 = AQ_value_soup.select('tr td')[157].text
        self.nova_cetvrt_pm25 = AQ_value_soup.select('tr td')[158].text

class Mostar:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')

        self.bijeli_brijeg_pm10 = AQ_value_soup.select('tr td')[176].text
        self.bijeli_brijeg_pm25 = AQ_value_soup.select('tr td')[177].text

class Zenica:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')

        self.tetovo_pm10 = AQ_value_soup.select('tr td')[196].text
        self.tetovo_pm25 = AQ_value_soup.select('tr td')[197].text
        self.centar_pm10 = AQ_value_soup.select('tr td')[204].text
        self.centar_pm25 = AQ_value_soup.select('tr td')[205].text
        self.radakovo_pm10 = AQ_value_soup.select('tr td')[212].text
        self.radakovo_pm25 = AQ_value_soup.select('tr td')[213].text

class Visoko:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')

        self.centar_pm10 = AQ_value_soup.select('tr td')[230].text
        self.centar_pm25 = AQ_value_soup.select('tr td')[231].text

class Maglaj:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')
        
        self.centar_pm10 = AQ_value_soup.select('tr td')[239].text
        self.centar_pm25 = AQ_value_soup.select('tr td')[224].text

class Tesanj:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')
        
        self.vatrogasni_dom_pm10 = AQ_value_soup.select('tr td')[248].text
        self.vatrogasni_dom_pm25 = AQ_value_soup.select('tr td')[249].text

class Tuzla:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')

        self.trnovac_pm10 = AQ_value_soup.select('tr td')[258].text
        self.trnovac_pm25 = AQ_value_soup.select('tr td')[259].text
        self.skver_pm10 = AQ_value_soup.select('tr td')[267].text
        self.skver_pm25 = AQ_value_soup.select('tr td')[268].text
        self.bkc_pm10 = AQ_value_soup.select('tr td')[275].text
        self.bkc_pm25 = AQ_value_soup.select('tr td')[276].text

class Lukavac:
    def __init__(self):
        AQ_value = requests.get(url)
        AQ_value_soup = bs4.BeautifulSoup(AQ_value.text, 'lxml')
        
        self.centar_pm10 = AQ_value_soup.select('tr td')[301].text
        self.centar_pm25 = AQ_value_soup.select('tr td')[302].text

print (Lukavac().centar_pm10)