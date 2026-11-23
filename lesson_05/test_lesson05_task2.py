from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    base_url = "https://httpbin.qa-territory.online/forms/post"
    driver.get(base_url)
    sleep(2)

    input_name = driver.find_element(By.NAME, "custname")
    input_name.send_keys("Илья")

    submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_btn.click()
    sleep(2)
    assert driver.current_url == base_url

    driver.quit()
