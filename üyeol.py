from selenium import webdriver
from üyelikbilgileri import name,lastname, eposta ,password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
 

class Üyeol:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.haydigiy.com/")
        self.name=name
        self.lastname=lastname
        self.eposta = eposta
        self.password=password
        
        
    def test_üyeol(self): 
       self.driver.get("https://www.haydigiy.com/")
       login_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[4]/div[2]")))
       login_button.click()
       üyeol_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div[2]/span/a")))
       üyeol_button.click()
       WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"FirstName")))
       nameInput= self.driver.find_element(By.ID,"FirstName")
       WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"LastName")))
       lastnameInput= self.driver.find_element(By.ID,"LastName")
       WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"EmailOrPhone")))
       epostaInput= self.driver.find_element(By.ID,"EmailOrPhone")
       WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"Password")))
       passwordInput= self.driver.find_element(By.ID,"Password")
       sleep(5)
       actions = ActionChains(self.driver)
       actions.send_keys_to_element(nameInput, name)
       actions.send_keys_to_element(lastnameInput,lastname)
       actions.send_keys_to_element(epostaInput,eposta)
       actions.send_keys_to_element(passwordInput, password)
       actions.perform()  #ilgili aksiyonları çalıştır.
       sleep(5)
       uyeol = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"register-button")))
       uyeol.click()
       sleep(2)
       Message = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/form/div[1]")))
       testResult = Message.text == "Üyelik işleminiz başarıyla tamamlanmıştır"
       print(f"TEST SONUCU: {testResult}")
       
testclass=Üyeol()
testclass.test_üyeol()       