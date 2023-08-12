import random

def load_questions_and_answers(file_name):
    qa = {}  # Initialize an empty dictionary to store questions and answers
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip("\n")
            parts = stripped_line.split("|||")
            if len(parts) == 2:  # Make sure the line has the correct format
                question = parts[0]
                answer = parts[1]
                qa[question] = answer
    return qa


def get_random_question(qa):
    if not qa:  # Check if the dictionary is empty
        return None
        
    # Use random.choice() to select a random question (key) from the dictionary
    random_question = random.choice(list(qa.keys()))
    return random_question


def ask_question(qa):
    question=get_random_question(qa) 
    print(question)
    answer=input("Enter response: ")
    if answer==qa[question]:
        print("correct!")
        del qa[question] # Remove the question from the dictionary
        return True
        
    else:
        print("incorrect!")
        return False


def main():
    file_name = input('What is the name of the QA file? ')
    number_of_questions = int(input('How many questions should be asked? '))
    questions_answers = load_questions_and_answers(file_name)
    correct_count = 0
    for i in range(number_of_questions):
        if ask_question(questions_answers):
            correct_count += 1
    print('You got', correct_count, 'out of', number_of_questions, 'correct.')
    print('Your percentage grade: ' + str(correct_count / number_of_questions * 100) + '%')

main()