import json

try:
    with open("herbs.json", "r") as file:
        HERB_DATABASE = json.load(file)
except FileNotFoundError:
    print("Error: Could not find herbs.json file!")
    HERB_DATABASE = {}

def search_database():
    print("--- 🌿 Welcome to the Kitchen Witch Database 🌿 ---")
    print("Type 'exit' at any time to close your grimoire.\n")
    
    # This loop keeps the program running until you type 'exit'
    while True:
        user_input = input("Enter an herb name to look up its correspondences: ").lower().strip()
        
        # Check if the user wants to leave
        if user_input == "exit":
            print("Bright blessings on your workings! Goodbye.")
            break
            
        # Check if the herb exists in our dictionary
        if user_input in HERB_DATABASE:
            herb_info = HERB_DATABASE[user_input]
            print(f"\n✨ Correspondences for {user_input.capitalize()}:")
            print(f"  • Element: {herb_info['element']}")
            print(f"  • Planetary Ruler: {herb_info['ruler']}")
            
            # Turn the list of intentions into a clean, comma-separated string
            intentions_str = ", ".join(herb_info["intentions"])
            print(f"  • Magical Uses: {intentions_str}\n")
        else:
            print(f"❌ '{user_input}' is not in your database yet. Try rosemary, lavender, mint, cinnamon, or thyme.\n")

# Run the database search loop
search_database()