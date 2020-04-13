import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # button = browser.find_element_by_css_selector("#book")

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")

    )
    button = browser.find_element_by_css_selector("#book")
    button.click()

    result = calc(browser.find_element_by_css_selector("#input_value").text)
    browser.find_element_by_css_selector("#answer").send_keys(result)

    button = browser.find_element_by_css_selector("#solve")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
