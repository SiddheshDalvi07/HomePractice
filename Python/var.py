class Car:
    wheels = 4 #class variable
    def __init__(self):
        self.mil = 10
        self.name = "BMW"
    def show(self):
        print(self.mil,self.name)


#instance variables are defined in the constructor
#instance variables are accessed using self keyword / object name
        

#class variables are defined outside the constructor
#class variables are accessed using class name/ object name
#class variables are same for all object


c1 = Car()
c2 = Car()
c1.show()
print(Car.wheels)
print(c1.wheels)


#methods are of 3 types  - instance methods , static methods and class methods
#1. instance methods - takes self as first argument, it belongs to class
#we can access class method takes self as argument, it belong to object

#2. class methods - takes cls as first argument, it belongs to class
#we can access classmethods we use class.methodname

#3.static method does not take any argument 


class Student:
    school = "Oreo" #class variable
    def __init__(self,marks1,marks2,marks3,marks4):
        #instance variables
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.marks4 = marks4

        #instance method
    def avg(self):
        return (self.marks1+self.marks2+self.marks3+self.marks4)/4
    @classmethod
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is a student")
s1 = Student(10,20,30,40)
s2 = Student(50,60,70,80)

print(s1.avg())
print(s2.avg())

#to access classmethods we use class.methodname
print(Student.getSchool())

#to access staticmethods we use class.methodname
Student.info()



class Animal:
    home = "ZOO" #class variable
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod
    def animal_home (cls,home):
        cls.home = home



a1 = Animal("lion", 5)
print(Animal.home)
Animal.animal_home("Jungle")
print(Animal.home)


#destructor 

class Stud:
    def __init__(self):
        print("constructor called")

    def __del__(self):
        print("destructor called")

a = Stud()
del a

#in python destructor called as soon as object is no longer in use by the program, without calling it explicitily

class Age:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @staticmethod
    def checkAge(age):
        if age >= 18:
            print("Adult")
        else:
            print("Child")

a4 = Age("sid",23)
Age.checkAge(a4.age)

#to pass parameter in static method to access instance variable we use objectname.instancevariable

class Student:

  institute="Itvedant"#static variable(class level variable)

  def set_info(self,name,age,marks):#method,to refer current object

       self.name=name

       self.age=age

       self.Marks=marks

  def get_info(self):

        print("name",self.name)

        print("age",self.age)

        print("marks",self.Marks)

        print("Institute",Student.institute)



  @classmethod

  def set_name(cls):

        cls.institute ="Itvedant education "





#before calling class method      

s1=Student()

s1.set_info("Meera",20,95)

s1.get_info()

s2=Student()

s2.set_info("mayank",21,70)

s2.get_info()

#after calling class method  

Student.set_name()#calling class method

s2.get_info()

s1.get_info()









class Student:

  def __init__(self,name,age,marks):#method,to refer current object

       self.name=name

       self.age=age

       self.Marks=marks

       print(self.name, self.age, self.Marks)

  def __del__(self):

      print("destructed called,class got deleted")   
  
stud = Student("Sid",24,95)
del stud
