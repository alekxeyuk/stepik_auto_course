from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/get_attribute.html")
    browser.find_element_by_css_selector("#answer").send_keys((lambda x: str(__import__('math').log(abs(12*__import__('math').sin(int(x))))))(browser.find_element_by_css_selector("#treasure").get_attribute('valuex')))
    list(map(lambda x: browser.find_element_by_css_selector(x).click(), ["#robotCheckbox", "#robotsRule", ".btn.btn-default"]))

except Exception as e:
    print(e)

finally:
    input()
    browser.close()
    browser.quit()
