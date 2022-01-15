from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    answer = num1 + num2
    answer_field = Select(browser.find_element_by_tag_name("select"))
    answer_field.select_by_value(str(answer))

    confirm = browser.find_element_by_css_selector("[type='Submit']")
    confirm.click()
finally:
    time.sleep(5)
    browser.quit()
