import spacy
import csv
import os

nlp = spacy.load("en_core_web_sm")
csv_path = r'D:\College notes\4th sem\AI\chatbot\chatbot cie\using nlp\student_marks.csv'

def load_marks():
    if not os.path.exists(csv_path):
        print("Error: CSV file not found!")
        return []
    
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def get_cie_mark(name):
    data = load_marks()
    for row in data:
        if row['name'].lower() == name.lower():
            return f"{row['name']} has scored {row['cie_mark']} in {row['subject']}."
    return "Student not found."


def extract_name(message):
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def main():
    print("Ask about a student's CIE mark (e.g., 'What is the mark of John?')\nType 'exit' to quit.")
    while True:
        user_input = input("You: ").lower()
      
        
        if user_input in ["exit", "quit"]:
            break
        
        name = extract_name(user_input)
        print(f"Extracted Name: {name}") 
        
        if name:
            response = get_cie_mark(name)
        else:
            response = "I couldn't understand the student name. Please try again with a different question."
        
        print("Bot:", response)

if __name__ == '__main__':
    main()

