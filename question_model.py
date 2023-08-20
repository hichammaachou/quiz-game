from data import question_data
import random
class Question:
    
    def __init__(self):
        self.question = None
        self.score = 0
        self.question_num = 0
       
    def ask(self):
        random_index = random.randint(0,11) 
        self.question = question_data[random_index]["text"]
        print(self.question)
        return random_index
    

    def check_answer(self,answer,random_index):
        
        if answer == question_data[random_index]["answer"]:
            print('Correct!')
            self.score += 1 
            self.question_num+=1
            print(f'your score is {self.score}/{self.question_num}')
        else:
            print('Wrong!') 
            self.question_num+=1
            print(f'your score is {self.score}/{self.question_num}')
