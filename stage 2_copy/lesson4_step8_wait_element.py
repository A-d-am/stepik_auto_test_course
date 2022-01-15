from selenium import webdriver
import math
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    book = browser.find_element_by_id("book")
    WebDriverWait(browser,13).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book.click()
    x = browser.find_element_by_id("input_value").text
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(calc(x))
    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()
    final_answer_alert = browser.switch_to.alert
    final_answer = final_answer_alert.text
    print(final_answer)
finally:
    browser.quit()
