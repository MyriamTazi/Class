## Classes
Classes are a sort of templates that create objects with related data and functions that can be used to manipulate that data.

define your class using the format: "class User:"

create a user : <user1 = user()> user1 is an instance or an object of the class. 
Attach data to your object: <user1.first_name = "John"> Data attached to the object is a Field (first_name)

Access data same way its been assigned: <print(user1.first_name)>
CLASSES are used to make objects , and each object can have different value for the same variable names, example: <user2.first_name = "Tommy"> This is stored into user2 though it contains the same variable first_name.

Different users can be created and different fields can be created for each user, which can be of any type, example: <user1.age = 20> <user2.hobby = "Axe-Throwing"> <user3.is_sitting = True>

Init methods are to initialise our class. functions inside classes are called methods.
__init__ is a constructor that is a method called whenever there is a first instance in the class. it starts with the argument (self) which is a reference to the new object that is being created, additional arguments can be added. example: 
<class User:
      def __init__(self, name, age, hobby, is_sitting):> 

Then we store the values to fields in the object, like so 
<class User:
      def __init__(self, name, age, hobby, is_sitting):
         self.name = name 
         self.age  = "34"
         self.hobby= "Axe-Throwing"
         is_sitting= True >

GOOD PRACTISE: To add help text, type a docstring than use <help(User)>

SUMMARY : classes group together data <fields>, and related functions <methods> into a sort of machine to create many objects <instances>
