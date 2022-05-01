import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_go_link = "http://go/edit/"
part450_sections = []
part450_url = []

with open('part450list.csv','r') as f:
    csv_data = csv.reader(f)

    for row in csv_data:
        part450_sections.append(row[0])
        part450_url.append(row[3])

section_count = len(part450_url)

try:
    driver = webdriver.Chrome()
    print("Chrome is open")

    for num in range(section_count):
        go_450_url = base_go_link+part450_sections[num]

        driver.get(go_450_url)
        driver.implicitly_wait(0.5)
        text_box = driver.find_element(By.ID,"url")

        print(go_450_url)

        text_box.clear()
        text_box.send_keys(part450_url[num])
        text_box.send_keys(Keys.ENTER)

except Exception as err:
    print(err)
    driver.quit()

driver.quit()

print("And it's done.")
