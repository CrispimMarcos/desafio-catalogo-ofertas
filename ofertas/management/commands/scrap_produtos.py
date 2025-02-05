from django.core.management.base import BaseCommand
from ofertas.models import Produto
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def find_element_with_fallbacks(item, fallbacks):
    for method, selector in fallbacks:
        try:
            return item.find_element(method, selector)
        except NoSuchElementException:
            pass
    raise NoSuchElementException("Element not found with any of the given selectors")

def scraping_function():
    options = Options()
    options.headless = True

    chrome_driver_path = 'C:\\Users\\Administrador\\Documents\\Catalogo\\catalogo\\chromedriver.exe'
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    url = "https://lista.mercadolivre.com.br/computador-gamer-i7-16gb-ssd-1tb"
    driver.get(url)
    
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ui-search-result__wrapper')))

    products = []
    for item in driver.find_elements(By.CLASS_NAME, "ui-search-result__wrapper"):
        print("Item encontrado: ", item.text)

        fallbacks = [
            (By.CLASS_NAME, 'ui-search-result-image__element'),
            (By.CSS_SELECTOR, '.ui-search-result__image .ui-search-result-image__element'),
            (By.TAG_NAME, 'img')
        ]
        
        imagem_element = find_element_with_fallbacks(item, fallbacks)
        imagem = imagem_element.get_attribute('src')
        print("Imagem: ", imagem)

        try:
            nome = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-search-item__title'))).text
        except TimeoutException:
            print("Timeout ao esperar pelo elemento 'ui-search-item__title'")
            continue
        print("Nome: ", nome)

        try:
            preco = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'price-tag'))).text
        except TimeoutException:
            print("Timeout ao esperar pelo elemento 'price-tag'")
            continue
        print("Preço: ", preco)

        try:
            parcelamento = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-search-item__group__element'))).text
        except TimeoutException:
            print("Timeout ao esperar pelo elemento 'ui-search-item__group__element'")
            continue
        print("Parcelamento: ", parcelamento)

        try:
            link = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'a'))).get_attribute('href')
        except TimeoutException:
            print("Timeout ao esperar pelo elemento 'a'")
            continue
        print("Link: ", link)

        preco_sem_desconto = item.find_element(By.CLASS_NAME, 'ui-search-price__second-line__label').text if item.find_elements(By.CLASS_NAME, 'ui-search-price__second-line__label') else None
        print("Preço sem Desconto: ", preco_sem_desconto)

        percentual_desconto = item.find_element(By.CLASS_NAME, 'ui-search-price__second-line__label').text if item.find_elements(By.CLASS_NAME, 'ui-search-price__second-line__label') else None
        print("Percentual Desconto: ", percentual_desconto)

        tipo_entrega = 'Full' if 'full' in item.text.lower() else 'Normal'
        print("Tipo de Entrega: ", tipo_entrega)

        frete_gratis = 'Frete grátis' if 'frete grátis' in item.text.lower() else None
        print("Frete Grátis: ", frete_gratis)

        product = {
            'imagem': imagem,
            'nome': nome,
            'preco': preco,
            'parcelamento': parcelamento,
            'link': link,
            'preco_sem_desconto': preco_sem_desconto,
            'percentual_desconto': percentual_desconto,
            'tipo_entrega': tipo_entrega,
            'frete_gratis': frete_gratis
        }
        products.append(product)
    
    driver.quit()

    for product in products:
        Produto.objects.create(
            imagem=product['imagem'],
            nome=product['nome'],
            preco=product['preco'],
            parcelamento=product['parcelamento'],
            link=product['link'],
            preco_sem_desconto=product.get('preco_sem_desconto'),
            percentual_desconto=product.get('percentual_desconto'),
            tipo_entrega=product['tipo_entrega'],
            frete_gratis=bool(product['frete_gratis'])
        )

    print('Dados raspados e salvos com sucesso')

class Command(BaseCommand):
    help = 'Raspa dados de produtos do MercadoLivre e salva no banco de dados'

    def handle(self, *args, **kwargs):
        scraping_function()
