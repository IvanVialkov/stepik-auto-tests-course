from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element_by_css_selector('.btn').click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    submit = browser.find_element_by_css_selector('.btn')
    submit.click()
    
finally:
    time.sleep(10)
    browser.quit()
