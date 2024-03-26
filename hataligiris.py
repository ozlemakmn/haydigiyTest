from selenium import webdriver
from loginUserInfo import username,password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
 

class Login:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.haydigiy.com/")
        self.username=username
        self.password=password
        
        
    def test_login(self): 
       self.driver.get("https://www.haydigiy.com/")
       login_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[4]/div[2]")))
       login_button.click()
       WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"EmailOrPhone")))
       usernameInput= self.driver.find_element(By.ID,"EmailOrPhone")
       WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"Password")))
       passwordInput= self.driver.find_element(By.ID,"Password")
       actions = ActionChains(self.driver)
       actions.send_keys_to_element(usernameInput, username)
       actions.send_keys_to_element(passwordInput, password)
       actions.perform()  #ilgili aksiyonları çalıştır.
       sleep(5)
       singIn = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/main/div/div[1]/form/div[3]/button")))
       singIn.click()
       errorMessage= WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[1]/form/div[1]")))
       testResult = errorMessage.text == "Bilgiler Doğrulanamadı, Tekrar Deneyin."
       print(f"TEST SONUCU: {testResult}")
        
       
        
testclass=Login()
testclass.test_login()      
    
       
       