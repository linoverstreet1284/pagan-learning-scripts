import random
import time

def run_scrying_engine():
    print("Scrying engine is running...")
    time.sleep(2)  # Simulate some processing time
    result = random.choice(["Success", "Failure", "Inconclusive"])
    print(f"Scrying result: {result}")

    target_number = random.randint(1, 100)
    attempts = 0

    print("Channelling the elements...")
    time.sleep(1.5)
    print("✨ The energy is cast. Begin your scrying. ✨\n")

    while True:
        user_input = input("Enter your guess (1-100): ")

        if user_input.lower() == "exit":
            print(f"The energy dissipates. The hidden number was: {target_number}. Blessed be.")
            break

        if not user_input.isdigit():
            print("❌ The elements do not recognize that input. Please enter a whole number.\n")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < 1 or guess > 100:
            print("❌ The number is outside the circle of 1 to 100. Try again.\n")
        elif guess < target_number:
            print("🔥 Too Low. The current energy burns higher. Try scrying upwards.\n")
        elif guess > target_number:
            print("❄️ Too High. The current energy rests lower. Try scrying downwards.\n")
        else:
            print(f"\n🌟 Success! You have aligned with the matrix. 🌟")
            print(f"The hidden number was indeed {target_number}!")
            print(f"It took you {attempts} meditative attempts to match the vibration.\n")
            break

# Execute the scrying session
if __name__ == "__main__":
    run_scrying_engine()
