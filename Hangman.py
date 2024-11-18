import random
l = ["Apple", "Banana", "Grapes"]
rand_word = (random.choice(l)).lower()
guess_string = []
final_guess = ""
for i in range(0,len(rand_word)):
    guess_string += "_"
print(rand_word)
from hangman_art import logo
print(logo)
lives = 6
from hangman_art import stages
print(stages[lives])
c = 0
while(c < 100):
    f = 0
    for i  in guess_string:
        if(i == "_"):
            f += 1
    if(f >= 1 and lives > 0):
        guess_word = input("Guess:")
        for i in range(0,len(rand_word)):
                if(guess_word == rand_word[i]):
                    guess_string[i] = guess_word
        if guess_word not in rand_word:
            print("You guessed wrong!")
            lives -= 1
            print(stages[lives])
        if(lives == 0):
            if "_" in guess_string:
                print("You lost, since you have no lives")
            else:
                print("You win")
        elif(lives > 0 and "_" not in guess_string):
            print("You win")
    else:
        break
    print(final_guess.join(guess_string))
    c += 1
    print(f"You have {lives} turns")

