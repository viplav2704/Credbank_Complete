from selenium.webdriver.common.by import By


class CustMgt_Class:
    Click_CustMgtUrl_Xpath = (By.XPATH, "//a[normalize-space()='Customer Management']")
    Text_CustID_Xpath = (By.XPATH, "//input[@id='customerId']")
    Click_SearchCustID_Xpath = (By.XPATH, "//button[@type='submit']")
    Verify_ErrorMsg_Xpath = (By.XPATH, "//div[@class='error-message']")
    Click_CreateCust_Xpath = (By.XPATH, "//a[normalize-space()='Create Customer']")
    Text_UserID_Xpath = (By.XPATH, "//input[@id='userId']")
    Text_Fname_Xpath = (By.XPATH, "//input[@id='firstName']")
    Text_Lname_Xpath = (By.XPATH, "//input[@id='lastName']")
    Text_DOB_Xpath = (By.XPATH, "//input[@id='dateOfBirth']")
    Text_Address_Xpath = (By.XPATH, "//input[@id='address']")
    Text_City_Xpath = (By.XPATH, "//input[@id='city']")
    Text_State_Xpath = (By.XPATH, "//input[@id='state']")
    Text_Zipcode_Xpath = (By.XPATH, "//input[@id='zipCode']")
    Click_CreateCustFinal_Xpath = (By.XPATH, "//button[@type='submit']")
    Verify_SuccessMsg_Xpath = (By.XPATH, "//div[@class='success-message']")
    Click_Viewallcust_Xpath = (By.XPATH, "a[href='/customers']")
    Edit_Cust_Xpath = (By.XPATH, "//h2[normalize-space()='Edit Customer']")
    Click_Savechanges_Xpath = (By.XPATH, "//button[normalize-space()='Save Changes']")

    def __init__(self, driver):
        self.driver = driver

    def Click_Custmgt_Button(self):
        self.driver.find_element(*CustMgt_Class.Click_CustMgtUrl_Xpath).click()

    def Enter_CustID(self, custid):
        self.driver.find_element(*CustMgt_Class.Text_CustID_Xpath).send_keys(custid)

    def Click_SearchCustID_Button(self):
        self.driver.find_element(*CustMgt_Class.Click_SearchCustID_Xpath).click()

    def Validate_Search(self):
        try:
            self.driver.find_element(*CustMgt_Class.Edit_Cust_Xpath)
            return "pass"
        except:
            return "fail"

    def Click_CreateCust_Button(self):
        self.driver.find_element(*CustMgt_Class.Click_CreateCust_Xpath).click()

    def Enter_UserID(self, userID):
        self.driver.find_element(*CustMgt_Class.Text_UserID_Xpath).clear()
        self.driver.find_element(*CustMgt_Class.Text_UserID_Xpath).send_keys(userID)

    def Enter_fname(self, fname):
        self.driver.find_element(*CustMgt_Class.Text_Fname_Xpath).clear()
        self.driver.find_element(*CustMgt_Class.Text_Fname_Xpath).send_keys(fname)

    def Enter_lname(self, lname):
        self.driver.find_element(*CustMgt_Class.Text_Lname_Xpath).clear()
        self.driver.find_element(*CustMgt_Class.Text_Lname_Xpath).send_keys(lname)

    def Enter_DOB(self, DOB):
        self.driver.find_element(*CustMgt_Class.Text_DOB_Xpath).clear()
        self.driver.find_element(*CustMgt_Class.Text_DOB_Xpath).send_keys(DOB)

    def Enter_Address(self, addr):
        self.driver.find_element(*CustMgt_Class.Text_Address_Xpath).clear()
        self.driver.find_element(*CustMgt_Class.Text_Address_Xpath).send_keys(addr)

    def Enter_City(self, city):
        self.driver.find_element(*CustMgt_Class.Text_City_Xpath).clear()
        self.driver.find_element(*CustMgt_Class.Text_City_Xpath).send_keys(city)

    def Enter_State(self, state):
        self.driver.find_element(*CustMgt_Class.Text_State_Xpath).clear()
        self.driver.find_element(*CustMgt_Class.Text_State_Xpath).send_keys(state)

    def Enter_Zipcode(self, zipcode):
        self.driver.find_element(*CustMgt_Class.Text_Zipcode_Xpath).clear()
        self.driver.find_element(*CustMgt_Class.Text_Zipcode_Xpath).send_keys(zipcode)

    def Click_CreateFinalCust_Button(self):
        self.driver.find_element(*CustMgt_Class.Click_CreateCustFinal_Xpath).click()

    def Click_Viewallcust_Button(self):
        self.driver.find_element(*CustMgt_Class.Click_Viewallcust_Xpath).click()

    def Validate_CreateCust(self):
        try:
            self.driver.find_element(*CustMgt_Class.Verify_SuccessMsg_Xpath)
            return "pass"
        except:
            return "fail"

    def Click_Savechanges_Button(self):
        self.driver.find_element(*CustMgt_Class.Click_Savechanges_Xpath).click()

    def Validate_Savedchanges(self):
        try:
            self.driver.find_element(*CustMgt_Class.Verify_SuccessMsg_Xpath)
            return "pass"
        except:
            return "fail"
