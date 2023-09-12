import csv
import random
import re

class Student:
    def __init__(self, csv_row):
       self.name = csv_row[0]
       self.intro = csv_row[1] 
       self.academics = csv_row[2] 
       self.assignments = csv_row[3] 
       self.behavior = csv_row[4] 
       self.soc_emo = csv_row[5] 
       self.advice = csv_row[6] 
       self.bye = csv_row[7] 

def load_students(csv_filename):
    rows = []
    with open(csv_filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            student = Student(row)
            rows.append(student)

    # CSV parser returns the column names first. This is hacky, but who cares.
    del rows[0]
    return rows
    
class EvaluationItem:
    def __init__(self, csv_filename):
        self.negative = []
        self.neutral = []
        self.positive = []

        with open(csv_filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._add_entry(row)

    def choose_random_item(self, sentiment):
        if sentiment == 'negative':
            return random.choice(self.negative)
        elif sentiment == 'positive':
            return random.choice(self.positive)
        else:
            return random.choice(self.neutral)

    def _add_entry(self, csv_row):
        sentiment = csv_row[0]
        if sentiment == 'negative':
            self.negative = [sentence for sentence in csv_row if sentence != 'negative']
        elif sentiment == 'positive':
            self.positive = [sentence for sentence in csv_row if sentence != 'positive']
        else:
            self.neutral = [sentence for sentence in csv_row if sentence != 'neutral']

        


class Evaluation:
    def __init__(self, student):
        self.output = ''
        self.student = student
        self.academics = EvaluationItem('/Users/patrick/Documents/comments/app/academics.csv')
        self.assignments = EvaluationItem('/Users/patrick/Documents/comments/app/assignments.csv')
        self.behavior = EvaluationItem('/Users/patrick/Documents/comments/app/behavior.csv')
        self.soc_emo = EvaluationItem('/Users/patrick/Documents/comments/app/soc-emo.csv')
        self.advice = EvaluationItem('/Users/patrick/Documents/comments/app/advice.csv')        

    def build(self):
        self.add_academics()
        self.add_assignments()
        self.add_behavior()
        self.add_soc_emo()
        self.add_advice()
        self.add_advice()
        
    def add_academics(self):
        academics = self.academics.choose_random_item(self.student.academics)
        if academics is None:
            academics = 'Here is some default advice.'
        self._append_sentence(academics)
    
    def add_assignments(self):
        assignments = self.assignments.choose_random_item(self.student.assignments)
        if assignments is None:
            assignments = 'Here is some default advice.'
        self._append_sentence(assignments)
    
    def add_behavior(self):
        behavior = self.behavior.choose_random_item(self.student.behavior)
        if behavior is None:
            behavior = 'Here is some default advice.'
        self._append_sentence(behavior)
    
    def add_soc_emo(self):
        soc_emo = self.soc_emo.choose_random_item(self.student.soc_emo)
        if soc_emo is None:
            soc_emo = 'Here is some default advice.'
        self._append_sentence(soc_emo)

    def add_advice(self):
        advice = self.advice.choose_random_item(self.student.advice)
        if advice is None:
            advice = 'Here is some default advice.'
        self._append_sentence(advice)

    def _append_sentence(self, sentence):
        if sentence is None:
            return

        self.output += sentence
        self.output += ' '

    def replace_name(self, output):
        #This method will replace hashmarks with student names
        hashtag = re.compile('#')
        return re.sub(hashtag, self.student, output)
    
def feminize(output: str) -> str:
    #This mehtod swaps male pronouns to female
    pronouns = {"He":"She","Him":"Her","His":"Hers","Himself":"Herself","He's":"She's","he":"she","him":"her","his":"hers",
                "himself":"herself","hisself":"herself","he's":"she's", "him.":"her.","his.":"hers.", "himself.":"herself."}
        
    words = output.split()  # Split the sentence into words
    feminized = [pronouns.get(word, word) for word in words]
            
    return ' '.join(feminized)  # Join the words back into a sentence


if __name__ == '__main__':
    male_students = load_students('/Users/patrick/Documents/comments/app/allStudentsM.csv')
    for studentM in male_students:
        evaluationM = Evaluation(studentM)    
        evaluationM.build()   
        print(evaluationM.output)

    female_students = load_students('/Users/patrick/Documents/comments/app/allStudentsF.csv')
    for studentF in female_students:
        evaluationF = Evaluation(studentF)
        evaluationF.build()
        print(feminize(evaluationF.output))