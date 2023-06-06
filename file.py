class User:

    Bank_Name = "The Money Place"
    User_List = []

    def __init__(self, first_name, last_name, email, age): 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False #default
        self.gold_card_points = 0 #default

    def display_info(self): #instance methods
        print(f'First Name : {self.first_name}\n Last Name : {self.last_name}\n Email : {self.email}\n Age : {self.age}')
        return self

    def enroll(self): #instance methods
        if self.is_rewards_member: 
            print(f'User already a member.')
            return self
        #change member's "is_rewards_member" status to True
        self.is_rewards_member = True
        #Then set their "gold_card_points" to 200
        self.gold_card_points = 200
        print(f'Is a Rewards Member?  {self.is_rewards_member}\n Number of Gold Card Points : {self.gold_card_points}')
        return self
        #Bonus: if User is a member already, print "User already a member." and return False, otherwise return True.


    def spend_points(self, amount): #instance methods
        if self.gold_card_points < amount:
            print(f'Not enough points on your account.')
        else:
        #have this method decrease the user's points by the amount specified
            self.gold_card_points = self.gold_card_points - (amount)
            print(f'User {self.first_name} {self.last_name} has {self.gold_card_points} left')
        #Bonus: Add logic to spend pointsmethod so if they don't have enough points to spend it stops them (print 'Sorry, there's not enough points on your account')


#Ben the variable is the instance
Ben = User('Ben', 'Gomez', 'benfakemailisfake@fakeemail.com', 31) #added User 

# Ben.display_info() #call instance
# Ben.enroll() #call instance
# Ben.enroll()
# Ben.spend_points(210) #call instance

Ben.display_info().enroll().spend_points(50) 