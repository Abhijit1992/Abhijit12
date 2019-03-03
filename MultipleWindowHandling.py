from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:/Driver/chromedriver.exe")
driver.get("https://phptravels.com/")
driver.maximize_window()
driver.implicitly_wait(30)
win_id= driver.current_window_handle
print(win_id)
time.sleep(15)
driver.find_element_by_xpath("//span[text()='Login']").click()

mul_win_id=driver.window_handles
#print(mul_win_id)
#print(type(mul_win_id))
#print(mul_win_id[1])
#driver.switch_to.window(mul_win_id[1])
for id in mul_win_id:
    if (win_id !=id):
        driver.switch_to.window(id)
        driver.find_element_by_id("inputEmail").send_keys("testt")
#driver.close()
#driver.quit()