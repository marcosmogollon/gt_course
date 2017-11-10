#Copy your Burrito class from the last exercise. Now,
#write a getter and a setter method for each attribute.
#each setter should accept a value as an argument. If the
#value is a valid value, it should set the corresponding
#attribute to the given value. Otherwise, it should set the
#attribute to False. Edit the constructor to use these new
#setters and getters.
#
#Valid values for each setter are as follows:

# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False

#Make sure you name each setter with the format:
#"set_some_attribute" and "get_some_attribute"
#
#For example, the getter for meat would be get_meat. The
#getter for to_go would be get_to_go.
#
#Hint: Your code is going to end up *very* long. This
#will be the longest program you've written so far, but
#it isn't the most complex. Complexity and length are
#often very different!
#
#Hint 2: Checking for valid values will be much easier
#if you make a list of valid values for each attribute
#and check the new value against that.


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
        #check if the correct type of meat is provided and if not set the instance variable to False
        if not ((meat is "chicken") or (meat is "pork") or (meat is "steak") or (meat is "tofu")):
            self.meat = False
        else:
            # if the correct type of meat is provided the set the instance
            #variable to the provided type and return the instance variable
            self.meat = meat
            return self.meat

    def set_to_go(self, to_go):
        if not((to_go is True) or (to_go is False)):
            self.to_go = False
        else:
            self.to_go = to_go
            return self.to_go

    def set_rice(self, rice):
        if not((rice is "brown") or (rice is "white")):
            self.rice = False
        else:
            self.rice = rice
            return self.rice

    def set_beans(self, beans):
        if not((beans is "black") or (beans is "pinto")):
            self.beans = False
        else:
            self.beans = beans
            return self.beans

    def set_extra_meat(self, extra_meat):
        if not((extra_meat is False) or (extra_meat is True)):
            self.extra_meat = False
        else:
            self.extra_meat = extra_meat
            return self.extra_meat

    def set_guacamole(self, guacamole):
        if not((guacamole is False) or (guacamole is True)):
            self.guacamole = False
        else:
            self.guacamole = guacamole
            return self.guacamole

    def set_cheese(self, cheese):
        if not((cheese is False) or (cheese is True)):
            self.cheese = False
        else:
            self.cheese = cheese
            return self.cheese

    def set_pico(self, pico):
        if not((pico is False) or (pico is True)):
            self.pico = False
        else:
            self.pico = pico
            return self.pico


    def set_corn(self, corn):
        if not((corn is False) or (corn is True)):
            self.corn = False
        else:
            self.corn = corn
            return self.corn


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

#Feel free to add code below to test out the class that
#you've written. It won't be used for grading

newBurrito = Burrito("tofu", True, True, True)
print(newBurrito.rice)
print(newBurrito.guacamole)
