#Copy both your code and ours from the previous exercise.
#You should copy your Burrito class and our Meat, Rice, and
#Beans classes into this exercise.
#
#In this exercise, you won't edit any of your code from the
#Burrito class. Instead, you're just going to write a
#function to use instances of the Burrito class.
#
#Write a function called total_cost. total_cost should take
#as input a list of instances of Burrito, and return the
#total cost of all those burritos together as a float.
#
#Hint: Don't reinvent the wheel. Use the work that you've
#already done. The function can be written in only five
#lines, including the function declaration.
#
#Hint 2: The exercise here is to write a function, not a
#method. That means this function should *not* be part of
#the Burrito class.


#Paste your previous code here.
class Meat:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False

class Beans:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False

#Write your code here!
#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.meat = Meat(meat)
        self.set_to_go(to_go)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    # setter functions:
    def set_meat(self, meat):
        self.meat = Meat(meat)
        # this is the same as the constructor because you initiall want to set
        # the value but you might want to change it again later, this is
        # why the code is repeated here (and in the other setter functions
        # that are using the above classes)

    def set_to_go(self, to_go):
        if not((to_go is True) or (to_go is False)):
            self.to_go = False
        else:
            self.to_go = to_go
            return self.to_go

    def set_rice(self, rice):
        self.rice = Rice(rice)

    def set_beans(self, beans):
        self.beans = Beans(beans)

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
        return self.meat.get_value()

    def get_to_go(self):
       return self.to_go

    def get_rice(self):
        return self.rice.get_value()

    def get_beans(self):
        return self.beans.get_value()

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
        if (self.extra_meat is True) and (not self.meat.get_value() is False):
            base_cost = base_cost + 1
        if self.guacamole is True:
            base_cost = base_cost + 0.75
        if (self.meat.get_value() == "chicken") or (self.meat.get_value() == "pork") or (self.meat.get_value() == "tofu"):
            base_cost = base_cost + 1
        if self.meat.get_value() == "steak":
            base_cost = base_cost + 1.5

        return base_cost

#Write your new function here.

def total_cost(item_list):
    item_total = 0
    for item in item_list:
        item_total = item_total + item.get_cost()
    return item_total

#You can add code below to test your function. We'd suggest
#creating a couple instances of Burrito, adding them to a
#list, then passing that list to total_cost and printing the
#result.

new_burrito1 = Burrito("chicken", True, "brown", "pinto")
new_burrito2 = Burrito("steak", True, "brown", "pinto")
new_burrito3 = Burrito("pork", True, "brown", "pinto")
new_burrito4 = Burrito("tofu", True, "brown", "pinto")

item_list = [new_burrito1, new_burrito2, new_burrito3, new_burrito4]

print(total_cost(item_list))
