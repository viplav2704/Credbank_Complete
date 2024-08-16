
import time

import allure

from pageObjects.Login_user import Login_user_Class
from pageObjects.FundTransfer import Fundtransfer_Class
from utilities import Excelutilities
from utilities.Readconfig import ReadConfig_Class


class Test_FundTransfer:
    FundTrans_Data = "./testCases/Test_Data/FundTransfer.xlsx"

    def test_fundtransfer_001(self, setup_login):
        Login = Login_user_Class(setup_login)
        username = ReadConfig_Class.getUsername()
        password = ReadConfig_Class.getPassword()
        Login.enter_username(username)
        Login.enter_passowrd(password)
        Login.click_login2_button()
        Rcount = Excelutilities.getrowCount(self.FundTrans_Data, "Sheet1")
        transfer_status = []

        Ftrans = Fundtransfer_Class(setup_login)
        Ftrans.Click_Fundtransfer_Button()

        setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
        Ftrans.Click_CreateTrasnfer_Button()
        for r in range(2, Rcount + 1):
            setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
            Ftrans.Enter_FromAccID(Excelutilities.readData(self.FundTrans_Data, "Sheet1", r, 2))
            Ftrans.Enter_ToAccID((Excelutilities.readData(self.FundTrans_Data, "Sheet1", r, 3)))
            Ftrans.Enter_Amount((Excelutilities.readData(self.FundTrans_Data, "Sheet1", r, 4)))
            Ftrans.Enter_Description((Excelutilities.readData(self.FundTrans_Data, "Sheet1", r, 5)))
            Ftrans.Click_FundTransferfinal_Button()
            time.sleep(3)
            Expected_result = Excelutilities.readData(self.FundTrans_Data, "Sheet1", r, 6)
            if Ftrans.Validate_TransferFund() == Expected_result:
                setup_login.save_screenshot(f".\\Screenshots\\fundtransfer_001_pass{r}.png")  # Save a screenshot
                screenshot = setup_login.get_screenshot_as_png()  # for allure screenshot attachment
                allure.attach(screenshot, name=f"fundtransfer_001_pass{r}.png", attachment_type=allure.attachment_type.PNG) # for allure screenshot attachment

                Excelutilities.writeData(self.FundTrans_Data, "Sheet1", r, 7, Ftrans.Validate_TransferFund())
                Excelutilities.writeData(self.FundTrans_Data, "Sheet1", r, 8, "pass")
                transfer_status.append("pass")
            else:
                setup_login.save_screenshot(f".\\Screenshots\\fundtransfer_001_fail{r}.png")  # Save a screenshot
                screenshot = setup_login.get_screenshot_as_png()  # for allure screenshot attachment
                allure.attach(screenshot, name=f"fundtransfer_001_fail{r}.png", attachment_type=allure.attachment_type.PNG) # for allure screenshot attachment

                Excelutilities.writeData(self.FundTrans_Data, "Sheet1", r, 7, Ftrans.Validate_TransferFund())
                Excelutilities.writeData(self.FundTrans_Data, "Sheet1", r, 8, "fail")
                transfer_status.append("fail")

        if "fail" not in transfer_status:
            assert True
        else:
            assert False


