from selenium import webdriver
qspiders = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
qspiders.get("https://www.facebook.com/")
qspiders.maximize_window()
qspiders.implicitly_wait(30)
qspiders.find_element_by_id("email").send_keys("admin")
qspiders.find_element_by_id("pass").send_keys("manager")
qspiders.find_elements_by_id("royal_login_button").click()
qspiders.find_element_by_xpath("//select[@name='birthday_day]")















