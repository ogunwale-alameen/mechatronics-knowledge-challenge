# MECHATRONICS QUIZ MASTER
# Author: OGUNWALE AL-AMEEN OLAWALE
# Course: CTE213

questions = [
    {
        "topic": "Sensors",
        "question": "Which sensor is used to detect the presence of an object?",
        "options": ["A. Temperature sensor", "B. Proximity sensor", "C. Pressure sensor", "D. Light sensor"],
        "answer": "B",
        "hint": "It detects nearby objects without physical contact."
    },
    {
        "topic": "Control Systems",
        "question": "What is the main purpose of a feedback system?",
        "options": ["A. To increase noise", "B. To remove power", "C. To correct system errors", "D. To stop all operations"],
        "answer": "C",
        "hint": "It compares the actual output with the desired output."
    },
    {
        "topic": "Robotics",
        "question": "Which component allows a robot to move its joints?",
        "options": ["A. Actuator", "B. Resistor", "C. Capacitor", "D. Fuse"],
        "answer": "A",
        "hint": "It converts energy into mechanical movement."
    },
    {
        "topic": "Electronics",
        "question": "What is the unit of electrical resistance?",
        "options": ["A. Volt", "B. Ampere", "C. Watt", "D. Ohm"],
        "answer": "D",
        "hint": "Its symbol is the Greek letter Omega."
    },
    {
        "topic": "PLC",
        "question": "What does PLC stand for?",
        "options": ["A. Power Line Control", "B. Programmable Logic Controller", "C. Process Level Circuit", "D. Primary Logic Computer"],
        "answer": "B",
        "hint": "It is commonly used in industrial automation."
    },
    {
        "topic": "Mechanical Systems",
        "question": "Which device converts rotary motion into linear motion?",
        "options": ["A. Transformer", "B. Generator", "C. Lead screw", "D. Battery"],
        "answer": "C",
        "hint": "It uses a threaded shaft and a moving nut."
    },
    {
        "topic": "Electrical Systems",
        "question": "Which instrument measures electric current?",
        "options": ["A. Ammeter", "B. Voltmeter", "C. Thermometer", "D. Barometer"],
        "answer": "A",
        "hint": "Its name begins with the same letter as Ampere."
    },
    {
        "topic": "Microcontrollers",
        "question": "Which board is commonly used for beginner electronics projects?",
        "options": ["A. Monitor", "B. Printer", "C. Scanner", "D. Arduino"],
        "answer": "D",
        "hint": "It is a popular programmable development board."
    },
    {
        "topic": "Automation",
        "question": "What is the main function of an actuator?",
        "options": ["A. Store information", "B. Produce physical movement", "C. Display images", "D. Measure temperature"],
        "answer": "B",
        "hint": "It performs an action in response to a control signal."
    },
    {
        "topic": "Engineering",
        "question": "Which material is commonly used as an electrical conductor?",
        "options": ["A. Rubber", "B. Wood", "C. Copper", "D. Plastic"],
        "answer": "C",
        "hint": "It is widely used in electrical wiring."
    },
    {
        "topic": "Computer Programming",
        "question": "Which Python keyword is used to define a function?",
        "options": ["A. def", "B. loop", "C. function", "D. create"],
        "answer": "A",
        "hint": "It is a three-letter Python keyword."
    },
    {
        "topic": "Mechatronics",
        "question": "Mechatronics combines which major fields?",
        "options": ["A. Biology and Chemistry", "B. History and Geography", "C. Accounting and Economics", "D. Mechanical, Electrical and Computer Engineering"],
        "answer": "D",
        "hint": "It combines mechanical systems, electronics and computing."
    }
]


def display_menu():
    print("\n" + "=" * 45)
    print("       MECHATRONICS QUIZ MASTER")
    print("=" * 45)
    print("1. Start Quiz")
    print("2. View Instructions")
    print("3. Exit")


def display_instructions():
    print("\n--- QUIZ INSTRUCTIONS ---")
    print(f"1. The quiz contains {len(questions)} questions.")
    print("2. Each question has four options (A-D).")
    print("3. You have two attempts per question.")
    print("4. Correct on the first attempt = 5 points.")
    print("5. Correct on the second attempt = 2 points.")
    print("6. A wrong second attempt earns 0 points.")
    print("7. Your final result will be displayed.")


def calculate_grade(score):
    percentage = (score / (len(questions) * 5)) * 100

    if percentage >= 80:
        grade = "A - Excellent"
    elif percentage >= 70:
        grade = "B - Very Good"
    elif percentage >= 60:
        grade = "C - Good"
    elif percentage >= 50:
        grade = "D - Fair"
    else:
        grade = "F - Needs Improvement"

    return percentage, grade


def conduct_quiz():
    score = 0
    correct_answers = 0

    print("\nWelcome to the Mechatronics Challenge!")
    print(f"There are {len(questions)} questions. Answer carefully. Good luck!\n")

    for number, item in enumerate(questions, start=1):
        print("-" * 45)
        print(f"Question {number} of {len(questions)} | Topic: {item['topic']}")
        print(item["question"])

        for option in item["options"]:
            print(option)

        attempts = 0
        solved = False

        while attempts < 2 and not solved:
            answer = input("\nYour answer (A-D): ").strip().upper()

            if answer not in ("A", "B", "C", "D"):
                print("Invalid option! Enter A, B, C or D.")
                continue

            attempts += 1

            if answer == item["answer"]:
                points = 5 if attempts == 1 else 2
                score += points
                correct_answers += 1
                print(f"Correct! You earned {points} points.")
                solved = True
            elif attempts == 1:
                print("Not quite right!")
                print("HINT:", item["hint"])
                print("You have one more attempt.")
            else:
                print("Incorrect!")
                print("Correct answer:", item["answer"])

        if not solved:
            print("No points earned for this question.")

    show_result(score, correct_answers)


def show_result(score, correct_answers):
    maximum_score = len(questions) * 5
    percentage, grade = calculate_grade(score)

    print("\n" + "=" * 45)
    print("             QUIZ RESULTS")
    print("=" * 45)
    print("Student: OGUNWALE AL-AMEEN OLAWALE")
    print("Total Questions:", len(questions))
    print("Questions Correct:", correct_answers)
    print("Final Score:", score, "/", maximum_score)
    print(f"Percentage: {percentage:.1f}%")
    print("Performance:", grade)
    print("=" * 45)

    if percentage >= 70:
        print("Great work! Keep developing your skills.")
    else:
        print("Keep practising. You can do better!")


def main():
    while True:
        display_menu()

        try:
            choice = int(input("\nSelect an option (1-3): "))

            if choice == 1:
                conduct_quiz()
            elif choice == 2:
                display_instructions()
            elif choice == 3:
                print("\nThank you for using Mechatronics Quiz Master!")
                print("Goodbye!")
                break
            else:
                print("Please select a number between 1 and 3.")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
