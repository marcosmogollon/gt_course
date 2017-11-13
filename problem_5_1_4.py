#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5
# - If the burrito's meat is "chicken", "pork" or "tofu",
#   add $1 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1 to the cost
# - If guacamole is True, add $0.75 to the cost


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

    def get_cost(self):
        base_cost = float(5)
        if (self.extra_meat is True) and (not self.meat is False):
            base_cost = base_cost + 1
        if self.guacamole is True:
            base_cost = base_cost + 0.75
        if (self.meat == "chicken") or (self.meat == "pork") or (self.meat == "tofu"):
            base_cost = base_cost + 1
        if self.meat == "steak":
            base_cost = base_cost + 1.5

        return base_cost


newBurrito = Burrito("chicken", True, True, True, True, True)
print(newBurrito.get_cost)
#print(newBurrito.guacamole)

#Feel free to add code below to test out the class that
#you've written. It won't be used for grading.
