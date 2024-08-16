import time

import pytest

from pageObjects.Credbankapp_Create_user import Signup_Class

class Test_Signup:
    def test_main_pageURL_001(self, setup):
        print("Title page --> ", setup.title)
        if setup.title == 'Bank Application':
            assert True
        else:
            assert False

    def test_signup_URL_002(self, setup):
        Sign_Obj = Signup_Class(setup)
        Sign_Obj.Click_Signup_Button()
        print("TITLE URL SIGNUP: ", setup.title)
        time.sleep(1)
        if setup.title == 'Create User':

            assert True
        else:
            assert False
    @pytest.mark.xfail
    def test_Create_user_003(self, setup):

        Create_user = Signup_Class(setup)
        Create_user.Click_Signup_Button()
        Create_user.Enter_Username("Viplav")
        Create_user.Enter_Password("Viplav@1234")
        Create_user.Enter_Email("Viplavborkar1@gmail.com")
        time.sleep(3)
        Create_user.Enter_Phoneno("9022515409")
        setup.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Code for scroll to bottom
        time.sleep(1)

        Create_user.Click_CreateUser_Button()
        time.sleep(2)
        if Create_user.Validation_Create_user() == "User created successfully":
            print(Create_user.Validation_Create_user())
            assert True
        else:
            print("Failed Creating user because: ", Create_user.Validation_Create_user())
            assert False
