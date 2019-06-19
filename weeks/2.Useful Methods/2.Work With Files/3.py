from selenium import webdriver
import os 
file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'debug.log')  

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")
    list(map(lambda x: browser.find_element_by_css_selector(x).send_keys(file_path), ["[id='file']", "[name='firstname']", "[name='lastname']", "[name='email']"]))
    browser.find_element_by_css_selector(".btn.btn-primary").click()

except Exception as e:
    print(e)

finally:
    input()
    browser.close()
    browser.quit()
