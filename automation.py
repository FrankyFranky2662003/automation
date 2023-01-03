from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSe3ZqvDxwplkxeoxxyLxF5yK-vGXPPkTqTWqC3UIpJRNepj-w/viewform')
time.sleep(3)

mn_button = web.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label')
mn_button.click()

car_id = '530'
id = web.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
id.send_keys(car_id)

name= 'Wira Min Thway'
lname =web.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
lname.send_keys(name)

emp_id = '6194'
ie = web.find_element('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
ie.send_keys(emp_id)

sumilf = web.find_element('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
sumilf.click()
