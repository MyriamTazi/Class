#classes templates for creating objects with data and utilise it 
"""class keyword followed by name of class """
class User:
    pass 
user1 = User()                  #User1 is an "instance" of User, can also be called an "object"
user1.first_name = "Madeline"   # Data attached to an object is called field
user1.lastname = "O'reiley"     # Lowercase with words separated by _ as a custom
#these can be printed when called
#can attach additional fields to objects which can be any type 
user2 = User() 
user2.age = 15
print(user2.age)

#init method short for initialisation > constructor 
#function inside class is called a method


# # """
# # self is a reference to the new objcet that is being created 
# # after self, additional args can be added """


class Dolls:                              # The init sets the tone
    def __init__(self, intro, H, ag, Har):  # Attributes must match 
        self.name = intro                     # The self. ...
        self.Height = H
        self.age = ag
        self.Hair = Har

    def intoduction(self):        # Def what will print for each Attribute
        print("I am a doll and my name is " , self.name, "\n")

    def Har(self):
        print("I am a doll and my hair is " , self.Hair, "\n")

    def H(self):
        print("I am a doll and I am" , self.Height , "cm tall", "\n")

    def Ag(self):
        print("I am a doll and I am " , self.age , "years of age", "\n")

# Set variables for diff class members to call later
D1 = Dolls("Darcy", 1.7, 35, "Brown") 
D2 = Dolls("Tim", 2.0, 22, "Blonde")
D3 = Dolls("Barnie", 1.5, 55, "Blondepink")
D5 = Dolls("Carmen", 1.8, 32, "Green")

# Call var . Attribute () to execute the function 
D1.intoduction()
D1.Har()
D1.H()

D2.intoduction()
D2.Har()

D3.intoduction()
D3.Har()

#More examples
class Owners:
    def __init__(self, Owner_Name, Owner_Age, Owner_Hobby, Owner_Hair_colour):
        self.Owner_Name = Owner_Name
        self.Owner_Age = Owner_Age
        self.Owner_Hobby = Owner_Hobby
        self.Owner_Hair_colour = Owner_Hair_colour

    def O_Name(self):
        print("I am an owner and my name is " , self.Owner_Name, "\n")

    def O_Age(self):
        print("I am an owner and I am ", self.Owner_Age, "\n")

    def O_Hobby(self):
        print("I am an owner and my hobbies include ", self.Owner_Hobby, "\n")

    def O_Hair_colour(self):
        print("My hair colour is ", self.Owner_Hair_colour, "\n")

O1 = Owners("Tommy", 65, "Gradening", "Grey")
O2 = Owners("Lacy", 23, "Biking", "Brown")
O3 = Owners("Chad", 45, "Axe Throwing", "Blonde")

O1.O_Name(), O1.O_Hair_colour()
O2.O_Age()
O3.O_Hobby()


class Robots:
    def __init__(self, Cali, N, Model, Colour, Typ, Height):
        self.Caliber = Cali
        self.Name = N
        self.Model = Model
        self.colour = Colour
        self.Type = Typ
        self.Height = Height

    def N(self):
        print("Hi", self.Name)

    def Cali(self):
        print( self.Caliber)

R1 = Robots("High", "Washi", 202312, "Black", "Hybrid", 2.5)
R1.N()
R1.Cali()



class Humans: 
    def __init__(self, Race, Country, Hair_colour, Body_Type):
        self.Race = Race
        self.Country = Country
        self.Hair_colour = Hair_colour
        self.Body_Type = Body_Type
        
    def Race(self):
        print("I am a ", self.Race, " person")
        
    def Country(self):
        print("I am from ", self.Country)

    def Hair_colour(self):
        print("My hair colour is ", self.Hair_colour)

    def Body_Type(self):
        print()


class Students:
    def __init__(self, name, last_name, bday, results, sex):
        self.name = name
        self.last_name = last_name
        self.bday = bday
        self.results = results
        self.sex = sex
    def Name(self):
        print("I am a student and my name is: ")
    
    def Last_name(self):
        print("My last name is: ", self.last_name)
        
    def Bday(self):
        print("I was born on: ", self.bday)
        
    def Results(self):
        print("I got ", self.results, " in my test")
    
    def Sex(self): 
        print(" I am ", self.sex)    
        
S1 = Students("John", "McGregor", 1980/2/1, 78, "Male" )
S2 = Students("Tammy", "Nulty", 1950/1/1, 45, "Female" )
S3 = Students("Darcy", "Sheffy", 1990/7/5, 89, "Female" )

S1.Sex()
