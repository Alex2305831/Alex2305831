import random

word_list=["DECEPTICONS"]
secret_word=random.choice(word_list)
guessed_letters=[]
attempts=6

print("Geia soy kaloshrthes sthn kremala vres thn parakato leksi:")
print("_"*len(secret_word))

while attempts>0:
    guess=input("Grapse ena gramma gia na vreis thn leksi:").upper()

    if guess in guessed_letters:
        print("Exeis grapsei auto to gramma")
        continue
    guessed_letters.append(guess)
    
    if guess in secret_word:
        print("Sosta auto to gramma uparxei sthn leksi")
    else:
        attempts-=1
        print(f"Lathos den uparxei auto to gramma dokimase ksana apomenoun {attempts} prospatheies akomh")
        
    displayed_word=[letter if letter in guessed_letters else "_"  for letter in secret_word]
    print("".join(displayed_word))
    
    if "_" not in displayed_word:
        print("Mpravo vrhkes thn leksi:",secret_word)
        break
    
if attempts==0:
    print(f"H leksi pou psaxname einai {secret_word}")
print("\n Telos paixnidiou")