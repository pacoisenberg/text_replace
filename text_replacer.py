import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_go_link = "http://go/edit/"
cfr_part_sections = []
cfr_part_url = []

with open('part420list.csv','r') as f:
    csv_data = csv.reader(f)

    for row in csv_data:
        cfr_part_sections.append(row[0])
        cfr_part_url.append(row[2])

section_count = len(cfr_part_url)

try:
    driver = webdriver.Chrome()
    print("Chrome is open")

    for num in range(section_count):
        go_cfr_part_url = base_go_link+cfr_part_sections[num]

        driver.get(go_cfr_part_url)
        driver.implicitly_wait(0.5)
        text_box = driver.find_element(By.ID,"url")

        print(cfr_part_url[num])

        text_box.clear()
        text_box.send_keys(cfr_part_url[num])
        text_box.send_keys(Keys.ENTER)

except Exception as err:
    print(err)
    driver.quit()

driver.quit()

print("And it's done.")
