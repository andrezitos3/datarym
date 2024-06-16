from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


def pesquisarBanda(banda):

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service)
    driver.maximize_window()

    driver.get('https://en.wikipedia.org/wiki/Main_Page')
    listaGeneros = []

    search_box = driver.find_element(By.NAME, "search")
    botao = driver.find_element(By.XPATH, '//button[text()="Search"]')

    search_box.click()
    search_box.send_keys(banda)

    botao.click()

    try:
        generos = driver.find_element(By.XPATH, '//th[text()="Genres"]')

        td_element = generos.find_element(By.XPATH, './following-sibling::td')

        try:
            div = td_element.find_element(By.XPATH, './div')
            ul = div.find_element(By.XPATH, './ul')
            li = ul.find_elements(By.XPATH, './li')

            for li in li:
                listaGeneros.append(li.text)

        except NoSuchElementException:
            a = td_element.find_element(By.XPATH, './a')
            listaGeneros.append(a.text)

        #ul = div.find_element(By.XPATH, './ul')

        #li = ul.find_elements(By.XPATH, './li')

    except NoSuchElementException:
            print('')

    driver.quit()

    return listaGeneros
