#Create lists for the available toppings and their prices
toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2,6,1,3,2,7,2]

#Count and print the number of 2 dollar slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#Count the number of pizza varieties and print it
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#Create a two dimensional list of the pizzas and their prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

#Sort the pizzas from lowest cost to highest
pizza_and_prices.sort()

#Save the cheapest and most expensive pizzas
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

#Remove the most expensive pizza from the list
pizza_and_prices.pop()

#Add a new pizza in the correct order by price
pizza_and_prices.insert(4, [2.5, "peppers"])

#Make  a list of the three cheapest pizzas and print it
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)