from selenium.webdriver.common.by import By

class UserManagement_Class:
    Click_UserManagement_Xpath = (By.XPATH, "//a[normalize-space()='User Management']")
    Text_EditUsername_Xpath = (By.XPATH, "//input[@id='username']")
    Click_Usersearch_Xpath = (By.XPATH, "//button[@type='submit']")
    Text_EditPassword_Xpath = (By.XPATH, "//input[@id='password']")
    Text_EditEmail_Xpath = (By.XPATH, "//input[@id='email']")
    Text_EditPhoneno_Xpath = (By.XPATH, "//input[@id='phone']")
    Click_Savechanges_Xpath = (By.XPATH, "//button[@type='submit']")
    Click_Viewallusers_Xpath =(By.XPATH,"//a[normalize-space()='View All Users']")
    Click_Createuser_Xpath =(By.XPATH,"//a[normalize-space()='Create User']")
    Click_Createusersubmit_Xpath = (By.XPATH,"//button[@type='submit']")
    Click_Edit_Xpath = (By.XPATH,"//tbody/tr[1]/td[4]/a[1]")
    Click_Delete_Xpath = (By.XPATH,"//tbody/tr[1]/td[4]/a[1]")
    Verify_Usermanagement_URL_Xpath = (By.XPATH,"//h2[normalize-space()='User Management']")
    Verify_Usermanagement_search_Xpath = (By.XPATH,"//h2[normalize-space()='Edit User']")
    Verify_Edituser_Xpath = (By.XPATH,"//div[@class='success-message']")
    Verify_Viewallusers_Xpath = (By.XPATH,"//h2[normalize-space()='User List']")


    def __init__(self,driver):
        self.driver = driver

    def Click_Usermanagement_Button(self):
        self.driver.find_element(*UserManagement_Class.Click_UserManagement_Xpath).click()

    def Click_Usersearch_Button(self):
        self.driver.find_element(*UserManagement_Class.Click_Usersearch_Xpath).click()

    def Enter_Username(self, username):
        self.driver.find_element(*UserManagement_Class.Text_EditUsername_Xpath).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*UserManagement_Class.Text_EditPassword_Xpath).send_keys(password)

    def Enter_Email(self, email):
        self.driver.find_element(*UserManagement_Class.Text_EditEmail_Xpath).send_keys(email)

    def Enter_Phoneno(self, phoneno):
        self.driver.find_element(*UserManagement_Class.Text_EditPhoneno_Xpath).send_keys(phoneno)

    def Click_Savechanges_Button(self):
        self.driver.find_element(*UserManagement_Class.Click_Savechanges_Xpath).click()

    def Click_Viewallusers_Button(self):
        self.driver.find_element(*UserManagement_Class.Click_Viewallusers_Xpath).click()

    def Click_Createuser_Button(self):
        self.driver.find_element(*UserManagement_Class.Click_Createuser_Xpath).click()

    def Click_Edit_Button(self):
        self.driver.find_element(*UserManagement_Class.Click_Edit_Xpath).click()

    def Click_Delete_Button(self):
        self.driver.find_element(*UserManagement_Class.Click_Delete_Xpath).click()

    def Click_Createusersubmit_Button(self):
        self.driver.find_element(*UserManagement_Class.Click_Createusersubmit_Xpath).click()

    def Validate_Usermanagement_URL(self):
        if self.driver.find_element(*UserManagement_Class.Verify_Usermanagement_URL_Xpath).text == "User Management":
            return "pass"
        else:
            return "fail"

    def Validate_Usermanagement_search(self):
        if self.driver.find_element(*UserManagement_Class.Verify_Usermanagement_search_Xpath).text == "Edit User":
            return "pass"
        else:
            return "fail"

    def Validate_Edituser(self):
        if self.driver.find_element(*UserManagement_Class.Verify_Edituser_Xpath).text == "User updated successfully":
            return "pass"
        else:
            return "fail"

    def Validate_viewalluser(self):
        if self.driver.find_element(*UserManagement_Class.Verify_Viewallusers_Xpath).text == "User List":
            return "pass"
        else:
            return "fail"

    def Validate_Createuser(self):
        try:
            if self.driver.find_element(*UserManagement_Class.Verify_Edituser_Xpath).text == "User created successfully":
                return "pass"
            else:
                return "fail in Try"
        except:
            return "Failed in Except"








