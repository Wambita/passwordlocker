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

        self.new_user = User("Charity","Wambita","Cwambita","cw123", "123cw")

     def tearDown(self):

            """
            tearDown method does clean up after each test case has runself.
            """
    
    def test_init(self):
        """
        used to test if the objects have been initialized properly
        """

         self.assertEqual(self.new_user.first_name,"Charity")
        self.assertEqual(self.new_user.last_name,"Wambita")
        self.assertEqual(self.new_user.phone_number,"Cwambita")
        self.assertEqual(self.new_user.email,"cw123")
        self.assertEqual(self.new_user.email,"123cw")


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
        test_user = user("Test","user","0712345678","test@user.com")
        test_user.save_detail()
        self.assertEqual(len(User.user_detail),3)



  
    def test_display_all_details(self):

        """
        is a method that returns a list of all details saved
        """

        self.assertEqual(User.display_all_details(),User.user_detail)

if __name__ == '__main__':
    unittest.main()
