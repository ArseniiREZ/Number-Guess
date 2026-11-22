from game import Game
game = Game()
while game.attempts > 0:
    print(f"{game.attempts} Attempts left")

    guess = int(input("Guess the number!"))

    result = game.guess(guess)

    print(result)

    if result == "You guessed the number!":
        print("You won")
        break

else:
    print("You lost")
    print(f"The number was {game.number}")


