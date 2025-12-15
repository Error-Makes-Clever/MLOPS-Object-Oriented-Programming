class chatbook:
    """
    A simple social media application class that simulates user registration,
    login, posting, and messaging functionality.
    """

    # Class variable (private) - shared across all instances to track unique user IDs
    # The double underscore (__) makes it name-mangled for privacy
    __user_id = 1

    def __init__(self):
        """
        Constructor method that initializes a new user instance.
        Logic:
        - Assigns a unique ID to each user by using the class variable __user_id
        - Increments the class variable so the next user gets a different ID
        - Initializes user attributes with default values
        """
        # Assign current class-level user_id to this instance
        self.id = chatbook.__user_id
        
        # Increment class-level user_id for next user (auto-increment pattern)
        chatbook.__user_id += 1

        # Private attribute for user's display name (name-mangled with __)
        self.__name = "Default User"
        
        # Public attributes for authentication
        self.username = ''  # Stores email/username
        self.password = ''  # Stores password (should be hashed in production)
        self.loggedin = False  # Tracks login state
        self.menu()

    @staticmethod
    def get_id():
        """
        Static method to retrieve the current value of the class-level user_id counter.
        Logic: Returns the next ID that will be assigned to a new user
        """
        return chatbook.__user_id

    @staticmethod
    def set_id(val):
        """
        Static method to manually set the class-level user_id counter.
        Logic: Allows resetting or adjusting the ID counter (useful for testing)
        """
        chatbook.__user_id = val

    def get_name(self):
        """
        Getter method for the private __name attribute.
        Logic: Provides controlled access to private attribute
        """
        return self.__name
    
    def set_name(self, value):
        """
        Setter method for the private __name attribute.
        Logic: Allows modification of private attribute with potential validation
        """
        self.__name = value

    def menu(self):
        """
        Main menu display and navigation logic.
        Logic:
        - Displays menu options to user
        - Takes user input and routes to appropriate method
        - Acts as the central navigation hub for the application
        """
        user_input = input(""""Welcome to Chatbook !! How would you like to proceed?
                           
                           1. Press 1 to Sign Up
                           2. Press 2 to Sign In
                           3. Press 3 to Write a Post
                           4. Press 4 to Message a Friend
                           5. Press 5 to Exit
                           \n
                           -> """)
        
        # Route user to appropriate functionality based on input
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            print("Logged out sucessfully")
            exit()  # Any other input exits the application

    def signup(self):
        """
        User registration logic.
        Logic:
        - Collects email and password from user
        - Stores credentials in instance attributes
        - Confirms successful signup
        - Returns to main menu for next action
        """
        email = input("Enter your email here -> ")
        pwd = input("Setup your password here -> ")

        # Store credentials in instance variables
        self.username = email
        self.password = pwd

        print("You have signed up successfully !!")

        print("\n")
        self.menu()  # Recursive call to display menu again

    def signin(self):
        """
        User authentication logic.
        Logic:
        - Checks if user has signed up first (credentials exist)
        - If signed up, prompts for login credentials
        - Validates credentials by comparing with stored values
        - Sets loggedin flag to True on successful authentication
        - Returns to menu regardless of outcome
        """
        # Check if user has registered first
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the main menu")
        else:
            # Prompt for credentials
            uname = input("Enter your email/username here -> ")
            pwd = input("Enter your password here -> ")

            # Validate credentials by exact string match
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully !!")
                self.loggedin = True  # Set authentication flag
            else:
                print("Please input correct credentials..")

        print("\n")
        self.menu()  # Return to menu

    def my_post(self):
        """
        Post creation logic.
        Logic:
        - Checks if user is logged in before allowing post
        - If logged in, accepts post content and displays confirmation
        - If not logged in, prompts user to sign in first
        - Returns to menu after operation
        """
        # Authorization check - must be logged in to post
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something...")

        print("\n")
        self.menu()  # Return to menu

    def sendmsg(self):
        """
        Direct messaging logic.
        Logic:
        - Checks if user is logged in before allowing messaging
        - If logged in, accepts message content and recipient name
        - Displays confirmation of message sent
        - If not logged in, prompts user to sign in first
        - Returns to menu after operation
        """
        # Authorization check - must be logged in to send messages
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the msg? -> ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first to post something...")
            
        print("\n")
        self.menu()  # Return to menu


# User instantiation (currently commented out)
# user1 = chatbook()