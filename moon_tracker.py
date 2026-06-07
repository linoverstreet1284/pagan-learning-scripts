import datetime

SABBATS = {
    "Litha (Summer Solstice)": datetime.date(2026, 6, 21),
    "Lughnasadh (Lammas)": datetime.date(2026, 8, 1),
    "Samhain (The Witch’s New Year)": datetime.date(2026, 10, 31),
    "Yule (Winter Solstice)": datetime.date(2026, 12, 21),
}

FULL_MOONS = {
    "Strawberry Full Moon": datetime.date(2026, 5, 31),
    "Buck Full Moon": datetime.date(2026, 6, 29),
    "Sturgeon Full Moon": datetime.date(2026, 8, 27),
    "Harvest Full Moon": datetime.date(2026, 9, 26),
    "Hunter's Full Moon": datetime.date(2026, 10, 25),
    "Beaver Full Moon": datetime.date(2026, 11, 24),
    "Cold Full Moon": datetime.date(2026, 12, 23),
}

NEW_MOONS = {
    "Gemini New Moon": datetime.date(2026, 6, 14),
    "Cancer New Moon": datetime.date(2026, 7, 14),
    "Leo New Moon": datetime.date(2026, 8, 12),
    "Virgo New Moon": datetime.date(2026, 10, 10),
    "Scorpio New Moon": datetime.date(2026, 11, 9),
    "Sagittarius New Moon": datetime.date(2026, 12, 8)
}

events = {**SABBATS, **FULL_MOONS, **NEW_MOONS}

def check_next_event():
    today = datetime.date.today()
    print(f"Today's Date: {today}")
    print("\n--- Upcoming Celestial & Sacred Events ---")
    
    for event_name, event_date in sorted(events.items(), key=lambda item: item[1]):
        delta = event_date - today
        days_left = delta.days
        
        if days_left > 0:
            print(f"🌕 {event_name}: {days_left} days away")
        elif days_left == 0:
            print(f"✨ {event_name} is TODAY! Blessed be.")

if __name__ == "__main__":
    check_next_event()
