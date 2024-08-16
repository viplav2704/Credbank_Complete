from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AccountMgt_Class:
    Click_AccMgt_Xpath = (By.XPATH, "//a[normalize-space()='Account Management']")
    Click_CreateAcc_Xpath = (By.XPATH, "//a[normalize-space()='Create Account']")
    Text_CustID_Xpath = (By.XPATH, "//input[@id='customerId']")
    Select_Acctype_Xpath = (By.XPATH, "//select[@id='accountTypeId']")
    Text_Balance_Xpath = (By.XPATH, "//input[@id='balance']")
    Click_CreateAccfinal_Xpath = (By.XPATH, "//button[@type='submit']")
    Verify_Successmsg_Xpath = (By.XPATH, "//div[@class='success-message']")
    Verify_failedmsg_Xpath = (By.XPATH, "//div[@class='error-message']")
    Enter_AccSearch_Xpath = (By.XPATH, "//input[@id='accountId']")
    Click_AccSearch_Xpath = (By.XPATH, "//button[@type='submit']")
    Verify_Accsearch_Xpath = (By.XPATH, "//h2[normalize-space()='Search Account Results']")
    Click_DeleteAcc_Xpath = (By.XPATH, "//button[@type='submit']")
    Click_EditAcc_Xpath = (By.XPATH, "//a[@class='btn']")
    Click_Update_Xpath = (By.XPATH,"//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def Click_AccMgt_Button(self):
        self.driver.find_element(*AccountMgt_Class.Click_AccMgt_Xpath).click()

    def Click_CreateAcc_Button(self):
        self.driver.find_element(*AccountMgt_Class.Click_CreateAcc_Xpath).click()

    def Enter_CustID(self, custid):
        self.driver.find_element(*AccountMgt_Class.Text_CustID_Xpath).clear()
        self.driver.find_element(*AccountMgt_Class.Text_CustID_Xpath).send_keys(custid)

    def Select_Acctype(self, i):
        Select(self.driver.find_element(*AccountMgt_Class.Select_Acctype_Xpath)).select_by_index(i)

    def Enter_Balance(self, balance):
        self.driver.find_element(*AccountMgt_Class.Text_Balance_Xpath).clear()
        self.driver.find_element(*AccountMgt_Class.Text_Balance_Xpath).send_keys(balance)

    def Click_CreateAccFinal_Button(self):
        self.driver.find_element(*AccountMgt_Class.Click_CreateAccfinal_Xpath).click()

    def Validate_CreateAcc(self):
        try:
            self.driver.find_element(*AccountMgt_Class.Verify_Successmsg_Xpath)
            return "pass"
        except:
            self.driver.find_element(*AccountMgt_Class.Verify_failedmsg_Xpath)
            return "fail"

    def Enter_AccSearch(self, accid):
        self.driver.find_element(*AccountMgt_Class.Enter_AccSearch_Xpath).send_keys(accid)

    def Click_AccSearch_Button(self):
        self.driver.find_element(*AccountMgt_Class.Click_AccSearch_Xpath).click()

    def Validate_SearchAcc(self):
        try:
            self.driver.find_element(*AccountMgt_Class.Click_EditAcc_Xpath)
            return "pass"
        except:
            return "fail"

    def Click_Edit_Button(self):
        self.driver.find_element(*AccountMgt_Class.Click_EditAcc_Xpath).click()

    def Validate_EditAcc(self):
        try:
            self.driver.find_element(*AccountMgt_Class.Verify_Successmsg_Xpath)
            return "pass"
        except:
            return "fail"

    def Click_Update_Button(self):
        self.driver.find_element(*AccountMgt_Class.Click_Update_Xpath).click()
