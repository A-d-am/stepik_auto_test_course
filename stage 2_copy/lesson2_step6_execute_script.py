from selenium import webdriver
import math
import time

link = "http://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(int(x)))
    captcha = browser.find_element_by_id("robotCheckbox")
    captcha.click()
    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    submit = browser.find_element_by_css_selector("[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
finally:
    time.sleep(5)
    browser.quit()
