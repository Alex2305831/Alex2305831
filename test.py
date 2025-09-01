import json
import platform
class Computer:
    def __init__(self,processor,motherboard,graphics_card):
        self.processor=processor
        self.motherboard=motherboard
        self.graphics_card=graphics_card
        
    def myFunction(self):
        return "Your motherboard is",self.motherboard,"the processor's brand is",self.processor,"and the graphics card brand is",self.graphics_card
text="This is Python my favorite programming language"
if "Python" in text:
    print(text.lower())
else:
    print("This word doesnt appear in the text")
print(len(text))
print(text.replace("p","f"))
print(text[27:38])
print(text.replace("Python","Javascrypt"))
print(text.isdigit())
password="Boss05"
guess=input("Guess the password to continue: ")
while guess!=password:
    guess=input("Its wrong guess again: ")
    if guess==password:
        break
print("Great you guessed it its",password,"lets continue")
my_info={
    "Name":"Alex",
    "Phonenumber":6970625307,
    "Age":20,
    "City":"Thessaloniki"
}
print(len(my_info))
if "City" in my_info:
    print("The city key is exists")
else:
    print("This key doesnt exist")
print("Your name is",my_info["Name"],"and you are",my_info["Age"],"years old")
print(json.dumps(my_info,indent=4,separators=(",","="),sort_keys=True))
p1=Computer("Amd","Aorus","Msi")
print(p1.processor,p1.motherboard,p1.graphics_card)
print(p1.myFunction())
y=platform.system()
print("Your computer system is",y,"11 Pro")