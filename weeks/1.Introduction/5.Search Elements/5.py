from selenium import webdriver
import time

try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector(".first_block>.first_class .form-control").send_keys("Ivan")
    browser.find_element_by_css_selector(".first_block>.second_class .form-control").send_keys("Petrov")
    browser.find_element_by_css_selector(".first_block>.third_class .form-control").send_keys("Smolensk")
    browser.find_element_by_css_selector(".second_block>.first_class .form-control").send_keys("Russia")
    browser.find_element_by_css_selector(".second_block>.second_class .form-control").send_keys("AAaaAA")
    browser.find_element_by_class_name("btn").click()
    time.sleep(1)

    assert "Поздравляем! Вы успешно зарегистировались!" == browser.find_element_by_tag_name("h1").text

except Exception as e:
    print(e)

finally:
    browser.close()
    browser.quit()
