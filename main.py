from data import question_data
from question_model import Question
import random


Question1 = Question()
while True:
    random_index = Question1.ask()
    answer = input('True or False: ').capitalize()
    Question1.check_answer(answer,random_index)
    while True:
        choice = input('Do you want to continue(y/n): ').lower()
        if choice == 'y':
            break
        elif choice == 'n':
            print('Have a great day!')
            quit()
        else:
            print('Invalid choice!pick again.')    