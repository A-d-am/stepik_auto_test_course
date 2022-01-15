from selenium import webdriver
import math



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    start_btn = browser.find_element_by_css_selector("[type='submit']")
    start_btn.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value").text
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(calc(int(x)))
    submit = browser.find_element_by_css_selector("[type='Submit']")
    submit.click()
    final_answer_alert = browser.switch_to.alert
    final_answer = final_answer_alert.text
    print(final_answer)
finally:
    browser.quit()
