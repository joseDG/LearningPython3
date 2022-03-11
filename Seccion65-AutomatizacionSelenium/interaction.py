from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a")
#print(article_count.text)

#do click tag
all_portals = driver.find_element_by_partial_link_text("All portals")
#all_portals.click()

#metodo para buscar
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)