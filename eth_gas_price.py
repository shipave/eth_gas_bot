import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_gas_price(url):
    """scraping a price value from cointool.app site"""
    service = Service('/Users/pavelshilkin/eth_gas/chromedriver/chromedriver')
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(url=url)
        time.sleep(3)

        html_code = driver.page_source
        soup = BeautifulSoup(html_code, 'lxml')
        items_div = soup.find_all('div', class_='numBox')
        gas_price_values = []
        for div in items_div:
            gas_price_value = div.find('span', class_='num').text.strip()
            gas_price_values.append(gas_price_value)

    except Exception as exception:
        print(exception)

    finally:
        driver.close()
        driver.quit()

    return gas_price_values
