class User:
    def __init__(self, user_id, user_name):
        # here we have self (which refers to the object, not the User), and all the self's variables, or it's Attributes
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    # here we have our method, which takes our self(object) and does something with it.
    # A method, unlike a function, requires the first parameter to be self, for the object calling it. This means that when this method is called, it knows which object is calling it.
    def follow(self, user):
        # the user we are 'following', it's followercount goes up1
        user.followers += 1
        self.following += 1


user_1 = User("001", "jack")
user_2 = User("002", "angela")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
