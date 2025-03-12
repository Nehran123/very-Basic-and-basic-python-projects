class car:
    def drive(self, mileage):
        print(mileage*8)

    def display_info(self,make, model, year, mileage):
        print(make, model, year, mileage)


show_car= car()
show_car.display_info(make="Jake", model="kolomba",year=2006,mileage=90)
show_car.drive(mileage=90)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

# Test the class
rectangle = Rectangle(10, 20)
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
rectangle.resize(15, 25)
print(f"New Area: {rectangle.area()}")
"""
class circle:
    def __init__(self,radius,pie):
        self.radius= 7
        self.pie= 3.14

    def caluclate_circle_area(self):
        return self.radius*self.pie**2


    def circumference(self):
        return 2 * 3.14 * self.radius

    def resize(self, new_radius):
        self.radius = new_radius


area= circle(6,7)
print(area.caluclate_circle_area())
circle.resize(10)
print(f"New Area: {circle.area()}")
"""
""""
class movie:
    def display_info(self,title, director, release_year):
        self.title= input("What is the title of movie")
        self.director=input("Who is the director")
        self.release_year=int(input("What is the year"))
        print(self.title, self.director, self.release_year)

    def is_old(self):
        current_year=2025
        return current_year-self.release_year>20


MOVIE=movie()
MOVIE.display_info("Jumanji","hhu",2003)
print(MOVIE.is_old())
"""
class animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
        self.sound=self.name
        print(sound)

    def display_info(self,name, species, age):

        print(self.name,species,age)


Animal=animal("Garfield","meoow")
Animal.display_info("Kaputa","Cat",29)
print(Animal)

class Temperature:
    def __init__(self,celcius):
        self.celcius= celcius


    def convert_temperature(self, celcius):
        celcius= int(input("Enter a weather"))
        Fehreinheit= celcius * 9/5 +32
        Kelvin= celcius + 273.15
        print(f"The fehrenheit is {Fehreinheit}")
        print(f"The Kelvin is {Kelvin}")

TEMPERATURE= Temperature(32)
TEMPERATURE.convert_temperature(32)

#inheritance
class mammal:
    def walk(self):
        print("walk")


class dog(mammal):
    pass # this is used when function are empty inorder to please python and it is important to leave 2 line


class cat(dog):
    pass


Cat=cat()
Cat.walk()


