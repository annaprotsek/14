import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
SAVE_FOLDER = "programming_images"
SEARCH_URL = "https://www.pexels.com/search/programming/"
NUM_IMAGES = 5
os.makedirs(SAVE_FOLDER, exist_ok=True)
driver = webdriver.Chrome()
driver.get(SEARCH_URL)
img_elements = driver.find_elements(By.TAG_NAME, "img")[:NUM_IMAGES]

for i, img_element in enumerate(img_elements):
    img_url = img_element.get_attribute("src")
    if img_url:
        img_data = requests.get(img_url).content
        img_path = os.path.join(SAVE_FOLDER, f"image_{i + 1}.jpg")
        with open(img_path, "wb") as file:
            file.write(img_data)
        print(f"Зображення {i + 1} збережено: {img_path}")

driver.quit()
