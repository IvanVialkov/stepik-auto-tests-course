from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')
    people_radio = browser.find_element_by_id("robotsRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert robots_checked is None
finally:
    time.sleep(10)
    browser.quit()
