from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1')
    num1 = int(num1.text)

    num2 = browser.find_element_by_id('num2')
    num2 = int(num2.text)

    num_sum = num1 + num2

    dropdown = browser.find_element_by_id('dropdown')
    dropdown.click()

    value = browser.find_element_by_css_selector(f".custom-select [value='{num_sum}']")
    value.click()

    submit = browser.find_element_by_css_selector('.btn')
    submit.click()
    
    
finally:
    time.sleep(15)
    browser.quit()
