class weight:
    def __init__(self, message):
        self.message=input("Enter ur weight(kg/lbs), if u choose kg it will be calculated in pounds")#display message
        message1= float(message)

    def pounds_to_kilogram(self,kilogram):#initializing solution
        return message1 * 0.4535924


    def kilogram_to_pounds(self,message1):#initializing solution
        return message1 * 2.204623



WEIGHT=weight(56)


if WEIGHT.message=="kg":
    WEIGHT.kilogram_to_pounds(3)
    print(WEIGHT.kilogram_to_pounds(3))

elif WEIGHT.message == "lbs":
    WEIGHT.pounds_to_kilogram(1)
    print(WEIGHT.pounds_to_kilogram(2))
else:
    print("Invlaid input")