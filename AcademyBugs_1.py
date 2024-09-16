from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

def test():
    driver = Chrome(options=chrome_options)
    time.sleep(2)
    driver.get("https://academybugs.com/find-bugs/#")
    findbugs = driver.find_element(By.XPATH, "//a[@title = 'Find Bugs']")
    findbugs.click()
    view_elements = driver.find_element(By.LINK_TEXT, '10')
    view_elements.click()
    time.sleep(10)
    driver.close()

test()
