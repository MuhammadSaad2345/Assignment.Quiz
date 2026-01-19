"Holton College Digital Quiz System - Console-based quiz application."

from typing import List, Dict
def get_questions() -> List[Dict[str, object]]:
    """
    Return a list of quiz questions grouped into 3 topics.
    Each question includes:
    - text
    - options
    - correct (1-based index)
    """

    questions = [

        {
            "text": "What gas do plants absorb during photosynthesis?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "correct": 2,
        },
        {
            "text": "What is the chemical symbol for water?",
            "options": ["H2O", "O2", "CO2", "HO"],
            "correct": 1,
        },
        {
            "text": "How many planets are in our solar system?",
            "options": ["7", "8", "9", "10"],
            "correct": 2,
        },
        {
            "text": "What part of the cell contains genetic material?",
            "options": ["Nucleus", "Ribosome", "Cell Wall", "Mitochondria"],
            "correct": 1,
        },
        {
            "text": "What force keeps us on the ground?",
            "options": ["Magnetism", "Friction", "Gravity", "Electricity"],
            "correct": 3,
        },


        {
            "text": "Which is the largest continent in the world?",
            "options": ["Africa", "Asia", "Europe", "North America"],
            "correct": 2,
        },
        {
            "text": "Which country has the largest population?",
            "options": ["USA", "India", "China", "Brazil"],
            "correct": 3,
        },
        {
            "text": "What is the longest river in the world?",
            "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
            "correct": 2,
        },
        {
            "text": "Which country is known as the Land of the Rising Sun?",
            "options": ["China", "Japan", "Thailand", "South Korea"],
            "correct": 2,
        },
        {
            "text": "Which ocean is the largest?",
            "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
            "correct": 3,
        },


        {
            "text": "What does CPU stand for?",
            "options": [
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Power Utility",
                "Control Program Unit"
            ],
            "correct": 1,
        },
        {
            "text": "Which company created the iPhone?",
            "options": ["Samsung", "Apple", "Google", "Microsoft"],
            "correct": 2,
        },
        {
            "text": "Which programming language uses a snake as its logo?",
            "options": ["Java", "C++", "Python", "Ruby"],
            "correct": 3,
        },
        {
            "text": "What does 'www' stand for in a website address?",
            "options": [
                "World Web Window",
                "Wide World Web",
                "World Wide Web",
                "Web World Wide"
            ],
            "correct": 3,
        },
        {
            "text": "Which device stores long-term data?",
            "options": ["RAM", "CPU", "Hard Drive", "GPU"],
            "correct": 3,
        },
    ]

    return questions


def print_welcome_message() -> None:
    print("Welcome to the Holton College Quiz!")
    print("Please answer with the number (1, 2, 3, or 4) of your choice.\n")


def ask_question(question: Dict[str, object], question_number: int) -> bool:
    print(f"Question {question_number}: {question['text']}")
    for index, option in enumerate(question["options"], start=1):
        print(f"{index}. {option}")

    user_answer = get_valid_answer(len(question["options"]))

    if check_answer(user_answer, question["correct"]):
        print("Correct!\n")
        return True

    print(f"Incorrect. The correct answer was {question['correct']}.\n")
    return False


def get_valid_answer(num_options: int) -> int:
    while True:
        user_input = input("Your answer: ").strip()
        if user_input.isdigit():
            answer = int(user_input)
            if 1 <= answer <= num_options:
                return answer
        print(f"Please enter a number between 1 and {num_options}.")


def check_answer(user_answer: int, correct_answer: int) -> bool:
    return user_answer == correct_answer


def run_quiz() -> None:
    questions = get_questions()
    score = 0

    print_welcome_message()

    for index, question in enumerate(questions, start=1):
        if ask_question(question, index):
            score += 1

    print("Quiz Complete!")
    print(f"You scored {score} out of {len(questions)} correct.")
    print("Thank you for playing.")


if __name__ == "__main__":
    run_quiz()



