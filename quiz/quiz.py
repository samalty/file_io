import random
from random import shuffle

def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")
    
    option = input("Enter option: ")
    return option
    
def ask_questions():
    questions = []
    answers = []
    
# Using the with block, we open our questions.txt file
    
    with open("questions.txt", "r")as file:
        lines = file.read().splitlines()

# The enumerate function turns each list into a tuple with a line number stored in 'i' and the text in 'text'.
# So, if 'i', or the line number, is even, we assume it to be a question. If it's odd, it'll be an answer.
# Questions are even because the first line of our questions.txt file was 0, and it was a question.

    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
            shuffle(questions)
        else:
            answers.append(text)
            shuffle(answers)
            
        number_of_questions = len(questions)
        questions_and_answers = zip(questions, answers)
        
        score = 0
            
# The zip function is used to put everything together into another tuple in memory.
# This tuple will look something like: ("In which city was the first skyscraper built?", "Chicago")
            
    for question, answer in zip(questions, answers):
        guess = input(question + "> ")
        if guess == answer:
            score += 1
            print("Correct")
            print(score)
        else:
            print("Wrong")
            
    print("You got {0} correct out of {1}".format(score, number_of_questions))
    
def add_question():
    print("")
    question = input("Enter a question\n> ")
    
    print("")
    print("OK then, tell me the answer")
    answer = input("{0}\n> ".format(question))
    
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()
    
def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You selected 'Ask questions'")
            ask_questions()
        elif option == "2":
            print("You selected 'Add a question'")
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid option")
        print("")

game_loop()