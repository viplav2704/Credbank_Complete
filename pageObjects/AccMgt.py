from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class AccountMgt_Class:
    Click_AccMgt_Xpath = (By.XPATH, "//a[normalize-space()='Account Management']")
    Click_CreateAcc_Xpath = (By.XPATH, "//a[normalize-space()='Create Account']")
    Text_CustID_Xpath = (By.XPATH, "//input[@id='customerId']")
    Select_Acctype_Xpath = (By.XPATH, "//select[@id='accountTypeId']")
    Text_Balance_Xpath = (By.XPATH, "//input[@id='balance']")
    Click_CreateAccfinal_Xpath = (By.XPATH, "//button[@type='submit']")
    Verify_CreateAccsuccessmsg_Xpath =(By.XPATH,"//div[@class='success-message']")
    Verify_failedmsg_Xpath = (By.XPATH,"//div[@class='error-message']")

    def __init__(self, driver):
        self.driver = driver

    def Click_AccMgt_Button(self):
        self.driver.find_element(*AccountMgt_Class.Click_AccMgt_Xpath).click()

    def Click_CreateAcc_Button(self):
        self.driver.find_element(*AccountMgt_Class.Click_CreateAcc_Xpath).click()

    def Enter_CustID(self, custid):
        self.driver.find_element(*AccountMgt_Class.Text_CustID_Xpath).send_keys(custid)

    def Select_Acctype(self, i):
        Select(self.driver.find_element(*AccountMgt_Class.Select_Acctype_Xpath)).select_by_index(i)

    def Enter_Balance(self, balance):
        self.driver.find_element(*AccountMgt_Class.Text_Balance_Xpath).send_keys(balance)

    def Click_CreateAccFinal_Button(self):
        self.driver.find_element(*AccountMgt_Class.Click_CreateAccfinal_Xpath).click()

    def Validate_CreateAcc(self):
        try:
            self.driver.find_element(*AccountMgt_Class.Verify_CreateAccsuccessmsg_Xpath)
            return "pass"
        except:
            self.driver.find_element(*AccountMgt_Class.Verify_failedmsg_Xpath)
            return "fail"


