import unittest
from user import user
class TestUser(unittest.TestCase):
    
    """
    Test class that defines test cases for the user class behaviours,
    the arguments help in creating test cases.
    
    """

    def setUp(self)
    """
       this method runs before each test case, carries the instrctions of what is to be done
    """

        self.new_user = User("twitter","Wambita")

    def test_init(self):
        """
        used to test if the objects have been initialized properly
        """

        self.assertEqual(self.new_user.login_account,"twitter")
        self.assertEqual(self.new_user.login_username,"Wambita")

    def test_save_detail(self):

        """
        the test_save_detail test is used to test if the contact object is saved into details
        """

        self.new_user.save_detail()

        self.assertEqual(len(User.user_detail),1)

    def test_save_multiple_detail(self):

        """
        a method to check if we can save multiple user details to our details array
        """

        self.new_user.save_detail()
        test_user = Contact("Test","user")
        test_user.save_detail()
        self.assertEqual(len(User.user_detail),2)



if __name__ == '__main__':
    unittest.main()
