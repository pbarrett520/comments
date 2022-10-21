import csv
import enum
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

class Feminize:
    def __init__(self):
        pronouns = {"He":"She","Him":"Her","His":"Hers","Himself":"Herself","he":"she","him":"her","his":"hers","himself":"herself"}
    
    def change(self, text):
        
        pass
    


class StartEnd: # This class is broken and I need to figure out why
    def __init__(self, csv_filename):
        self.startEnd1 = []
        self.startEnd2 = []
    
        with open(csv_filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._add_startEnd(row)

    def choose_random_item(self, n):
        if n == 1 or '1':
            return random.choice(self.startEnd1)
        elif n == 2 or '2':
            return random.choice(self.startEnd2)
        
    def _add_startEnd(self, csv_row):
        order = csv_row[0]
        if order == 1 or '1':
            self.startEnd1 = [sentence for sentence in csv_row[1]]
        elif order == 2 or '2':
            self.startEnd2 = [sentence for sentence in csv_row[2]]

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
        self.intro = StartEnd('intro.csv')
        self.academics = EvaluationItem('academics.csv')
        self.assignments = EvaluationItem('assignments.csv')
        self.behavior = EvaluationItem('behavior.csv')
        self.soc_emo = EvaluationItem('soc-emo.csv')
        self.advice = EvaluationItem('advice.csv')
        self.bye = StartEnd('bye.csv')
        

    def build(self):
        self.add_intro()
        self.add_academics()
        self.add_assignments()
        self.add_behavior()
        self.add_soc_emo()
        self.add_advice()
        self.add_advice()
        self.add_bye()
    
    def add_intro(self):
        intro = self.intro.choose_random_item(self.student.intro)
        if intro is None:
            intro = 'Here is a default intro.'
        self._append_sentence(intro)
        
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

    def add_bye(self):
        bye = self.bye.choose_random_item(self.student.bye)
        if bye is None:
            bye = 'Here is a default bye.'
        self._append_sentence(bye)

    def _append_sentence(self, sentence):
        # @spader Just so I don't have to fill out everything.
        if sentence is None:
            return

        self.output += sentence
        self.output += ' '

    def replace_name(self, output):
        #This method will replace hashmarks with student names
        hashtag = re.compile('#')
        return re.sub(hashtag, self.student, output)
    
    def feminize(self, output):
        #This mehtod will swap male pronouns to female
        pronouns = {"He":"She","Him":"Her","His":"Hers","Himself":"Herself","he":"she","him":"her","his":"hers","himself":"herself"}
        for words in output:
            

if __name__ == '__main__':
    male_students = load_students('allStudentsM.csv')
    for studentM in male_students:
        evaluationM = Evaluation(studentM)    
        evaluationM.build()    
        print(evaluationM.output)

    female_students = load_students('allStudentsF.csv')
    for studentF in female_students:
        evaluationF = Evaluation(studentF)
        evaluationF.build()
        print(evaluationF.output)