# Using Python Selenium and the URL https://www.cowin.gov.in/ you have to-

# Click on the "Create "FAQ" and "Partners anchor tag present on the Home Page and open two new windows.

# Now you have to fetch the opened windows/frame ID and display the same on the console.

# Kindly close the two new windows and come back to the home page also.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open the main page
url = "https://www.cowin.gov.in/"
driver = webdriver.Chrome()  # You can use other browser drivers like Firefox, Safari, etc.
driver.get(url)

# Click on "FAQ" link and open a new window
faq_link = driver.find_element(By.XPATH, "//a[normalize-space()='FAQ']")
faq_link.click()

# Click on "Partners" link and open another new window
partners_link = driver.find_element(By.XPATH, "//a[normalize-space()='Partners']")
partners_link.click()

# Get all window handles (main window + two new windows)
all_handles = driver.window_handles

# Display window/frame IDs on the console
for handle in all_handles:
    print(f"Window/Frame ID: {handle}")

# Close the two new windows and switch back to the main window
for handle in all_handles[1:]:
    driver.switch_to.window(handle)
    driver.close()

# Switch back to the main window
driver.switch_to.window(all_handles[0])

# Close the main window
driver.quit()

# Using Python Selenium Visit the URL https://labour.gov.in/. and do the following task given below-
# Goto the menu whose name is "Documents" and download the monthly progress report.
# Go to the menu whose name is "Media" where you will find a sub menu, whose name is "Photo Gallery".
# Your task is to download 10 photos from the webpage and store them in a folder.
# Kindly create the folder using python only.

from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import requests

# Function to create a folder if it doesn't exist
def create_folder(Photo_folder):
    if not os.path.exists(Photo_folder):
        os.makedirs(Photo_folder)

# Function to download an image
def download_image(url, folder, filename):
    response = requests.get(url, stream=True)
    with open(os.path.join(folder, filename), 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)

# Open the main page
url = "https://labour.gov.in/"
driver = webdriver.Chrome()  # You can use other browser drivers like Firefox, Safari, etc.
driver.get(url)

# Task 1: Download monthly progress report from "Documents" menu
documents_menu = driver.find_element(By.XPATH, "//a[normalize-space()='Documents']")
documents_menu.click()

# Add code here to locate and download the monthly progress report

# Task 2: Download 10 photos from "Media" -> "Photo Gallery"
media_menu = driver.find_element(By.XPATH, "//a[normalize-space()='Media']")
media_menu.click()

photo_gallery_submenu = driver.find_element(By.XPATH, "//a[normalize-space()='Photo Gallery']")
photo_gallery_submenu.click()

# Create a folder to store downloaded photos
photo_folder = "downloaded_photos"
create_folder(photo_folder)

# Download 10 photos
photo_count = 10
for i in range(1, photo_count + 1):
    photo_xpath = f"//div[@id='image-gallery']/div[{i}]/a/img"
    photo_element = driver.find_element(By.XPATH, "photo_xpath")
    photo_src = photo_element.get_attribute("src")

    # Assuming photo URLs end with '.jpg'
    photo_filename = f"photo_{i}.jpg"
    download_image(photo_src, photo_folder, photo_filename)

# Close the browser
driver.quit()
