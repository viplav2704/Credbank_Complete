import time

import allure
import pytest

from pageObjects.UserManagement import UserManagement_Class
from pageObjects.Login_user import Login_user_Class
from utilities.Readconfig import ReadConfig_Class
from utilities import Excelutilities


class Test_UserManagement:
    def test_UserMgt_url001(self, setup_login):
        Login = Login_user_Class(setup_login)
        username = ReadConfig_Class.getUsername()
        password = ReadConfig_Class.getPassword()
        Login.enter_username(username)
        Login.enter_passowrd(password)
        Login.click_login2_button()
        User = UserManagement_Class(setup_login)
        User.Click_Usermanagement_Button()

        if User.Validate_Usermanagement_URL() == "pass":
            setup_login.save_screenshot(".\\Screenshots\\UserMgt_url_pass.png")  # Save a screenshot
            screenshot = setup_login.get_screenshot_as_png()  # for allure screenshot attachment
            allure.attach(screenshot, name="UserMgt_url_pass.png", attachment_type=allure.attachment_type.PNG)  # for allure screenshot attachment
            assert True
        else:
            setup_login.save_screenshot(".\\Screenshots\\UserMgt_url_fail.png")  # Save a screenshot
            screenshot = setup_login.get_screenshot_as_png()  # for allure screenshot attachment
            allure.attach(screenshot, name="UserMgt_url_fail.png", attachment_type=allure.attachment_type.PNG)  # for allure screenshot attachment
            assert False

    @pytest.mark.skip
    def test_UserManagement_search_002(self, setup_login):
        search = UserManagement_Class(setup_login)
        setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
        time.sleep(1)
        search.Enter_Username("Viplav")
        search.Click_Usersearch_Button()
        time.sleep(1)
        if search.Validate_Usermanagement_search() == "pass":
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_usersearchedit_003(self, setup_login):
        edit = UserManagement_Class(setup_login)
        edit.Enter_Username("Viplav")
        edit.Click_Usersearch_Button()
        # setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
        edit.Enter_Phoneno("1234567890")
        edit.Click_Savechanges_Button()
        time.sleep(3)
        print(edit.Validate_Edituser())
        if edit.Validate_Edituser() == "pass":
            assert True
        else:
            assert False
    @pytest.mark.skip
    def test_viewallusers_004(self, setup_login):
        User = UserManagement_Class(setup_login)
        User.Click_Usermanagement_Button()
        setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
        User.Click_Viewallusers_Button()
        if User.Validate_viewalluser() == "pass":
            assert True
            User.Click_Usermanagement_Button()
        else:
            assert False

    # def test_createuser_005(self, setup_login):
    #     create = UserManagement_Class(setup_login)
    #     time.sleep(2)
    #     setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
    #     create.Click_Createuser_Button()
    #     create.Enter_Username("test1")
    #     create.Enter_Password("Test1@12345")
    #     create.Enter_Email("viplav2@viplav.com")
    #     create.Enter_Phoneno("90225515151")
    #     setup_login.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
    #     time.sleep(1)
    #     create.Click_Createusersubmit_Button()
    #     time.sleep(1)
    #     if create.Validate_Createuser() == "pass":
    #         assert True
    #     else:
    #         print(create.Validate_Createuser())
    #         assert False

    # def test_viewalledit_005(self):
    #     pass
    #
    # def test_viewalldelete_006(self):
    #         pass


