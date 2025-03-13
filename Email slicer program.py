Message_asking_email=input("Enter ur email address= ")
Indexxing= Message_asking_email.find("@")#finds the index of @
Username=Message_asking_email[Indexxing:]#Stops after reaching @ as defined by index variable but start with the 0 index
Domain=Message_asking_email[:Indexxing]#starts after @ and finish the whole input after the @ if +! is used it starts after the @ symbol
print(f"Ur username is {Username} and {Domain}")


