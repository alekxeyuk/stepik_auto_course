from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")
    Select(browser.find_element_by_tag_name("select")).select_by_value(str(sum(map(lambda x: int(browser.find_element_by_id(x).text), ["num1", "num2"]))))
    list(map(lambda x: browser.find_element_by_css_selector(x).click(), [".btn.btn-default"]))

except Exception as e:
    print(e)

finally:
    input()
    browser.close()
    browser.quit()
