import random
answer = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
def make_choice():
    global my_Choice
    while True:  # Sonsuz döngü, doğru seçim yapılana kadar devam edecek
        my_Choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if my_Choice == 'easy':
            print("Your atttemps are 10.")
            return 10  # Easy mode gives 10 attempts
        elif my_Choice == 'hard':
            print("Your atttemps are 5.")
            return 5  # Hard mode gives 5 attempts
        else:
            print("Your choice is meaningless. Please try again.")
attempts = make_choice()
def guess():
    global attempts
    while attempts > 0:
        num = int(input("Guess a number: "))
        
        if num < 1 or num > 100:  # This checks the range of the user's guess, not the answer
            print("Your guess is out of range. Please try a number between 1 and 100.")
            continue  # Skip the rest of the loop if out of range

        if num < answer:
            print("Too low! Try again.")
        elif num > answer:
            print("Too high! Try again.")
        else:
            print(f"Correct!! The answer is {answer}")
            return  # Exit the game if guessed correctly

        attempts -= 1
        
        if attempts > 0:
            print(f"You have {attempts} attempts left.")
        else:
            print(f"You're out of attempts! The correct answer was {answer}.")
            return  # Exit when out of attempts

guess()
