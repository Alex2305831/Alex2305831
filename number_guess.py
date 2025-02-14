import random

secret_number=random.randint(1,100)
attempts=0

print("Geia sou kaloshrthes sto 'Mantepse ton arithmo!'")
print("Prospathise na mantepseis enan arithmo metaksi tou 1 mexri to 100")

while True:
    guess=input("Mantepse ton arithmo:")
    
    if not guess.isdigit():
        print("Oxi theloume enan egkuro arithmo")
        continue
    guess=int(guess)
    attempts+=1
    
    if guess<secret_number:
        print("Ligo pio megalos")
    elif guess>secret_number:
        print("Ligo pio mikros")
    else:
        print(f"Mpravo vrhkes ton arithmo {secret_number} sth prospatheia {attempts} suxaritiria")
        break  
print("Efxaristoume pou epaixes")
