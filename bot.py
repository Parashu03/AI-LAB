import spacy
import csv
import os

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Path to CSV file
csv_path = r'D:\College notes\4th sem\AI\chatbot\chatbot cie\using nlp\student_marks.csv'

# Load marks from CSV
def load_marks():
    if not os.path.exists(csv_path):
        print("Error: CSV file not found!")
        return []
    
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

# Find mark for a given name
def get_cie_mark(name):
    data = load_marks()
    for row in data:
        if row['name'].lower() == name.lower():
            return f"{row['name']} has scored {row['cie_mark']} in {row['subject']}."
    return "Student not found."

# Extract name using spaCy
def extract_name(message):
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

# Preprocess and standardize input to handle variations
def preprocess_input(user_input):
    user_input = user_input.lower()  # Convert input to lowercase
    return user_input

# Main interaction loop
def main():
    print("Ask about a student's CIE mark (e.g., 'What is the mark of John?')\nType 'exit' to quit.")
    while True:
        user_input = input("You: ")
        user_input = preprocess_input(user_input)
        
        if user_input in ["exit", "quit"]:
            break
        
        name = extract_name(user_input)
        print(f"Extracted Name: {name}")  # Debug print
        
        if name:
            response = get_cie_mark(name)
        else:
            response = "I couldn't understand the student name. Please try again with a different question."
        
        print("Bot:", response)

if __name__ == '__main__':
    main()

