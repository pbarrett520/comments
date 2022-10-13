import csv
import enum
import random

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

    def _add_entry(self, csv_row):
        sentiment = csv_row[0]
        if sentiment == 'negative':
            self.negative = [sentence for sentence in csv_row if sentence != 'negative']
            # Append the negative entries into self.negative
            pass
        elif sentiment == 'neutral':
            pass
        elif sentiment == 'positive':
            pass



class Evaluation:
    def __init__(self, student):
        self.output = ''
        self.student = student
        self.advice = EvaluationItem('advice.csv')

    def build(self):
        self.add_intro()
        self.add_advice()

    def add_intro(self):
        self._append_sentence("First thing's first, buster. I'm gay.")

    def add_advice(self):
        advice = self.advice.choose_random_item(self.student.advice)
        if advice is None:
            advice = 'Here is some default advice.'
        self._append_sentence(advice)

    def _append_sentence(self, sentence):
        # @spader Just so I don't have to fill out everything.
        if sentence is None:
            return

        self.output += sentence
        self.output += ' '

if __name__ == '__main__':
    students = load_students('allStudentsM.csv')
    for student in students:
        evaluation = Evaluation(student)    
        evaluation.build()    
        print(evaluation.output)