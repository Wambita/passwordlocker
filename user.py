class User:
    """

    Class that will generate new instances of users

    """
    user_detail = []

    def save_detail(self):

        """
        the method saves detail objects into the empty user_detail array
        """
        User.user_detail.append(self)
        
    def delete_detail():

        """
        the delete_detail method is used to remove objects from the user detail array
        """

        User.user_detail.remove(self)

    def __init__(self,first_name,last_name,username,password,confirm_password):

        """
        the __init__method helps us define properties for our objectsself.

        """    

    
    
    def __init__(self,account_name,username,password,confirm_password):

        """
        the __init__method helps us define properties for our objectsself.

        """

        self.account_name = account_name
        self.username = username
        self.password =password
        self.confirm_password = confirm_password


        """
        arguments for our __init__method will include the following.

        """

        @classmethod
    def display_all_details(cls):

        return cls.user_detail