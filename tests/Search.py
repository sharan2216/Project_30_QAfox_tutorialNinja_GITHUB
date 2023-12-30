import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_for_valid_products():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)
    expected_title = "Your Store"
    actual_title = driver.title
    if actual_title.__eq__(expected_title):
        print("Title Matched")
    time.sleep(2)
    assert expected_title.__eq__(actual_title)
    driver.find_element(By.NAME, "search").send_keys("HP")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default btn-lg')]").click()
    time.sleep(2)
    print("NEXT ASSERTION line printed here")
    ele = driver.find_element(By.LINK_TEXT, "HP LP3065")
    assert ele.is_displayed()

    driver.quit()