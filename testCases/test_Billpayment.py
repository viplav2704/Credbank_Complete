import time

import allure

from pageObjects.Login_user import Login_user_Class
from pageObjects.BillPayment import BillPayment_Class
from utilities import Excelutilities
from utilities.Readconfig import ReadConfig_Class


class Test_Billpayment:
    Billpayment_Data = "./testCases/Test_Data/BillPayment.xlsx"

    def test_Billpayment_001(self, setup_login):
        Login = Login_user_Class(setup_login)
        username = ReadConfig_Class.getUsername()
        password = ReadConfig_Class.getPassword()

        Login.click_login2_button()
        Login.enter_username(username)
        Login.enter_passowrd(password)
        Login.click_login2_button()

        Bill = BillPayment_Class(setup_login)
        Bill.Click_BillPayment_Button()
        Rcount = Excelutilities.getrowCount(self.Billpayment_Data, "Sheet1")
        Billpayment_status = []

        for r in range(2, Rcount + 1):
            setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
            time.sleep(2)
            Bill.Enter_AccID(Excelutilities.readData(self.Billpayment_Data, "Sheet1", r, 2))
            Bill.Enter_Payeename(Excelutilities.readData(self.Billpayment_Data, "Sheet1", r, 3))
            Bill.Enter_Amount(Excelutilities.readData(self.Billpayment_Data, "Sheet1", r, 4))
            Bill.Enter_Description(Excelutilities.readData(self.Billpayment_Data, "Sheet1", r, 5))
            Bill.Click_PayBill_Button()

            Expected_result = Excelutilities.readData(self.Billpayment_Data, "Sheet1", r, 6)
            if Bill.Validate_Fundtransfer() == Expected_result:
                setup_login.save_screenshot(f".\\Screenshots\\Bill_payment001_pass{r}.png")  # Save a screenshot
                screenshot = setup_login.get_screenshot_as_png()  # for allure screenshot attachment
                allure.attach(screenshot, name=f"Bill_payment001_pass{r}.png", attachment_type=allure.attachment_type.PNG) # for allure screenshot attachment
                Excelutilities.writeData(self.Billpayment_Data, "Sheet1", r, 7, Bill.Validate_Fundtransfer())
                Excelutilities.writeData(self.Billpayment_Data, "Sheet1", r, 8, "pass")
                Billpayment_status.append("pass")
            else:
                setup_login.save_screenshot(f".\\Screenshots\\Bill_payment001_fail{r}.png")  # Save a screenshot
                screenshot = setup_login.get_screenshot_as_png()  # for allure screenshot attachment
                allure.attach(screenshot, name=f"Bill_payment001_fail{r}.png", attachment_type=allure.attachment_type.PNG) # for allure screenshot attachment
                Excelutilities.writeData(self.Billpayment_Data, "Sheet1", r, 7, Bill.Validate_Fundtransfer())
                Excelutilities.writeData(self.Billpayment_Data, "Sheet1", r, 8, "fail")
                Billpayment_status.append("fail")


        if "fail" not in Billpayment_status:
            assert True
        else:
            assert False