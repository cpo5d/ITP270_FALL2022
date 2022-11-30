#!/usr/bin/env python3

#School class 
class School():
  #School constructor
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  #Name getter
  def get_name(self):
    return self.name

  #Level getter
  def get_level(self):
    return self.level

  #number of students getter
  def get_numberOfStudents(self):
    return self.numberOfStudents

  #number of studentss setter
  def set_numberOfStudents(self, num):
    if isinstance(num, int):
      self.numberOfStudents = num
    else:
      raise TypeError

  #School string representation
  def __repr__(self):
   return "A {} school named {} with {} students.".format(self.level, self.name, str(self.numberOfStudents))


#Primary School class
class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  #Pickup policy getter
  def get_pickupPolicy(self):
    return self.pickupPolicy

  #Primary School string representation
  def __repr__(self):    
    return super().__repr__() + " The pickup policy is {}.".format(self.pickupPolicy)


#High School class
class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams

  #Sports teams getter
  def get_sportsTeams(self):
    return self.sportsTeams

  #High School string representation
  def __repr__(self):
    sportsTeams = ""
    for team in self.sportsTeams:
      sportsTeams += team
      sportsTeams += ", "
    return super().__repr__() + " The sports teams are: " + sportsTeams

#####################################
###############TESTS#################
#####################################

#Create a School and print its components
s1 = School("Longfellow", "middle", 800)
print(s1)
print(s1.get_name())
print(s1.get_level())
s1.set_numberOfStudents(801)
print(s1.get_numberOfStudents())

#Create a Primary School and print its components
s2 = PrimarySchool("Louise Archer", 500, "Pickup in the side parking lot")
print(s2)
print(s2.get_name())
print(s2.get_level())
s2.set_numberOfStudents(501)
print(s2.get_numberOfStudents())
print(s2.get_pickupPolicy())

#Create a High School and print its components
s3 = HighSchool("Langley", 1200, ["football", "soccer", "basketball", "field hockey", "baseball"])
print(s3)
print(s3.get_name())
print(s3.get_level())
s3.set_numberOfStudents(1201)
print(s3.get_numberOfStudents())
print(s3.get_sportsTeams())
