from selenium.webdriver.common.by import By

class Fundtransfer_Class:
    Click_fundtransfer_Xpath = (By.XPATH,"//a[normalize-space()='Funds Transfer Management']")
    Click_CreateTrans_Xpath = (By.XPATH,"//a[normalize-space()='Create Transfer']")
    Text_FromAccID_Xpath = (By.XPATH,"//input[@id='fromAccountId']")
    Text_ToAccID_Xpath = (By.XPATH,"//input[@id='toAccountId']")
    Text_Amount_Xpath = (By.XPATH,"//input[@id='amount']")
    Text_Description_Xpath = (By.XPATH,"//input[@id='description']")
    Click_fundtransferfinal_Xpath = (By.XPATH,"//button[@type='submit']")
    Verify_transfersuccessmsg_Xpath = (By.XPATH,"//div[@class='success-message']")

    def __init__(self,driver):
        self.driver = driver

    def Click_Fundtransfer_Button(self):
        self.driver.find_element(*Fundtransfer_Class.Click_fundtransfer_Xpath).click()

    def Click_CreateTrasnfer_Button(self):
        self.driver.find_element(*Fundtransfer_Class.Click_CreateTrans_Xpath).click()

    def Enter_FromAccID(self,fromid):
        self.driver.find_element(*Fundtransfer_Class.Text_FromAccID_Xpath).send_keys(fromid)

    def Enter_ToAccID(self,toid):
        self.driver.find_element(*Fundtransfer_Class.Text_ToAccID_Xpath).send_keys(toid)

    def Enter_Amount(self,amount):
        self.driver.find_element(*Fundtransfer_Class.Text_Amount_Xpath).send_keys(amount)

    def Enter_Description(self,desc):
        self.driver.find_element(*Fundtransfer_Class.Text_Description_Xpath).send_keys(desc)

    def Click_FundTransferfinal_Button(self):
        self.driver.find_element(*Fundtransfer_Class.Click_fundtransferfinal_Xpath).click()

    def Validate_TransferFund(self):
        try:
            self.driver.find_element(*Fundtransfer_Class.Verify_transfersuccessmsg_Xpath)
            return "pass"
        except:
            return "fail"







