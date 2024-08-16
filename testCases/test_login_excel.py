import time

import allure

from pageObjects.Login_user import Login_user_Class
from utilities import Excelutilities


class Test_login_excel:
    Excel_file_Path = "./testCases/Test_Data/Test_Data_Login.xlsx"

    def test_loginexcel_001(self, setup_login):
        Login = Login_user_Class(setup_login)
        Rcount = Excelutilities.getrowCount(self.Excel_file_Path, "Sheet1")
        List_Status = []
        for r in range(2, Rcount + 1):
            username = Excelutilities.readData(self.Excel_file_Path, "Sheet1", r, 1)
            password = Excelutilities.readData(self.Excel_file_Path, "Sheet1", r, 2)
            Expected_Result = Excelutilities.readData(self.Excel_file_Path, "Sheet1", r, 3)
            Login.enter_username(username)
            Login.enter_passowrd(password)
            Login.click_login2_button()
            if Login.verify_login_forexcel() == Expected_Result:
                setup_login.save_screenshot(f".\\Screenshots\\loginexcel_001_pass{r}.png")  # Save a screenshot
                screenshot = setup_login.get_screenshot_as_png()  # for allure screenshot attachment
                allure.attach(screenshot, name=f"loginexcel_001_pass{r}.png", attachment_type=allure.attachment_type.PNG) # for allure screenshot attachment

                Excelutilities.writeData(self.Excel_file_Path, "Sheet1", r, 4, Login.verify_login_forexcel())
                Excelutilities.writeData(self.Excel_file_Path, "Sheet1", r, 5, "pass")
                List_Status.append("pass")

            else:
                setup_login.save_screenshot(f".\\Screenshots\\loginexcel_001_fail{r}.png")  # Save a screenshot
                screenshot = setup_login.get_screenshot_as_png()  # for allure screenshot attachment
                allure.attach(screenshot, name=f"loginexcel_001_fail{r}.png", attachment_type=allure.attachment_type.PNG) # for allure screenshot attachment
                Excelutilities.writeData(self.Excel_file_Path, "Sheet1", r, 4, Login.verify_login_forexcel())
                Excelutilities.writeData(self.Excel_file_Path, "Sheet1", r, 5, "fail")
                List_Status.append("fail")
                time.sleep(2)
            try:
                Login.Click_Logout_Button()
            except:
                pass

        print(List_Status)
        if "fail" not in List_Status:
            assert True
        else:
            assert False
