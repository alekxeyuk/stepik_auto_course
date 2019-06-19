from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")
    browser.find_element_by_id("answer").send_keys((lambda x: str(__import__('math').log(abs(12*__import__('math').sin(int(x))))))(browser.find_element_by_id("input_value").text))
    browser.execute_script("""document.getElementById("robotCheckbox").scrollIntoView();""") 
    list(map(lambda x: browser.find_element_by_css_selector(x).click(), ["[for='robotCheckbox']", "[for='robotsRule']", ".btn.btn-default"]))

except Exception as e:
    print(e)

finally:
    input()
    browser.close()
    browser.quit()
