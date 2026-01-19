questions = [

    {
        "text": "What gas do plants absorb during photosynthesis?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correct": 2,
    },

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

def print_welcome_message() -> None:
    print("Welcome to the Holton College Quiz!")
    print("Please answer with the number (1, 2, 3, or 4) of your choice.\n")



