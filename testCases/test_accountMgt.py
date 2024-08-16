import time

from pageObjects.AccMgt import AccountMgt_Class
from utilities.Readconfig import ReadConfig_Class
from utilities import Excelutilities
from pageObjects.Login_user import Login_user_Class
import allure

class Test_AccMgt:
    acc_status = []
    Excel_createAcc_Data = "./testCases/Test_Data/Test_Data_createAcc.xlsx"

    def test_createacc_001(self, setup_login):

        username = ReadConfig_Class.getUsername()
        password = ReadConfig_Class.getPassword()
        Login = Login_user_Class(setup_login)
        Login.enter_username(username)
        Login.enter_passowrd(password)
        Login.click_login2_button()
        create = AccountMgt_Class(setup_login)

        time.sleep(2)

        Rcount = Excelutilities.getrowCount(self.Excel_createAcc_Data, "Sheet1")
        for r in range(2, Rcount + 1):
            create.Click_AccMgt_Button()
            setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
            create.Click_CreateAcc_Button()
            setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
            create.Enter_CustID(Excelutilities.readData(self.Excel_createAcc_Data, "Sheet1", r, 2))
            create.Select_Acctype(Excelutilities.readData(self.Excel_createAcc_Data, "Sheet1", r, 3))
            time.sleep(1)
            create.Enter_Balance(Excelutilities.readData(self.Excel_createAcc_Data, "Sheet1", r, 4))
            time.sleep(1)
            create.Click_CreateAccFinal_Button()
            time.sleep(3)

            Expected_result = Excelutilities.readData(self.Excel_createAcc_Data, "Sheet1", r, 5)

            if create.Validate_CreateAcc() == Expected_result:
                setup_login.save_screenshot(f".\\Screenshots\\Createacc_001_pass{r}.png")  # Save a screenshot
                screenshot = setup_login.get_screenshot_as_png()  # for allure screenshot attachment
                allure.attach(screenshot, name=f"Createacc_001_pass{r}.png", attachment_type=allure.attachment_type.PNG) # for allure screenshot attachment
                Excelutilities.writeData(self.Excel_createAcc_Data, "Sheet1", r, 6, create.Validate_CreateAcc())
                Excelutilities.writeData(self.Excel_createAcc_Data, "Sheet1", r, 7, "pass")
                self.acc_status.append("pass")

            else:
                setup_login.save_screenshot(f".\\Screenshots\\Createacc_001_fail{r}.png")  # Save a screenshot
                screenshot = setup_login.get_screenshot_as_png()  # for allure screenshot attachment
                allure.attach(screenshot, name=f"Createacc_001_fail{r}.png", attachment_type=allure.attachment_type.PNG) # for allure screenshot attachment
                Excelutilities.writeData(self.Excel_createAcc_Data, "Sheet1", r, 6, create.Validate_CreateAcc())
                Excelutilities.writeData(self.Excel_createAcc_Data, "Sheet1", r, 7, "fail")
                self.acc_status.append("fail")
        if "fail" not in self.acc_status:
            assert True
        else:
            assert False

    def test_searchacc_002(self,setup_login):
        Search = AccountMgt_Class(setup_login)
        Search.Click_AccMgt_Button()
        setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
        Search.Enter_AccSearch("147")
        Search.Click_AccSearch_Button()
        if Search.Validate_SearchAcc() == "pass":
            assert True
        else:
            assert False


    def test_editacc_003(self,setup_login):
        Edit = AccountMgt_Class(setup_login)
        Edit.Click_AccMgt_Button()
        setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
        Edit.Enter_AccSearch("147")
        Edit.Click_AccSearch_Button()
        if Edit.Validate_SearchAcc() == "pass":
            Edit.Click_Edit_Button()
            setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
            time.sleep(3)
            Edit.Select_Acctype(1)
            time.sleep(3)
            Edit.Enter_Balance("6556")

            Edit.Click_Update_Button()
            if Edit.Validate_EditAcc() == "pass":
                assert True
            else:
                assert False
        else:
            assert False





