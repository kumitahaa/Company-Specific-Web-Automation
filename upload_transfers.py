'''This is Specific Company Related use.
    It is to update a daily routine  task
    It is not for needed for many  '''


# ------------- Imports Here --------- 
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

file_path = "6047.txt" # Name the file as the dID
input_name = file_path.split('.')
output_name = input_name[0]
print(output_name)



file = open (file_path, 'r')

dID = output_name

phone_nums = []
for line in file:
    if line.startswith("Inc"):
        words = line.split(" ")
        for element in words:
            if element.startswith("("):
                phone_nums.append(element)

print(len(phone_nums))
print(phone_nums)



#  ------------- URL -------------
driver = webdriver.Chrome()
url = "https://docs.google.com/forms/d/e/1FAIpQLSf6W9UmydKtkZhjKXSp505gELMKpRRVmik9hSngo1iTbNtQOg/viewform"
driver.get(url)
time.sleep(5)

record = 1
for num in phone_nums:
    # ------------- Entering Details -------------
    phone_input = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    phone_input.send_keys(num)
    print(f"----------Number: {num}----------")
    time.sleep(1)
    dID_input = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    dID_input.send_keys(dID)
    print(f"----------DID: {dID}----------")
    time.sleep(1)
    print(f"----------Record# {record}.----------")
    record = record+1
    submit_btn = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")
    submit_btn.click()
    time.sleep(2)
    resubmit_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    resubmit_btn.click()
    time.sleep(2)
    
print("----------All Done!!!----------")