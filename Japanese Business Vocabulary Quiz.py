import random

# List for Business-related English words and their Japanese translations (in romaji)
translations = {
    "meeting": "kaigi",
    "contract": "keiyaku",
    "company": "kaisha",
    "schedule": "yotei",
    "report": "houkoku",
    "email": "meeru",
    "document": "shiryou",
    "manager": "buchou",
    "client": "kokyaku",
    "presentation": "purezen",
    "agreement": "doui",
    "invoice": "seikyuu-sho",
    "salary": "kyuuryou",
    "office": "jimusho",
    "project": "purojekuto",
    "deadline": "shimekiri",
    "budget": "yosan",
    "approval": "shounin",
    "negotiation": "koushou",
    "meeting room": "kaigishitsu",
    "conference": "kaigi",
    "payment": "shiharai",
    "team": "chiimu",
    "boss": "joushi",
    "business trip": "shucchou",
    "working hours": "kinmu jikan",
    "leave": "kyuuka",
    "proposal": "teian",
    "plan": "keikaku",
    "decision": "kettei",
    "performance": "seiseki",
    "task": "ninmu"
}

# Counter for correct answers
correct_count = 0

# Shuffle the word pairs for randomized quiz order
items = list(translations.items())
random.shuffle(items)

# Quiz loop
for english_word, japanese_word in items:
    user_input = input(f"What is the Japanese translation for '{english_word}'? ").strip().lower()

    if user_input == japanese_word.lower():
        print("That is correct!")
        correct_count += 1
    else:
        print(f"That is incorrect, the Japanese translation for '{english_word}' is {japanese_word}.")

    print()  # Blank line for readability

# Final score summary
print(f"You got {correct_count}/{len(translations)} words correct, come study again soon!")