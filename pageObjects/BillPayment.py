from selenium.webdriver.common.by import By


class BillPayment_Class:
    Click_BillPayment_Xpath = (By.XPATH, "//a[normalize-space()='Bill Payments']")
    Text_AccountID_Xpath = (By.XPATH, "//input[@id='accountId']")
    Text_PayeeName_Xpath = (By.XPATH, "//input[@id='payeeName']")
    Text_Amount_Xpath = (By.XPATH, "//input[@id='amount']")
    Text_Description_Xpath = (By.XPATH, "//input[@id='description']")
    Click_PAYBILL_Xpath = (By.XPATH, "//button[@type='submit']")
    Verify_Fundtrans_Xpath = (By.XPATH, "//div[@class='success-message']")

    def __init__(self, driver):
        self.driver = driver

    def Click_BillPayment_Button(self):
        self.driver.find_element(*BillPayment_Class.Click_BillPayment_Xpath).click()

    def Enter_AccID(self, accid):
        self.driver.find_element(*BillPayment_Class.Text_AccountID_Xpath).send_keys(accid)

    def Enter_Payeename(self, payee):
        self.driver.find_element(*BillPayment_Class.Text_PayeeName_Xpath).send_keys(payee)

    def Enter_Amount(self, amount):
        self.driver.find_element(*BillPayment_Class.Text_Amount_Xpath).send_keys(amount)

    def Enter_Description(self, amount):
        self.driver.find_element(*BillPayment_Class.Text_Description_Xpath).send_keys(amount)

    def Click_PayBill_Button(self):
        self.driver.find_element(*BillPayment_Class.Click_PAYBILL_Xpath).click()

    def Validate_Fundtransfer(self):
        try:
            self.driver.find_element(*BillPayment_Class.Verify_Fundtrans_Xpath)
            return "pass"
        except:
            return "fail"
