#Write a class called "Burrito". A Burrito should have the
#following attributes (instance variables):
#
# - meat
# - to_go
# - rice
# - beans
# - extra_meat (default: False)
# - guacamole (default: False)
# - cheese (default: False)
# - pico (default: False)
# - corn (default: False)
#
#The constructor should let any of these attributes be
#changed when the object is instantiated. The attributes
#with a default value should be optional.
#
#Hint: Notice that we haven't specified types for the
#non-optional attributes: that's because the types for
#those won't matter!
#
#Hint 2: Think about how we can have default values for
#the last five arguments that can be overridden when the
#object is instantiated.


#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    # setter functions:
    def set_meat(self, meat):
        self.meat = meat

    def set_to_go(self, to_go):
        self.to_go = to_go

    def set_rice(self, rice):
        self.rice = rice

    def set_beans(self, beans):
        self.beans = beans

    def set_extra_meat(self, extra_meat):
        self.extra_meat = False

    def set_guacamole(self, guacamole):
        self.guacamole = False

    def set_cheese(self, cheese):
        self.cheese = False

    def set_pico(self, pico):
        self.pico = False

    def set_corn(self, corn):
        self.corn = False

    # getter functions
    def get_meat(self):
        return self.meat

    def get_to_go(self):
       return self.to_go

    def get_rice(self):
        return self.rice

    def get_beans(self):
        return self.beans

    def get_extra_meat(self):
        return self.extra_meat

    def get_guacamole(self):
        return self.guacamole

    def get_cheese(self):
        return self.cheese

    def get_pico(self):
        return self.pico

    def get_corn(self):
        return self.corn

#The code below will test your class. If it is written
#correctly, this will print True, then False. Note,
#though, that we'll test your code against more complex
#test cases when you submit.
newBurrito = Burrito("Tofu", True, True, True)
print(newBurrito.to_go)
print(newBurrito.guacamole)
