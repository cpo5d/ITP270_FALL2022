from datetime import date

class Student:

  def __init__(self, name, year, attendance):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = attendance
  
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
    else:
      pass

  def get_average(self):
    total = 0
    for grade in self.grades:
      total += grade.score
    return total/len(self.grades)

roger = Student("Roger van der Weyden", 10, {date(2022,11,15):True, date(2022,11,16):False, date(2022,11,17):True})
sandro = Student("Sandro Botticelli", 12, {date(2022,11,15):True, date(2022,11,16):True, date(2022,11,17):True})
pieter = Student("Pieter Bruegel the Elder", 8, {date(2022,11,15):False, date(2022,11,16):False, date(2022,11,17):False})

class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(score):
    if score >= self.minimum_passing:
      return True
    else: 
      return False

pieter.add_grade(Grade(100))
pieter.add_grade(Grade(90))
pieter.add_grade(Grade(85))
pieter.add_grade(Grade(97))
print(pieter.get_average())
