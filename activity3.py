import random

secret_number=random.randint(1,20)
print("Kaloshrthes sto mantepse ton arithmo")
attempts=0
while True:
    guess=int(input("Mantepse ton arithmo apo to 1 eos to 20: "))
    attempts+=1
    if guess>secret_number:
        print("Ligo mikroteros")
    elif guess<secret_number:
        print("ligo megaluteros")
    else:
        print(f"Mpravo vrhkes ton arithmo {secret_number} stis {attempts} prospatheies")
        break
    if attempts==5:
        print("Dustuxos teleiosan oi prospatheies sou to noumero htan",secret_number)
        break
print("\nTelos paixnidiou")