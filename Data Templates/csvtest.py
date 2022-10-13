import csv
import random
import re
hashtag = re.compile(r'#')

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

def load_csv(csv_filename, item_type):
    rows = []
    with open(csv_filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            # Instantiate an object of the type passed in, passing the row data to its constructor.
            # This means that each data class (like Student) needs to have a constructor that
            # accepts a row and fills out the data
            item = item_type(row)

            # Add this object to our list
            rows.append(item)

    # CSV parser returns the column names first. This is hacky, but who cares.
    del rows[0]
    return rows

students = load_csv('allStudentsM.csv', Student)

for student in students:
    print(student.name)

##### Define function to turn csv tables to lists of lists #####
def get_data(csvFile):
    outList = list()
    reader = csv.reader(open(csvFile))
    for row in reader:
        outList.append(row)
    return outList
##### Turn each csv table to list of lists so it can be manipulated #####
students_m = get_data('allStudentsM.csv')
students_f = get_data('allStudentsF.csv')
intro = get_data('intro.csv')
academics = get_data('academics.csv')
assignments = get_data('assignments.csv')
behavior = get_data('behavior.csv')
soc_emo = get_data('soc-emo.csv')
advice = get_data('advice.csv')
bye = get_data('bye.csv')
##### Begin aggregating comments #####

intro_str = f"{random.choice(intro[1][1:])} {random.choice(intro[2][1:])}" # These have a simpler structure, so let's just make format strings for them right away
bye_str = f"{random.choice(intro[1][1:])} {random.choice(intro[2][1:])}"



def concatenate(student_list):
    for part in student_list:
        part[1] == intro_str
        part[6] == bye
        if part[2] == 1:
            part[2] == random.choice(academics[1][1:])
        elif part[2] == 3:
            part[2] == random.choice(academics[3][1:])
        else:
            part[2] == random.choice(academics[2][1:]) # Default to neutral comments in case of typos

print(students_m[0])