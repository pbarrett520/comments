import csv
import random
import re
hashtag = re.compile(r'#')
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