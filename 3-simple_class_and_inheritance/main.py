# 3. Simple Class and Inheritance

class Person:
  def __init__(self, name, age): # constructor
    self.name = name
    self.age = age

  def greet(self):
    if self.age == 1:
      return "My name is " + self.name + " and I am 1 year old."
    else:
      return "My name is " + self.name + " and I am " + str(self.age) + " years old."

class Student (Person): # inherits Person
  def __init__(self, name, age, student_id): # constructor
    super().__init__(name,age)
    self.student_id = student_id

  def greet(self):
    return super().greet() + " My student id is " + self.student_id + "."

# Test code
new_student = Student("Anne", 27, "323")
print(new_student.greet()) # Prints name, age and student_id