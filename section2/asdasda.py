from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    first_field = browser.find_element_by_name('firstname')
    first_field.send_keys('first')
    second_field = browser.find_element_by_name('lastname')
    second_field.send_keys('second')
    third_field = browser.find_element_by_name('email')
    third_field.send_keys('third')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')

    submit = browser.find_element_by_id('file')
    submit.send_keys(file_path)
    

    button = browser.find_element_by_tag_name('button')
    button.click()
    

finally:
    time.sleep(10)
    browser.quit()
