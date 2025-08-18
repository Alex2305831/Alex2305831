def myFunction(x,y,z):
    return x*y+z
def myFunction2(x,y,z):
    return x+y-z

star="*"

print("If you are wrong in the results the star will be increase with a clone")
x=19*8+3
y=3445+23293-980
counter=1
guess=int(input("Find the result 19*8+3: "))
guess2=int(input("Find the result 3445+23293-980: "))
while guess!=x or guess2!=y:
    star=star*2
    guess=int(input("Guess again the first one: "))
    guess2=int(input("Guess again the second one: "))
    counter*=2
print(f"We finish the task with {counter} stars: {star}")



print(f"The first one is {myFunction(x=19,y=8,z=3)}")
print(f"And the second one is {myFunction2(3445,23293,980)}")