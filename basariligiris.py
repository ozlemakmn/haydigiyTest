from selenium import webdriver
from userinfo import username,password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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
       üyeol_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[4]/div[2]")))
       üyeol_button.click()
       WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"EmailOrPhone")))
       usernameInput= self.driver.find_element(By.ID,"EmailOrPhone")
       WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"Password")))
       passwordInput= self.driver.find_element(By.ID,"Password")
       actions = ActionChains(self.driver)
       actions.send_keys_to_element(usernameInput,username )
       actions.send_keys_to_element(passwordInput, password)
       actions.perform()  #ilgili aksiyonları çalıştır.
   
       singIn = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/main/div/div[1]/form/div[3]/button")))
       singIn.click()
       Logo_button=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/a/img")))
       Logo_button.click()
       WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.NAME,"q")))
       searchInput=self.driver.find_element(By.NAME,"q")
       searchInput.send_keys("çanta", Keys.ENTER)
    
       firstclass=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[2]/div[1]")))
       firstclass.click()
    
       basket=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"add-to-cart-button-99242")))
       basket.click()
       message= WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[14]/div/div")))
       testResult= message.text == "Ürün Alışveriş Sepetinize Eklendi"
       print(f"TEST SONUCU: {testResult}")
       tocartadd=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div/div[4]/div[4]"))) 
       tocartadd.click()                                        
                                                 
       
       
       
       sleep(5)
    
      
       
       
       
       
       
        
testclass=Login()
testclass.test_login()        
