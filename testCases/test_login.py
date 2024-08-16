import time

from pageObjects.Login_user import Login_user_Class
import pytest
from utilities.Readconfig import ReadConfig_Class


class Test_login:
    def test_login_url_001(self, setup):
        print("Page Title --> ", setup.title)
        Login = Login_user_Class(setup)
        Login.click_login_button()
        time.sleep(1)
        if setup.title == "Login":
            print("URL Test passed")
            assert True
        else:
            print("URL Test failed")
            assert False

    def test_login_user_002(self, setup_login):
        Login = Login_user_Class(setup_login)
        Login.enter_username(ReadConfig_Class.getUsername())
        Login.enter_passowrd(ReadConfig_Class.getPassword())
        Login.click_login2_button()
        if Login.verify_login() == f"Logged in as: {ReadConfig_Class.getUsername()}":
            print("TC PASSED:", Login.verify_login())
            assert True
        else:
            print("TC FAILED:", Login.verify_login())
            assert False
