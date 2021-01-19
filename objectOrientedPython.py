# methods are functions in a class
# attributes are variables in a class

class Pet:
    number_of_pets = 0 # this is a class attribute, it is not part of init, it is shared amongst the class

    # This is called whenever we create a class, and the arguments passed in are
    # set to the attributes
    def __init__(self, name, age): # what self does is denote which object we are referring to
        self.name = name
        self.age = age
        Pet.add_pet() # this way we can keep track of how many pets we have created
    
    def set_name(self, name): # here is a setter to set the name
        self.name = name

    def birthday(self):
        self.age +=1
    
    def greet(self):
        print(f"Hi, I'm {self.name}")

    # class methods do not act on behalf of one instance, it is meant to be called on the class itself
    # class methods require a decorator
    @classmethod
    def add_pet(cls):
        cls.number_of_pets += 1

class Cat(Pet): # Cat inherits from Pet
    def meow(self):
        print("meow")

class Dog(Pet): # Dog inherits from Pet
    def __init__(self, name, age, breed): # we want to add an initialization attribute for breed
        # super references the class we inherit from, it will call the init method from the parent class
        super().__init__(name, age) # notice you do not need self
        self.breed = breed

    def bark(self):
        print("BARK")

    # notice this overrides the method from the base class
    def greet(self):
        print(f"HI, I'M {self.name}")
    
    def get_breed(self):
        return self.breed

d = Dog("OLIVER", 4, "golden retriever") # this instantiates an object named d of the class of Dog
d.bark() # this calls the bark method from the Dog class
d.birthday()
print(d.age) # this is us accessing an attribute directly, notice Oliver started at 4, but is now 5 from his birthday
d.set_name("LORD OLIVER")
d.greet()
print(d.get_breed)
print(Pet.number_of_pets)
# Pet.number_of_pets = 10 # you can change a class variable directly from anywhere by doing this

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] # notice we can initialize this as empty
        self.is_active = True # notice we can assign a starting value on initialization

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print(f"Student {student.name} was added!")
            return True
        else:
            print(f"Class at max capacity! Student {student.name} was not added!")
            return False
    
    def get_average(self):
        average = 0
        for student in self.students:
            average += student.get_grade()
        
        return average / len(self.students)

s1 = Student("Ian", 29, 95)
s2 = Student("Sunny", 28, 100)
s3 = Student("Oliver", 4, 0)

c1 = Course("Computer Science", 2)
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)
print(c1.students[0].name)
print(c1.get_average())

# static classes
# sometimes you want to collect a bunch of things into a class so it is easy to import
# we can use static classes for this, you do not want to have to create an object to use it
# you just want to access the methods of the class in another file by importing it
# can import by doing:
# from objectOrientedPython import Tricks
class Tricks:
    @staticmethod # these DO NOT CHANGE ANYTHING, they only do something
    def get_first_letter(input): # no need for self of cls
        if type(input) == str:
            return input[0]
        else:
            print("Must pass a string!")
            return False

print(Tricks.get_first_letter("Test"))