import time

from selenium.webdriver.common.by import By


class Login_user_Class:
    Click_login_Xpath = (By.XPATH, "//a[normalize-space()='Login']")
    Text_Username_Xpath = (By.XPATH, "//input[@id='username']")
    Text_Password_Xpath = (By.XPATH, "//input[@id='password']")
    Click_login2_Xpath = (By.XPATH, "//button[@type='submit']")
    Passed_verify_Xpath = (By.XPATH, "//div[@class='username']")
    Failed_verify_Xpath = (By.XPATH, "//div[@class='error-message']")
    Click_Logout_Xpath = (By.XPATH,"//a[normalize-space()='Logout']")
    Verify_Login_Xpath = (By.XPATH,"//h2[normalize-space()='Dashboard']")

    def __init__(self, driver):
        self.driver = driver

    def click_login_button(self):
        self.driver.find_element(*Login_user_Class.Click_login_Xpath).click()

    def enter_username(self, username):
        self.driver.find_element(*Login_user_Class.Text_Username_Xpath).send_keys(username)

    def enter_passowrd(self, password):
        self.driver.find_element(*Login_user_Class.Text_Password_Xpath).send_keys(password)

    def click_login2_button(self):
        self.driver.find_element(*Login_user_Class.Click_login2_Xpath).click()

    def verify_login(self):
        time.sleep(1)
        try:
            self.driver.find_element(*Login_user_Class.Failed_verify_Xpath)
            return self.driver.find_element(*Login_user_Class.Failed_verify_Xpath).text
        except:
            return self.driver.find_element(*Login_user_Class.Passed_verify_Xpath).text

    def Click_Logout_Button(self):
        self.driver.find_element(*Login_user_Class.Click_Logout_Xpath).click()

    def verify_login_forexcel(self):
        try:
            self.driver.find_element(*Login_user_Class.Click_Logout_Xpath)   #Verifying and clicking logout
            # How to use Logout button in this method directly rather than using "xpath and click"?
            return "pass"
        except:
            return "fail"



