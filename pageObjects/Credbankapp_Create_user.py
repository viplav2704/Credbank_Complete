# test user: User: aaaa, pwd: Test@123, email: aaa@aaa.com, pwd: 987654321
# usr: Viplav ; Pwd: Viplav@1234 ; email: viplavborkar1@gmail.com ; Cust ID: 21; Acc ID: 21
import time

from selenium.webdriver.common.by import By


# Creating Class and objects of all :
class Signup_Class:
    Click_Signup_Xpath = (By.XPATH, "//a[normalize-space()='Sign Up']")
    Text_Username_Xpath = (By.XPATH, "//input[@id='username']")
    Text_Password_Xpath = (By.XPATH, "//input[@id='password']")
    Text_Email_Xpath = (By.XPATH, "//input[@id='email']")
    Text_Phoneno_Xpath = (By.XPATH, "//input[@id='phone']")
    Click_CreateUser_Xpath = (By.XPATH, "//button[@type='submit']")
    Success_Msg_Xpath = (By.XPATH, "//div[@class='success-message']")
    Failed_Msg_Xpath = (By.XPATH,"//div[@class='error-message']")


    def __init__(self, driver):
        self.driver = driver

    def Click_Signup_Button(self):
        self.driver.find_element(*Signup_Class.Click_Signup_Xpath).click()

    def Enter_Username(self, username):
        self.driver.find_element(*Signup_Class.Text_Username_Xpath).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*Signup_Class.Text_Password_Xpath).send_keys(password)

    def Enter_Email(self, email):
        self.driver.find_element(*Signup_Class.Text_Email_Xpath).send_keys(email)

    def Enter_Phoneno(self, phoneno):
        self.driver.find_element(*Signup_Class.Text_Phoneno_Xpath).send_keys(phoneno)

    def Click_CreateUser_Button(self):
        self.driver.find_element(*Signup_Class.Click_CreateUser_Xpath).click()

    def Scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom

    def Validation_Create_user(self):
        try:
            return self.driver.find_element(*Signup_Class.Success_Msg_Xpath).text
        except:
            return self.driver.find_element(*Signup_Class.Failed_Msg_Xpath).text

    def Validation_Createuser_Excel(self):
        try:
            self.driver.find_element(*Signup_Class.Success_Msg_Xpath)
            return "pass"
        except:
            self.driver.find_element(*Signup_Class.Failed_Msg_Xpath)
            return "fail"






            # print("Create User Failed as ", self.driver.find_element(*Signup_Class.Status_Msg_Xpath).text)

# User: Admin, pwd: Admin@123 , ID: 41 , Created Cust: Cust ID: 21, Acc id:21
# Tushar cust id: 4, user id: 21, Acc ID: 1
# Transfer id: 2


# Issues
# 1. when we create a new user and If user already exists, it navigates to "https://bankapp.credence.in/userManagement.html" as user "blank" instead to staying on the same page.
# 2 If we search the user : we see "Logout" Twice.
# 3." Logged in as: " is always visible on every page even if logged out.
# 4. Anyone can create user. Should there be access to Admins only create users?
# 5. All users not visible after clicking on "User Management" >> "View All users"
# 6. "User Management" >> "View All users" Bug when clicked on page 2, and also when clicked on page 1 , it is redirected to : https://bankapp.credence.in/customers?page=1 and 2 respectively instead of users page
# 7. Password is visible using inspect.
# 8. ID not visible when searched for a particular user on UserManagement page
