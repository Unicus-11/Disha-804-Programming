"""CLI Quiz App
Task 2 -  CLI Quiz App
Make a console-based quiz program. User should answer 5 multiple-choice questions, and the final score should be shown. Arrays/Lists, Input handling, Conditional logic"""

# Creatiing dictionary of question 


questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A) Python", "B) HTML", "C) C++", "D) Java"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
        "answer": "C"
    },
    {
        "question": "Which animal is known as the King of Jungle?",
        "options": ["A) Tiger", "B) Lion", "C) Elephant", "D) Bear"],
        "answer": "B"
    }
]


score = 0


question_number = 1

for question_item in questions:
    print(f"\nYour question is: {question_item['question']}")
    
    for option in question_item["options"]:
        print(option)
    
    answer = input("Your answer (A/B/C/D): ").upper()
    
    if answer == question_item["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question_item['answer']}.")
           
    question_number += 1


print(f"\nYour final score: {score} out of {len(questions)}")
