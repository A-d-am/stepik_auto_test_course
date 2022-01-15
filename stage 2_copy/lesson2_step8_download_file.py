from selenium import webdriver
import os
import time
link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element_by_name("firstname")
    name.send_keys("vova")
    l_name = browser.find_element_by_name("lastname")
    l_name.send_keys("vovas")
    email = browser.find_element_by_name("email")
    email.send_keys("email")
    file_input = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    file_input.send_keys(file_path)
    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()
finally:
    time.sleep(5)
    browser.quit()