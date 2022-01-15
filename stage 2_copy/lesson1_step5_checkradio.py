from selenium import webdriver
import math
import time
link = " http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_css_selector("#input_value.nowrap")

    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x.text))

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    robot = browser.find_element_by_id("robotsRule")
    robot.click()

    confirm = browser.find_element_by_css_selector("[type='Submit']")
    confirm.click()

finally:
    time.sleep(15)
    browser.quit()