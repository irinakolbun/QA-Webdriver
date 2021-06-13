from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

group_name = "іп-92"

driver = webdriver.Safari()
driver.get("http://rozklad.kpi.ua")
rozklad = driver.find_element_by_css_selector('[id="ctl00_lBtnSchedule"]')
WebDriverWait(driver, 10).until(ec.visibility_of(rozklad))
rozklad.click()
sleep(1)
group = driver.find_element_by_css_selector('[id="ctl00_MainContent_ctl00_txtboxGroup"]')
WebDriverWait(driver, 10).until(ec.visibility_of(group))
group.send_keys(group_name)
group.send_keys(Keys.RETURN)
sleep(2)
item = driver.find_element_by_css_selector('[id="ctl00_MainContent_lblHeader"]')

assert item.text == f'Розклад занять для {group_name.upper()}', 'Invalid group'
print("Test passed")
sleep(10)
driver.quit()
