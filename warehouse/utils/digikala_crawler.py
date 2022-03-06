import time
import requests
from bs4 import BeautifulSoup

from rest_framework.exceptions import APIException

from decouple import config
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from warehouse.models import(
    Product,
    Pack,
    Color,
    Guarantee
)

def validate_url(url):
    status = requests.get(url)
    if status.status_code != 200:
        raise APIException('Invalid URL')

    if not url.startswith('https://www.digikala.com/search/'):
        raise APIException('Invalid URL')

class GetProducts:
    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.pages = kwargs.get('pages')
        browser =  self.web_driver()
        products = self.get_all_products(browser = browser)
        products_detail = self.get_products_details(browser= browser, products= products)

    def web_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--ignore-certificate-errors-spki-list')
        browser = webdriver.Chrome(
            options=options,
            executable_path=config('CHROME_DRIVER_PATH', cast=str)
        )
        return browser

    def get_all_products(self, browser):
        all_products=list()
        delay = 6

        for i in range(self.pages):
            broke= False
            tries = 0
            while True:
                browser.get(f"{self.url}&page={i+1}")
                if tries>5:
                    broke = True
                    break
                try:
                    WebDriverWait(browser, delay).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'w-100.radius-medium.lazyloaded'))
                    )
                    time.sleep(1)
                    break 
                except TimeoutException:
                    tries += 1
                    print ("Loading took too much time!-Try again")

            if broke == True:
                continue

            soup = BeautifulSoup(browser.page_source)
            new_source = soup.find('div',{"class": 'd-flex flex-wrap'}).find_all('a')
            links = [link['href'] for link in new_source if 'dkp' in link['href']]
            products_sku = [link.split("/")[2] for link in links]
            all_products.extend(products_sku)

        return all_products

    def get_products_details(self, browser, products):
        delay = 10

        for i in range(len(products)):
            browser.get(f"https://www.digikala.com/product/{products[i]}/")
            tries = 0
            while True:
                if tries>10:
                    break
                try:
                    WebDriverWait(browser, delay).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'pos-relative.d-flex.ai-center'))
                    )
                    time.sleep(2)
                    break 
                except TimeoutException:
                    tries += 1
                    print ("Loading took too much time!-Try again")

            soup = BeautifulSoup(browser.page_source)
            prod = Product.objects.create(
                title = soup.find('h1',{"class":'text-h4 color-900 mb-2'}).text.replace('\u200c',' '),
                sku= products[i],
                subtitle = soup.find('span',{"class": "color-300 ml-2 text-body-2"}).text,
                description = soup.find('div',{"class": "text-body-1 color-800"}).text.replace('\u200c',' '),
                rating = float(unidecode(soup.find('p',{"class": "mr-1 text-body-2"}).text))
            )

            colors = browser.find_elements_by_class_name("bg-000.d-flex.ai-center.jc-center.pointer.mb-2.ml-2.px-2.px-0-lg.VariantInfo_variantInfo__ibDSa")
            for j in range(len(colors)):
                try:
                    colors[j].click()
                except :
                    pass
                time.sleep(0.2)

                soup = BeautifulSoup(browser.page_source)
                price = int(unidecode(soup.find('span',{"class": "text-h4 ml-1 color-800"}).text).replace(',',''))
                color, status = Color.objects.get_or_create(
                    title=[col.text for col in soup.find_all('p',{"class": "grow-1 text-h5 color-900"})
                        if "رنگ" in col.text][0].split()[1]
                )
                guarantee, status = Guarantee.objects.get_or_create(
                    title=[col.text for col in soup.find_all('p',{"class": "text-button-2 color-700"})
                        if "گارانتی" in col.text][0]
                )

                Pack.objects.create(
                    price= price,
                    product= prod,
                    guarantee= guarantee,
                    color= color 
                    )