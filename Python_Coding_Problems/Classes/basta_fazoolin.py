import datetime

################
# The Menu Class
################

class Menu:

  #Constructor, which takes the name, menu items, start time and end time of the menu
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

#String representation of the Menu
  def __repr__(self):
    return "The menu {name} is available from {start_time} to {end_time}.".format(name=self.name, start_time=self.start_time, end_time=self.end_time)

#Method which calculates the total bill given menu items from a menu
  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total

####################
#The Franchise class
####################

class Franchise:

  #Constructor which takes the address and available menus of the Franchise
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

#String representation
  def __repr__(self):
    return("The address of the restaurant is {address}".format(self.address))

  #Method which returns the menus available at a Franchise given a time
  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available.append(menu.name)
    return available

###################
#The Business Class
###################

class Business:

  #Constructor which takes a business name and a list of franchises
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#########################################################################

#Defining a Brunch menu
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.0, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, datetime.time(11,0,0), datetime.time(16,0,0))

#Defining an Early Bird menu
early_bird = Menu("Early Bird", {'salumeria plate': 8.00, 'salad and breadsticks( serves 2, no refils)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, datetime.time(15,0,0), datetime.time(18,0,0))

#Defining a Dinner menu
dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad':16.00, 'pizza with quattro formaggi':11.00, 'duck ragu':19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso':3.00}, datetime.time(17,0,0), datetime.time(23,0,0))

#Defining a Kids menu
kids = Menu("Kid's Menu", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms':12.00, 'apple juice': 3.00}, datetime.time(11,0,0), datetime.time(21,0,0))

#print the Brunch menu
print(brunch)

#Calculate the totals for two bills
print(brunch.calculate_bill(["pancakes","home fries","coffee"]))
print(early_bird.calculate_bill(["salumeria plate","mushroom ravioli (vegan)"]))

#Defining a Flagship Store
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
#Defining a New Installment store
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

#Printing the menus available at different times
print(flagship_store.available_menus(datetime.time(12,0,0)))
print(flagship_store.available_menus(datetime.time(17,0,0)))

#Defining a Business called Basta Fazoolin' with my Heart
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

#Defining an arepas menu
arepas_menu = Menu("Arepas Menu", {'arepa pabellon':7.00, 'pernil arepa': 8.50, 'guayanes arepa':8.00, 'jamon arepa':7.50}, datetime.time(10,0,0), datetime.time(20,0,0))

#Defining an Arepas Franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

#Defining an Arepas Business
arepa_business = Business("Take a' Arepa", [arepas_place])
