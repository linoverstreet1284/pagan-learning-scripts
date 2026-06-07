import random
import time

def load_affirmations():
    """Reads intentions from the external text file."""
    try:
        with open("affirmations.txt", "r") as file:
            # .readlines() takes each line of the text file and puts it into a Python list
            lines = file.readlines()
            # .strip() removes the invisible 'newline' character from each intention
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print("❌ Error: affirmations.txt not found. Please create it first!")
        return []

def run_altar_generator():
    intentions = load_affirmations()
    
    if not intentions:
        return

    print("--- ✨ Digital Altar & Affirmation Generator ✨ ---")
    print("Prepare your space. Your daily intention is being summoned...\n")
    
    # Visual delay for a meditative feel
    time.sleep(2)
    
    # Pick a random intention from the file
    daily_focus = random.choice(intentions)
    
    print("*************************************************")
    print(f"🌟 TODAY'S FOCUS: {daily_focus}")
    print("*************************************************")
    print("\nHold this thought in your mind as you go about your day.")

if __name__ == "__main__":
    run_altar_generator()
