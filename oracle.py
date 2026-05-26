import random

# All 78 Tarot Cards with their meanings
TAROT_DECK = {
    # Major Arcana
    "The Fool": "New beginnings, optimism, trust in life, spontaneity.",
    "The Magician": "Action, power, manifesting your desires, resourcefulness.",
    "The High Priestess": "Intuition, sacred knowledge, divine feminine, subconscious.",
    "The Empress": "Fertility, nature, abundance, creativity, nurturing.",
    "The Emperor": "Authority, structure, solid foundations, protection.",
    "The Hierophant": "Spiritual wisdom, tradition, institutions, mentoring.",
    "The Lovers": "Relationships, choices, alignment of values, harmony.",
    "The Chariot": "Direction, control, willpower, victory, determination.",
    "Strength": "Courage, inner strength, patience, compassion.",
    "The Hermit": "Soul-searching, introspection, inner guidance, solitude.",
    "Wheel of Fortune": "Change, cycles, destiny, good luck, turning points.",
    "Justice": "Fairness, truth, law, cause and effect, accountability.",
    "The Hanged Man": "Pause, surrender, letting go, new perspectives.",
    "Death": "Endings, transformation, transitions, letting go of the old.",
    "Temperance": "Balance, moderation, patience, purpose, harmony.",
    "The Devil": "Shadow self, attachment, addiction, restriction, illusion.",
    "The Tower": "Sudden change, upheaval, chaos, revelation, awakening.",
    "The Star": "Hope, faith, purpose, renewal, spirituality.",
    "The Moon": "Illusion, fear, anxiety, subconscious, intuition.",
    "The Sun": "Positivity, fun, warmth, success, vitality.",
    "Judgement": "Reflection, reckoning, awakening, inner calling.",
    "The World": "Completion, integration, accomplishment, travel.",

    # Suit of Wands
    "Ace of Wands": "Inspiration, new opportunities, growth, potential.",
    "Two of Wands": "Future planning, progress, decisions, discovery.",
    "Three of Wands": "Expansion, foresight, overseas opportunities.",
    "Four of Wands": "Celebration, joy, harmony, relaxation, homecoming.",
    "Five of Wands": "Conflict, disagreements, competition, tension.",
    "Six of Wands": "Success, public recognition, victory, progress.",
    "Seven of Wands": "Challenge, competition, perseverance, defense.",
    "Eight of Wands": "Speed, rapid movement, quick action, alignment.",
    "Nine of Wands": "Resilience, grit, persistence, boundaries.",
    "Ten of Wands": "Burden, extra responsibility, hard work, stress.",
    "Page of Wands": "Inspiration, ideas, discovery, limitless potential.",
    "Knight of Wands": "Energy, passion, inspired action, adventure.",
    "Queen of Wands": "Courage, confidence, independence, social butterfly.",
    "King of Wands": "Natural leader, vision, entrepreneur, honor.",

    # Suit of Cups
    "Ace of Cups": "Love, new relationships, creativity, compassion.",
    "Two of Cups": "Unified love, partnership, mutual attraction.",
    "Three of Cups": "Celebration, friendship, creativity, community.",
    "Four of Cups": "Apathy, contemplation, disconnectedness.",
    "Five of Cups": "Regret, failure, disappointment, pessimism.",
    "Six of Cups": "Revisiting the past, childhood memories, innocence.",
    "Seven of Cups": "Searching for purpose, choices, illusions, fantasy.",
    "Eight of Cups": "Disappointment, walking away, leaving behind.",
    "Nine of Cups": "Contentment, satisfaction, gratitude, wish come true.",
    "Ten of Cups": "Divine love, blissful relationships, harmony, alignment.",
    "Page of Cups": "Creative opportunity, intuitive messages, curiosity.",
    "Knight of Cups": "Creativity, romance, charm, imagination.",
    "Queen of Cups": "Compassionate, caring, emotionally stable, intuitive.",
    "King of Cups": "Emotional balance, control, generosity.",

    # Suit of Swords
    "Ace of Swords": "Breakthroughs, new ideas, mental clarity, success.",
    "Two of Swords": "Difficult choices, indecision, stalemate, truce.",
    "Three of Swords": "Heartbreak, emotional pain, sorrow, grief.",
    "Four of Swords": "Rest, relaxation, meditation, recuperation.",
    "Five of Swords": "Conflict, disagreements, win at all costs, defeat.",
    "Six of Swords": "Transition, change, leaving behind, healing.",
    "Seven of Swords": "Betrayal, deception, getting away with something, strategy.",
    "Eight of Swords": "Negative thoughts, self-imposed imprisonment, victim mentality.",
    "Nine of Swords": "Anxiety, worry, fear, depression, nightmares.",
    "Ten of Swords": "Painful endings, deep wounds, betrayal, collapse.",
    "Page of Swords": "New ideas, curiosity, thirst for knowledge, communication.",
    "Knight of Swords": "Action, speed, ambition, driven to succeed.",
    "Queen of Swords": "Independent, unbiased judgment, clear boundaries.",
    "King of Swords": "Mental clarity, intellectual power, truth, authority.",

    # Suit of Pentacles
    "Ace of Pentacles": "A new financial or career opportunity, abundance, manifestation.",
    "Two of Pentacles": "Multiple priorities, time management, adaptability.",
    "Three of Pentacles": "Teamwork, collaboration, learning, implementation.",
    "Four of Pentacles": "Saving money, security, conservatism, scarcity mindset.",
    "Five of Pentacles": "Financial loss, poverty, isolation, worry.",
    "Six of Pentacles": "Giving, receiving, sharing wealth, generosity.",
    "Seven of Pentacles": "Long-term view, sustainable results, perseverance, investment.",
    "Eight of Pentacles": "Apprenticeship, repetitive tasks, mastery, skill development.",
    "Nine of Pentacles": "Abundance, luxury, self-sufficiency, financial independence.",
    "Ten of Pentacles": "Legacy, culinary roots, family, wealth, long-term security.",
    "Page of Pentacles": "Manifestation, financial opportunity, skill development.",
    "Knight of Pentacles": "Hard work, productivity, routine, conservatism.",
    "Queen of Pentacles": "Nurturing, practical, providing financially, working parent.",
    "King of Pentacles": "Wealth, business acumen, leadership, security."
}

print("--- Welcome to the Digital Oracle ---")
input("Take a deep breath, focus on your question, and press Enter to draw a card...")

# Pull all card names into a list so random.choice works
card_names = list(TAROT_DECK.keys())
random_card = random.choice(card_names)

# Look up the meaning using the chosen card name
meaning = TAROT_DECK[random_card]

print("--- Welcome to the Digital Oracle ---")
input("Focus on your situation, and press Enter to draw a Past, Present, and Future spread...")

# 1. Pull all card names into a list
card_names = list(TAROT_DECK.keys())

# 2. Draw 3 UNIQUE cards at once (prevents duplicate cards in the same reading)
drawn_cards = random.sample(card_names, 3)

# 3. Define the positions for the spread
positions = ["PAST (What led to this situation)", "PRESENT (Your current energy)", "FUTURE (The likely outcome)"]
orientations = ["Upright", "Reversed"]

print("\n=== Your Three-Card Spread ===")

# 4. Loop through each position and assign a drawn card
for i in range(3):
    current_position = positions[i]
    random_card = drawn_cards[i]
    drawn_orientation = random.choice(orientations)
    meaning = TAROT_DECK[random_card]
    
    print(f"\n✨ POSITION: {current_position} ✨")
    
    if drawn_orientation == "Upright":
        print(f"🔮 {random_card} ({drawn_orientation})")
        print(f"Meaning: {meaning}")
    else:
        print(f"🙃 {random_card} ({drawn_orientation})")
        print(f"Meaning (Inverted Energy): Internalized, blocked, or the shadow side of: {meaning}")
        
print("\n==============================")
