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
