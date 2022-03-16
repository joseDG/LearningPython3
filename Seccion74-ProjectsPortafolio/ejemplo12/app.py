from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas
import csv
import time
import os

# This is for Firefox. Similarly if
# chrome is needed , then it has to be specified
webBrowser = webdriver.Chrome(executable_path=os.environ['PATH'])

# first tab. Open google.com in the first tab
webBrowser.get('https://web.whatsapp.com/')
with open("whats_app links.csv" , mode="r") as data:
    lf = csv.reader(data)
    list = list(lf)
print(list[59])


# second tab
# execute_script->Executes JavaScript snippet.
# Here the snippet is window.open that means, it
# opens in a new browser tab
time.sleep(30)
num_list = []
for i in range(59,78):
    try:
        webBrowser.execute_script(f"window.open('about:blank', 'tab{i+1}');")
        webBrowser.close()
        # It is switching to second tab now
        webBrowser.switch_to.window(f"tab{i+1}")
        # In the second tab, it opens geeksforgeeks
        webBrowser.get(f"{list[i][0]}")
        wait = WebDriverWait(webBrowser , 15)
        join = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="action-button"]'))).click()
        use_web = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fallback_block"]/div/div/a'))).click()
        join_grp = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div'))).click()
        time.sleep(4)
        numb = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/header/div[2]/div[2]/span')))
        print(numb.text)
        num_list.append(numb.text)

        time.sleep(3)
        try:
            menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/header/div[1]/div/img'))).click()
        except:
            numb.click()

            exit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div/div[2]/div/span'))).click()
            exit_confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div'))).click()
            continue

        time.sleep(3)
        exit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[6]/div/div[2]/div/span'))).click()
        exit_confirm = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div'))).click()
    except:
        continue

df = pandas.DataFrame(num_list)
df.to_csv("data2.csv", index=False)