# a simple high low number guessing game.
#
import random

class too_high_too_low:
    def __init__(self):
        # setup self.number to be a random number from 1 to 100
        self.number = random.randint(1, 100)
        # self.guesses to be zero
        self.guesses = 0
        pass

    def play(self):
        while True:
            guess_list = []
            guess_counter = 0
            while True:
                pass
                # Get a number guess from the user (between 1 and 100)
                if self.guesses == 0:
                    print("\033[2J\033[H\nWelcome to the High Low Game! I have selected a number between 1 and 100. Can you guess it?")
                elif self.guesses > 0 and self.guesses < 10:
                    print(f"Previous guesses: {guess_list}")
                guess = int(input("Guess a number between 1 and 100: "))
                # Convert the input to an integer
                # Increment the number of guesses by 1
                if guess < 1 or guess > 100:
                    print("\nPlease enter a number between 1 and 100. And try again.")
                    continue
                if guess in guess_list:
                    print("\nYou already guessed that number. But I'm being nice and not counting that as a guess")
                    print(f"You still have {10 - self.guesses} guesses left.")
                    guess_counter += 1
                    if guess_counter == 3:
                        print("\033[2J\033[H\nI guess you just don't want to win. Fine we are ending things here. Goodday and goodbye.")
                        exit()
                    continue
                guess_list.append(guess)
                self.guesses += 1
                # Check *if* the guess equals the secret number
                if guess == self.number:
                    print(f"\nCongratulations! You guessed the number {self.number} in {self.guesses} guesses.")
                    break
                # Check *if* the guess is less than the secret number
                if guess < self.number:
                    print(f"\nToo low! You have {10 - self.guesses} guesses left.")
                else:
                    print(f"\nToo high! You have {10 - self.guesses} guesses left.")
                if self.guesses == 3:
                    print("Are you only guessing randomly? Maybe ask ChatGPT for help.")
                if self.guesses == 6:
                    print("Half way through your guesses. May need to ask ChatGPT for help.")
                if self.guesses == 9:
                    print("So cloes or not, did you ask ChatGPT for help yet?")
                # Check *if* the player has made 10 guesses
                if self.guesses >= 10:
                    print(f"\nSorry, you've run out of guesses. The number was {self.number}.")
                    break
            status = input("\nDo you want to play again? (y/n): ")
            if status.lower() == 'y':
                self.__init__()
                continue
            else:                
                print("\nThanks for playing! Goodbye.")
                break
            # Check *if* the guess is less than the secret number
            # If so, print "Too low!"
            # Otherwise (the guess must be too high)
            # Print "Too high!"
            # Check *if* the player has made 10 guesses
            # If so, print a message saying they've run out of guesses and reveal the number
            # Exit the loop


def main():
    game = too_high_too_low()
    game.play()


if __name__ == "__main__":
    main()
