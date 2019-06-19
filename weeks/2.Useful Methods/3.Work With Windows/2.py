from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/redirect_accept.html")
    browser.find_element_by_css_selector(".btn.btn-primary").click()
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_id("answer").send_keys((lambda x: str(__import__('math').log(abs(12*__import__('math').sin(int(x))))))(browser.find_element_by_id("input_value").text))
    browser.find_element_by_css_selector(".btn.btn-primary").click()

except Exception as e:
    print(e)

finally:
    input()
    browser.close()
    browser.quit()
