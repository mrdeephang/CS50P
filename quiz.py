import json
import random

def load_questions(filename):
    with open(filename, "r") as file:
        return json.load(file)

def save_questions(filename, questions):
    with open(filename, "w") as file:
        json.dump(questions, file, indent=4)

def ask_question(question_data):
    question = question_data["question"]
    options = question_data["options"]
    answer = question_data["answer"]

    print(f"\n{question}")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    while True:
        try:
            choice = int(input("Enter your answer (1-4): "))
            if 1 <= choice <= len(options):
                if options[choice - 1] == answer:
                    print("✅ Correct!")
                    return True
                else:
                    print(f"❌ Incorrect! The correct answer is: {answer}")
                    return False
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

def practice_quiz(questions):
    print("\nAvailable Categories:")
    for idx, category in enumerate(questions.keys(), 1):
        print(f"{idx}. {category}")

    while True:
        try:
            category_choice = int(input("Select a category number: "))
            if 1 <= category_choice <= len(questions):
                selected_category = list(questions.keys())[category_choice - 1]
                break
            else:
                print("Please select a valid category number.")
        except ValueError:
            print("Please enter a number.")

    print(f"\nYou selected: {selected_category}")
    selected_questions = questions[selected_category]
    random.shuffle(selected_questions)

    score = 0
    for question_data in selected_questions:
        if ask_question(question_data):
            score += 1

    print(f"\n🎉 Quiz Over! Your final score: {score}/{len(selected_questions)}")

def add_questions(questions, filename):
    while True:
        print("\nAvailable Categories:")
        for idx, category in enumerate(questions.keys(), 1):
            print(f"{idx}. {category}")
        print(f"{len(questions) + 1}. Create New Category")

        try:
            category_choice = int(input("Select a category number or create a new one: "))
            if 1 <= category_choice <= len(questions):
                selected_category = list(questions.keys())[category_choice - 1]
            elif category_choice == len(questions) + 1:
                selected_category = input("Enter the name of the new category: ").strip()
                if selected_category not in questions:
                    questions[selected_category] = []
                else:
                    print("Category already exists.")
            else:
                print("Please select a valid category number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        question_text = input("Enter the question: ").strip()
        options = []
        for i in range(4):
            option = input(f"Enter option {i + 1}: ").strip()
            options.append(option)
        while True:
            answer = input("Enter the correct answer (it must match one of the options): ").strip()
            if answer in options:
                break
            else:
                print("The answer must match exactly one of the provided options.")

        questions[selected_category].append({
            "question": question_text,
            "options": options,
            "answer": answer
        })

        save_questions(filename, questions)
        print("✅ Question added successfully!")

        another = input("Do you want to add another question? (yes/no): ").strip().lower()
        if another != 'yes':
            break

def main():
    filename = "questions.json"
    questions = load_questions(filename)

    while True:
        print("\n🎮 Quiz Game Menu")
        print("1. Practice Quiz")
        print("2. Add Questions")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            practice_quiz(questions)
        elif choice == '2':
            add_questions(questions, filename)
        elif choice == '3':
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Please enter a valid option (1, 2, or 3).")

if __name__ == "__main__":
    main()
