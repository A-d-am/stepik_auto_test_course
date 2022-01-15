from selenium import webdriver
import time
import math
link = " http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(int(x)))
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    submit = browser.find_element_by_css_selector('[type="Submit"]')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()