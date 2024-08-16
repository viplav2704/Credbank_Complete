import time

import allure
import pytest

from pageObjects.CustMgt import CustMgt_Class
from utilities.Readconfig import ReadConfig_Class
from pageObjects.Login_user import Login_user_Class
from utilities import Excelutilities


class Test_CustMgt:
    Excel_custsearch_data = "./testCases/Test_Data/Test_Data_Custidsearch.xlsx"
    Excel_createcust_data = "./testCases/Test_Data/Test_Data_createcust.xlsx"
    search_status = []
    Rcount = Excelutilities.getrowCount(Excel_custsearch_data, "Sheet1")
    create_status = []

    def test_CustMgtsearch_001(self, setup_login):
        username = ReadConfig_Class.getUsername()
        password = ReadConfig_Class.getPassword()
        Login = Login_user_Class(setup_login)
        Login.enter_username(username)
        Login.enter_passowrd(password)
        Login.click_login2_button()

        search = CustMgt_Class(setup_login)
        search.Click_Custmgt_Button()
        for r in range(2, self.Rcount + 1):
            searchID = Excelutilities.readData(self.Excel_custsearch_data, "Sheet1", r, 1)
            Expected_result = Excelutilities.readData(self.Excel_custsearch_data, "Sheet1", r, 2)
            search.Enter_CustID(searchID)
            setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
            time.sleep(0.5)
            search.Click_SearchCustID_Button()
            time.sleep(3)
            if search.Validate_Search() == Expected_result:
                setup_login.save_screenshot(f".\\Screenshots\\CustMgtsearch_001_pass{r}.png")  # Save a screenshot
                screenshot = setup_login.get_screenshot_as_png()  # for allure screenshot attachment
                allure.attach(screenshot, name=f"CustMgtsearch_001_pass{r}.png",
                              attachment_type=allure.attachment_type.PNG)  # for allure screenshot attachment
                actual = Excelutilities.writeData(self.Excel_custsearch_data, "Sheet1", r, 3, search.Validate_Search())
                status = Excelutilities.writeData(self.Excel_custsearch_data, "Sheet1", r, 4, "pass")
                self.search_status.append("pass")
                search.Click_Custmgt_Button()
            else:
                setup_login.save_screenshot(f".\\Screenshots\\CustMgtsearch_001_fail{r}.png")  # Save a screenshot
                screenshot = setup_login.get_screenshot_as_png()  # for allure screenshot attachment
                allure.attach(screenshot, name=f"CustMgtsearch_001_fail{r}.png",
                              attachment_type=allure.attachment_type.PNG)  # for allure screenshot attachment

                actual = Excelutilities.writeData(self.Excel_custsearch_data, "Sheet1", r, 3, search.Validate_Search())
                status = Excelutilities.writeData(self.Excel_custsearch_data, "Sheet1", r, 4, "fail")
                self.search_status.append("fail")

        if "fail" not in self.search_status:
            assert True
        else:
            assert False

    def test_CreateCust_002(self, setup_login):
        create = CustMgt_Class(setup_login)
        Rcount = Excelutilities.getrowCount(self.Excel_createcust_data, "Sheet1")

        for r in range(2, Rcount + 1):
            create.Click_Custmgt_Button()
            setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom

            create.Click_CreateCust_Button()
            userID = Excelutilities.readData(self.Excel_createcust_data, "Sheet1", r, 2)
            fname = Excelutilities.readData(self.Excel_createcust_data, "Sheet1", r, 3)
            lname = Excelutilities.readData(self.Excel_createcust_data, "Sheet1", r, 4)
            dob = Excelutilities.readData(self.Excel_createcust_data, "Sheet1", r, 5)
            addr = Excelutilities.readData(self.Excel_createcust_data, "Sheet1", r, 6)
            city = Excelutilities.readData(self.Excel_createcust_data, "Sheet1", r, 7)
            state = Excelutilities.readData(self.Excel_createcust_data, "Sheet1", r, 8)
            zipcode = Excelutilities.readData(self.Excel_createcust_data, "Sheet1", r, 9)
            time.sleep(10)
            create.Enter_UserID(userID)
            setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
            create.Enter_fname(fname)
            create.Enter_lname(lname)
            create.Enter_DOB(dob)
            create.Enter_Address(addr)
            create.Enter_City(city)
            create.Enter_State(state)
            create.Enter_Zipcode(zipcode)
            create.Click_CreateFinalCust_Button()
            Expected_result = Excelutilities.readData(self.Excel_createcust_data, "Sheet1", r, 11)

            if create.Validate_CreateCust() == Expected_result:
                setup_login.save_screenshot(f".\\Screenshots\\Createcust_002_pass{r}.png")  # Save a screenshot
                Excelutilities.writeData(self.Excel_createcust_data, "Sheet1", r, 12, create.Validate_CreateCust())
                Excelutilities.writeData(self.Excel_createcust_data, "Sheet1", r, 13, "pass")
                self.create_status.append("pass")
            else:
                setup_login.save_screenshot(f".\\Screenshots\\Createcust_002_fail{r}.png")  # Save a screenshot
                Excelutilities.writeData(self.Excel_createcust_data, "Sheet1", r, 12, create.Validate_CreateCust())
                Excelutilities.writeData(self.Excel_createcust_data, "Sheet1", r, 13, "fail")
                self.search_status.append("fail")

        if "fail" not in self.search_status:
            assert True
        else:
            assert False
    def test_editacc_003(self, setup_login):
        Edit = CustMgt_Class(setup_login)
        Edit.Click_Custmgt_Button()
        setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
        Edit.Enter_CustID("21")
        Edit.Click_SearchCustID_Button()
        if Edit.Validate_Search() == "pass":
            setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
            Edit.Enter_City("Changecity")
            Edit.Click_Savechanges_Button()
            time.sleep(2)
            if Edit.Validate_Savedchanges() == "pass":
                assert True
            else:
                assert False
        else:
            assert False
