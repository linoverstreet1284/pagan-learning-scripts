import json

# Load data dynamically from your external JSON file
try:
    with open("herbs.json", "r") as file:
        HERB_DATABASE = json.load(file)
except FileNotFoundError:
    print("Error: Could not find herbs.json file!")
    HERB_DATABASE = {}

def search_database():
    print("--- 🌿 Welcome to the Kitchen Witch Database (JSON Edition) 🌿 ---")
    print("Options: Type an herb name, type 'search' to find by intention, or type 'exit'.\n")
    
    while True:
        user_input = input("Enter an herb name or command: ").lower().strip()
        
        if user_input == "exit":
            print("Bright blessings on your workings! Goodbye.")
            break
            
        elif user_input == "search":
            intention_query = input("What magical intention are you looking for? (e.g., peace, protection): ").lower().strip()
            found_herbs = []
            
            # Loop through the database to find matching intentions
            for herb_name, herb_info in HERB_DATABASE.items():
                if intention_query in herb_info["intentions"]:
                    found_herbs.append(herb_name.capitalize())
            
            if found_herbs:
                print(f"\n🔮 Herbs matching the intention '{intention_query}':")
                print(f"  -> {', '.join(found_herbs)}\n")
            else:
                print(f"❌ No herbs found for '{intention_query}' in this grimoire yet.\n")
                
        elif user_input in HERB_DATABASE:
            herb_info = HERB_DATABASE[user_input]
            print(f"\n✨ Correspondences for {user_input.capitalize()}:")
            print(f"  • Element: {herb_info['element']}")
            print(f"  • Planetary Ruler: {herb_info['ruler']}")
            
            intentions_str = ", ".join(herb_info["intentions"])
            print(f"  • Magical Uses: {intentions_str}\n")
        else:
            print(f"❌ '{user_input}' not recognized. Type 'search' or try an herb name.\n")

search_database()
