from selenium import webdriver
import sys, time

while True:
    # Code executed here
    driver=webdriver.Chrome()
    driver.get("https://mycutebaby.in/contest/participant/?n=5f094b39f3bde")
    driver.implicitly_wait(5)
    elem1 = driver.find_element_by_css_selector('a.vote-btn')
    elem1.get_attribute("href")
    elem1.click()
    time.sleep(1830)
