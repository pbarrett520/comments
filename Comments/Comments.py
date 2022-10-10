import random
import tkinter as tk

app = tk.Tk()
canvas = tk.Canvas(app, width=750, height=550)
title = app.title("Automated Comments for Everyone!")
scroll_bar = tk.Scrollbar(app,)

textbox_m = tk.Text()
textbox_m.pack()
instructions_m= tk.Label(app,text="Enter All Male Names Here")
instructions_m.pack()

textbox_f = tk.Text()
textbox_f.pack()
instructions_f =tk.Label(app,text="Enter All Female Names Here")
instructions_f.pack()

finished = tk.Button(app,text="Done: Continue to Comments")
finished.pack()


name_file = open('names.txt', "r")
names = name_file.read().splitlines()
name_list = [eval(name) for name in names]
#print(name_list)
pronouns = {"He":"She","Him":"Her","His":"Hers","Himself":"Herself"}
xx_names = []
xy_names = []

def toggle(boolean):
    return not boolean

while True:
    get_xx_name = input('Input all female names here, click button after each entry. Type "done" when done!')
    xx_names.append(get_xx_name)
    if get_xx_name == "done" or "Done" or "DONE":
        break
    


good_comments = [" is a good student.", " performs well in class.", " always exceeds my expectations.", 
                 "It is always a pleasure to teach  .", " is awesome."]

neutral_comments= ["bleh", "blah", "boop", "v", "q"]

bad_comments = ["beep", "bip", "boop", "blip", "blop"]

def selector(comments):
    for items in comments:
        if isinstance(items,int) == False:
            items = []
            print(items)
        elif items > 0:
            print(random.choice(good_comments))
        elif items < 0:
            print(random.choice(bad_comments))
        else:
            print(random.choice(neutral_comments))

#for tups in name_list:
    #selector(tups)

app.mainloop()