#!/bin/env python3

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
# A function to convert a fahrenheit temperature to a celsius temperature
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5/9)
  return f_temp

# Calling the function to convert from fahrenheit to celcius
f100_in_celcius = f_to_c(100)

# A function to convert a celcius temperature to a fahrenheit temperature
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

# Calling the function to convery from celius to fahrenheit
c0_in_fahrenheit = c_to_f(0)

# A function to determine force, given mass and acceleration
def get_force(mass, acceleration):
  return mass * acceleration

# Calling the function to calculate force and printing the result
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# A function to calculate energy, given mass and a constant
def get_energy(mass, c=3*10**8):
  return mass*c**2

# Calling the function to calculate energy and printing the result
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# A function to calculate work, given mass, acceleration, and distance
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

# Calling the function to calculate work and printing the result
train_work = get_work(train_mass,train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
