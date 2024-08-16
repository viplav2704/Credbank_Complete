import time

import allure

from pageObjects.Credbankapp_Create_user import Signup_Class
from utilities import Excelutilities
from datetime import datetime

import random
import string


def generate_random_username(length=6):
    return 'viplav' + ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_email(domain="gmail.com"):
    return generate_random_username() + "@" + domain


def generate_random_phone_number():
    return ''.join(random.choices(string.digits, k=10))


class Test_Create_user_excel:
    Excel_file_Path = "./testCases/Test_Data/Test_Data_createuser.xlsx"

    def test_createuser_excel_random_004(self, setup):
        Newuser = Signup_Class(setup)
        Newuser.Click_Signup_Button()
        time.sleep(1)

        Rcount = 2  #set the number of users we need to add
        Expected_result = "pass"
        List_status = []

        for r in range(2,Rcount + 2):
            username = generate_random_username(6)
            Excelutilities.writeData(self.Excel_file_Path,"Sheet1",r,2,username)

            password= "NewPassword@123"
            Excelutilities.writeData(self.Excel_file_Path,"Sheet1",r,3,password)

            email= generate_random_email()
            Excelutilities.writeData(self.Excel_file_Path, "Sheet1", r, 4,email)

            Phoneno = generate_random_phone_number()
            Excelutilities.writeData(self.Excel_file_Path, "Sheet1", r, 5,Phoneno)

            Excelutilities.writeData(self.Excel_file_Path,"Sheet1",r,6,"pass")

            Newuser.Enter_Username(username)
            Newuser.Enter_Password(password)
            Newuser.Enter_Email(email)
            Newuser.Enter_Phoneno(Phoneno)
            setup.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
            time.sleep(1)
            Newuser.Click_CreateUser_Button()

            if Newuser.Validation_Createuser_Excel() == Expected_result:
                setup.save_screenshot(f".\\Screenshots\\CreateUser1_004_pass{r}.png")  # Save a screenshot
                screenshot = setup.get_screenshot_as_png()  # for allure screenshot attachment
                allure.attach(screenshot, name=f"CreateUser1_004_pass{r}.png", attachment_type=allure.attachment_type.PNG) # for allure screenshot attachment
                Excelutilities.writeData(self.Excel_file_Path, "Sheet1", r,7,Newuser.Validation_Createuser_Excel())
                Excelutilities.writeData(self.Excel_file_Path, "Sheet1", r,8, "pass")
                Excelutilities.writeData(self.Excel_file_Path, "Sheet1", r,9, datetime.now())
                List_status.append("pass")
                Newuser.Click_Signup_Button()

            else:
                setup.save_screenshot(f".\\Screenshots\\CreateUser1_004_fail{r}.png")  # Save a screenshot
                screenshot = setup.get_screenshot_as_png()  # for allure screenshot attachment
                allure.attach(screenshot, name=f"CreateUser1_004_fail{r}.png", attachment_type=allure.attachment_type.PNG) # for allure screenshot attachment
                Excelutilities.writeData(self.Excel_file_Path, "Sheet1", r,7, Newuser.Validation_Createuser_Excel())
                Excelutilities.writeData(self.Excel_file_Path, "Sheet1", r,8, "fail")
                Excelutilities.writeData(self.Excel_file_Path, "Sheet1", r,9, datetime.now())

                List_status.append("fail")

        print(List_status)
        if "fail" not in List_status:
            assert True
        else:
            assert False


