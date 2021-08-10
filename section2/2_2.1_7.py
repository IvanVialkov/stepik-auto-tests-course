from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)
    img = browser.find_element_by_id('treasure')
    x = img.get_attribute('valuex')
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    robot_check = browser.find_element_by_id('robotCheckbox')
    robot_check.click()

    robotsRule = browser.find_element_by_id('robotsRule')
    robotsRule.click()

    submit = browser.find_element_by_css_selector('.btn')
    submit.click()
    
finally:
    time.sleep(10)
    browser.quit()

