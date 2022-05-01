import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

base_go_link = "https://go/"
part450_sections = []
part450_url = []

with open('short_part450list.csv','r') as f:
    csv_data = csv.reader(f)

    for row in csv_data:
        part450_sections.append(row[0])
        part450_url.append(row[3])

section_count = len(part450_url)
driver = webdriver.Chrome()

for num in range(section_count):
    go_450_url = base_go_link+part450_sections[num]
    print(go_450_url)

    driver.get(go_450_url)
    driver.implicitly_wait(0.5)
    text_box = driver.find_element(By.NAME, "?????")
    button = driver.find_element(By.NAME, "????")

    text_box.send_keys(part450_url[num])
    button.click()

driver.quit()
