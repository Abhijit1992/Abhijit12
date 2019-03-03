from selenium import webdriver
qspiders = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
#qspiders = webdriver.Firefox(executable_path="C:\Driver\geckodriver.exe")
qspiders.get("https://www.google.com")