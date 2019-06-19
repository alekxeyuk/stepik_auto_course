from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin

def func(x): return str(log(abs(12*sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR')
    )
    browser.find_element_by_id('book').click()
    browser.find_element_by_id("answer").send_keys(
        func(browser.find_element_by_id("input_value").text)
    )
    browser.find_element_by_css_selector("#solve").click()

except Exception as e:
    print(e)

finally:
    input()
    browser.close()
    browser.quit()
