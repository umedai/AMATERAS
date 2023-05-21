from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import pandas as pd
import pickle

options = Options()
PROFILE_PATH = r'C:\Users\umeda\Desktop\AMATERAS\app\UserData\Default'
options.add_argument('--user-data-dir=' + PROFILE_PATH)
driver = webdriver.Chrome(options=options)

url = "https://nft.amateras.io/#/app/Referral"


driver.get(url)


time.sleep(3)

driver.find_element(By.CSS_SELECTOR, ".mr-5").click()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "div:nth-child(8) span").click()

time.sleep(3)

driver.refresh()

time.sleep(15)

names = driver.find_elements(By.CLASS_NAME, "MyNFTList-card__name")
prices = driver.find_elements(By.CLASS_NAME, "nft-price_text")
numbers = driver.find_elements(By.CLASS_NAME, "MyNFTList-card__number")

namees = [name.text.split("\n") for name in names]

pricees = [price.text for price in prices]
pricees = [i.strip("Price:  AMT") for i in pricees]

numberes = [number.text for number in numbers]

pn = list(zip(pricees, numberes))


df1 = pd.DataFrame(namees)
df2 = pd.DataFrame(pn)

data = pd.concat([df1, df2], axis=1)

col = ["名前", "name", "price", "ID"]
data.columns = col

print(data)
with open("card_data.pickle", "wb") as f:
    pickle.dump(data, f)

