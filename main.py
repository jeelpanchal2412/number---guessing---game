import random
import time
from datetime import datetime

def show_menu():
    print("\n🎮 Number Guessing Game 🎮")
    print("1. Start Game")
    print("2. View Scores")
    print("3. Exit")

def start_game():
    print("\n📊 Choose difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    level = input("👉 Enter choice (1/2/3): ")

    if level == "1":
        number = random.randint(1, 50)
        max_attempts = 10
    elif level == "2":
        number = random.randint(1, 100)
        max_attempts = 7
    elif level == "3":
        number = random.randint(1, 200)
        max_attempts = 5
    else:
        print("❌ Invalid choice! Starting Medium by default.")
        number = random.randint(1, 100)
        max_attempts = 7

    attempts = 0
    start_time = time.time()

    print("\n🔢 Guess the number!")

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts} 👉 Your guess: ")

        if not guess.isdigit():
            print("❌ Enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("📉 Too low!")
        elif guess > number:
            print("📈 Too high!")
        else:
            end_time = time.time()
            time_taken = int(end_time - start_time)
            print(f"\n🎉 Correct! You guessed it in {attempts} tries.")
            print(f"⏱️ Time taken: {time_taken} seconds")
            name = input("📝 Enter your name: ")
            save_score(name, attempts, time_taken)
            break
    else:
        print(f"\n😢 Game Over! The number was {number}")

def view_scores():
    print("\n🏆 Scoreboard:")
    try:
        with open("scores.txt", "r") as file:
            scores = file.readlines()
            if scores:
                for line in scores:
                    print(line.strip())
            else:
                print("No scores yet!")
    except FileNotFoundError:
        print("Score file not found!")

def save_score(name, attempts, time_taken):
    now = datetime.now()
    with open("scores.txt", "a") as file:
        file.write(f"{name} - {attempts} attempts - {time_taken} sec - {now.strftime('%d-%m-%Y %H:%M:%S')}\n")

# 🔁 Main Game Loop
while True:
    show_menu()
    choice = input("👉 Enter your choice (1-3): ")

    if choice == "1":
        start_game()
    elif choice == "2":
        view_scores()
    elif choice == "3":
        print("👋 Thanks for playing!")
        break
    else:
        print("❌ Invalid choice! Try again.")
