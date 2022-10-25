#!/bin/python3

#A list of hairstyles offered by the salon
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

#A list of hairstyle prices
prices = [30, 25, 40, 20, 20, 35, 50, 35]

#A list of the number of customers who bought each hairstyle last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Set the total price to zero originally
total_price = 0

#Loop through the prices list and add each price to the total price
for price in prices:
  total_price += price

#Calculate and save the average price, then print it
average_price = total_price/len(prices)
print("Average Haircut Price: " + str(average_price))

#Use a list comprehension to make a list called new_prices which reduces the price of all haircuts by 5 dollars
new_prices = [price - 5 for price in prices]
print(new_prices)

#Create a variable to save the total revenue and set it to zero originally
total_revenue = 0

#Loop over the prices and customer amounts to calculate the total revenue
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

#Print the total revenue
print("Total Revenue: $" + str(total_revenue))

#Calculate and print the average daily revenue
average_daily_revenue = total_revenue/7
print("The Average Daily Revenue Is: $" + str(average_daily_revenue))

#Use a list comprehension to collect hairstyles that cost less than 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

#Print the hair cuts that cost less than 30 dollars
print("Check out our hairstyles under $30!")
for cut in cuts_under_30:
  print(cut)
