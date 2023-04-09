import tkinter as Quiz
from tkinter import StringVar

root = Quiz.Tk()
root.title("Quiz")
root.geometry('555x750')



from PIL import Image ,ImageTk
from urllib.request import urlopen

image_urls = [
    'https://photodentro.edu.gr/lor/retrieve/65797/thumbnail_m-diamerismata1_map_v2.1.jpg_teaser.jpg',
    'https://static.thenounproject.com/png/3853034-200.png',
    'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/09/f7/14/mystras.jpg?w=300&h=300&s=1',
    'https://signature.gr/wp-content/uploads/2022/11/42-300x300.jpg',
    'https://www.gethouse.gr/img/posts/20134309233812.jpeg',
]

u=urlopen(image_urls[0])

raw_data=u.read()
u.close()

photo = ImageTk.PhotoImage(data=raw_data)
label = Quiz.Label(image=photo)
label.pack(side=Quiz.BOTTOM)







questions =['Ποσα γεωγραφικα διαμερισματα εχει η Ελλαδα','Στην Κρητη ανηκει ο Νομος:','Στην Πελοποννησο ανηκει ο Νομος:','Στην Θεσσαλια ανηκει ο Νομος:','Στην Ηπειρος ανηκει ο Νομος:'] 
options=[['5','9','51','10','9'],['Καρδιτσας','Αργολιδας','Λασιθιου','Ηλειας','Λασιθιου'],['Λακωνιας','Φθιωτιδας','Καστοριας','Εβρου','Λακωνιας'],['Ιωαννινων','Φωκιδας','Βοιωτιας','Μαγνησιας','Μαγνησιας'],['Κιλκις','Θεσπρωτιας','Κοζανης','Τρικαλων','Θεσπρωτιας']]

 
frame=Quiz.Frame(root,padx=19,pady=10,bg='#fff')
question_label=Quiz.Label(frame,height=5,width=30,bg='#ddd',font=('Verdana',20),wraplength=500)


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)


#Making the buttons for the options on the app
option1 = Quiz.Radiobutton(frame,bg='#fff',variable=v1,font=('Verdana',20),command = lambda : checkAnswer(option1))
option2 = Quiz.Radiobutton(frame,bg='#fff',variable=v2,font=('Verdana',20),command = lambda : checkAnswer(option2))
option3 = Quiz.Radiobutton(frame,bg='#fff',variable=v3,font=('Verdana',20),command = lambda : checkAnswer(option3))
option4 = Quiz.Radiobutton(frame,bg='#fff',variable=v4,font=('Verdana',20),command = lambda : checkAnswer(option4))
#adding the potition of the 'options' buttons
option1.grid(sticky = 'W',row=1,column=0) 
option2.grid(sticky = 'W',row=2,column=0)
option3.grid(sticky = 'W',row=3,column=0)
option4.grid(sticky = 'W',row=4,column=0)
#making the 'next' button
button_next = Quiz.Button(frame, text='Next Question',bg="Light blue",font=('Verdana',15), command = lambda : displayNextQuetion())
frame.pack(fill='both',expand=True)
question_label.grid(row=0,column=0)
#potition of the 'next' button
button_next.grid(sticky = 'E',row=6,column=0)

index=0
correct=0

#create a funtion to disable radiobuttons
def disableButtons(state):
    option1['state']=state
    option2['state']=state
    option3['state']=state
    option4['state']=state
#create a function to check the selected answer
def checkAnswer(radio):
    global correct, index
    # the 4th item is the correct answer
    # we will chek if the user selected answer with the 4th item
    if radio['text']==options[index][4]:
        correct +=1 

    index +=1
    disableButtons('disable')

def displayNextQuetion():
    global correct,index

    if button_next['text'] == 'Restart The Quiz':
        correct=0
        index=0
        question_label['bg']='light grey'
        button_next['text']= 'Next Question'

    if index == len(options):
        question_label['text'] = str(correct) + " / " + str(len(options)) 
        button_next['text'] = 'Restart The Quiz'
        if correct >= len(options)/2:
            question_label['bg']='green'
        else:
            question_label['bg']='red'
    else:
        question_label['text'] = questions[index]

         # update the image
        u = urlopen(image_urls[index])
        raw_data = u.read()
        u.close()
        photo = ImageTk.PhotoImage(data=raw_data)
        label.config(image=photo)
        label.image = photo

        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]

        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Check the results'

displayNextQuetion()

root.mainloop()

