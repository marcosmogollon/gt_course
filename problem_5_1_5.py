#Copy your Burrito class from the last exercise. Below,
#We've given you three additional classes named "Meat",
#"Rice" and "Beans." We've gone ahead and built getters
#and setters in these classes to check if the incoming
#values are valid, so you'll be able to remove those
#from your original code.
#
#First, edit the constructor of your Burrito class.
#Instead of calling setters to set the values of the
#attributes self.meat, self.rice, and self.beans, it
#should instead create new instances of Meat, Rice, and
#Beans. The arguments to these new instances should be
#the same as the arguments you were sending to the
#setters previously (e.g. self.rice = Rice("brown")
#instead of set_rice("brown")).
#
#Second, modify your getters and setters from your
#original code so that they still return the same value
#as before. get_rice(), for example, should still
#return "brown" for brown rice, False for no rice, etc.
#instead of returning the instance of Rice.
#
#Third, make sure that your get_cost function still
#works when you're done changing your code.
#
#Hint: When you're done, creating a new instance of
#Burrito with Burrito("pork", True, "brown", "pinto")
#should still work to create a new Burrito. The only
#thing changing is the internal reasoning of the
#Burrito class.
#
#Hint 2: Notice that the classes Meat, Beans, and Rice
#already contain the code to validate whether input is
#valid. So, your setters in the Burrito class no
#longer need to worry about that -- they can just pass
#their input to the set_value() methods for those
#classes.
#
#Hint 3: This exercise requires very little actual
#coding: you'll only write nine lines of new code, and
#those nine lines all replace existing lines of code
#in the constructor, getters, and setters of Burrito.
#
#You should not need to modify the code below.

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

new_buritto = Burrito("chicken", True, "brown", "pinto", guacamole=True)

#print(new_buritto.meat.get_value())
#print(new_buritto.rice.get_value())
print(new_buritto.get_cost())
