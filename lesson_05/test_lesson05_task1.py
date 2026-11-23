from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_navigation():
    driver = webdriver.Chrome()
    base_url = "https://httpbin.qa-territory.online/"

    driver.get(base_url)

    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    sleep(2)
    assert driver.current_url.endswith("/forms/post")

    driver.back()
    sleep(2)
    assert driver.current_url == base_url
    driver.quit()
