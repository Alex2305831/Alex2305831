import random
from words import words_list

def get_word():
    word=random.choice(words_list)
    return word.upper()

def play(word):
    word_length="_" * len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=6
    print("Lets play Hangman!")
    print(word_length)
    while not guessed and tries>0:
        guess=input("Please guess a letter or word:").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter",guess)
                print(word_length)
            elif guess not in word:
                print(guess,"is not in the word")
                tries-=1
                print(word_length)
                guessed_letters.append(guess) 
            else:
                print("Good job",guess,"is in the word")
                guessed_letters.append(guess)
                word_as_list=list(word_length)
                indices=[i for i,letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_as_list[index]=guess
                word_length="".join(word_as_list)
                if not "_" in word_length:
                    guessed=True
                print(word_length)
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guess the word",guess)
            elif guess!=word:
                print(guess,"is not the word")
                tries-=1
                guessed_words.append(guess)
            else:
                guessed=True
                word_length=word
        else:
            print("Not a valid guess")
            break
    if guessed:
        print("Congrats, you guessed the word you win!")
    else:
        print("Sorry you out of tries the word was",word,"maybe next time")
        
def main():
    word=get_word()
    play(word)
    while input("Play Again? (Y/N)").upper()=="Y":
        word=get_word()
        play(word)
        
main()             