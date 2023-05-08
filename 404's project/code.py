#import everything from tkinter
from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

#import json to use json file for data
import json

choiceWindow = Tk()

option_selected = IntVar()


def main():
    # Add image file
    bg = PhotoImage(file = "Background.png")
    
    # Show image using label
    label1 = Label( choiceWindow, image = bg)
    label1.place(x = 0, y = 0)

    # set the size of the GUI Window
    choiceWindow.geometry("800x450")

    #setting title
    choiceWindow.title("QUESTIONNAIRE APP")

    choiceWindow.resizable(width=False, height=False)

    #Placing Main Questionarre App

    options()


    choiceWindow.mainloop()


def options():

    question_number = Label(choiceWindow, bg= "#1A1536",fg="white" ,text="WELCOME USER!\n SELECT DIFFICULTY LEVEL!\n", width=35,
        font=( 'times' ,12, 'bold' ), anchor= 'w' )

    question_number.place(x=220, y=100)

    y_pos = 180
    i = 0


    common_bg = '#1A1536'
    common_fg = '#ffffff'  # pure white
    myText = "Grade "


    
    while i < 5:
        
        myText+= str( i + 1)

        # setting the radio button properties
        radio_btn = Radiobutton(choiceWindow ,fg=common_fg, bg=common_bg,
                        activebackground=common_bg, activeforeground=common_fg, selectcolor=common_bg
                        ,text=myText,variable=option_selected,value = i+1,font = ("ariel",14))

        
        radio_btn.place(x = 400, y = y_pos)
        
        # incrementing the y-axis position by 40
        y_pos += 40

        i+= 1

        myText = "Grade "

    option_selected.set(1)

    next_button = Button(choiceWindow, text="Next",command=button_next_command,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))

        
    next_button.place(x=570,y=330)




#class to define the components of the GUI
class Questionarre:

    def __init__(self,mainWindow,questions,options,answers):

        self.mainWindow = mainWindow

        self.question = questions

        self.answer = answers

        self.option = options

        # set question number to 0
        self.question_number=0

        # assigns ques to the display_question function to update later.

        self.display_question()

        # option_selected holds an integer value which is used for
        # selected option in a question.
        self.option_selected=IntVar()

        # displaying radio button for the current question and used to
        # display options for the current question
        self.options=self.radio_my_buttons()

        # display options for the current question
        self.display_options()

        # displays the button for next and exit.
        self.my_buttons()

        # no of questions
        self.data_length=len(self.question)

        # keep a counter of correct answers
        self.correct=0
        



    def result_display(self):

        wrong_count = self.data_length - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        score = int(self.correct / self.data_length * 100)
        result = f"Score: {score}%"

        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


    def answer_check(self, question_number):

        if self.option_selected.get() == self.answer[question_number]:
            return True


    def button_next(self):


        if self.option_selected.get() >=1 and self.option_selected.get() <= 4:

            if self.answer_check(self.question_number):
                
                self.correct += 1

            self.question_number += 1

            if self.question_number==self.data_length:
                
                self.result_display()
                
                self.mainWindow.destroy()
            else:
                self.display_question()
                self.display_options()


    def my_buttons(self):

        next_button = Button(self.mainWindow, text="Next",command=self.button_next,
        width=13,bg="blue",fg="white",font=("ariel",16,"bold"))

        
        next_button.place(x=350,y=350)

        
        quit_button = Button(self.mainWindow, text="Quit", command=self.mainWindow.destroy,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))

        
        quit_button.place(x=630,y=335)


    def display_options(self):
        val=0

        self.option_selected.set(0)

        for option in self.option[self.question_number]:
            self.options[val]['text']=option
            val+=1


    def display_question(self):


        question_number = Label(self.mainWindow, bg= "black",fg="white" ,text=self.question[self.question_number], width=52,
        font=( 'ariel' ,12, 'bold' ), anchor= 'w' )

        question_number.place(x=207, y=100)



    def radio_my_buttons(self):

        # initialize the list with an empty list of options
        question_list = []

        y_pos = 180

        while len(question_list) < 4:
            
            common_bg = '#000000'  # pure black
            common_fg = '#ffffff'  # pure white

            # setting the radio button properties
            radio_btn = Radiobutton(self.mainWindow,fg=common_fg, bg=common_bg,
                            activebackground=common_bg, activeforeground=common_fg, selectcolor=common_bg
                            ,text=" ",variable=self.option_selected,
            value = len(question_list)+1,font = ("ariel",14))
            

            question_list.append(radio_btn)
            
            radio_btn.place(x = 360, y = y_pos)
            
            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio my_buttons
        return question_list


def button_next_command():
    if option_selected.get() >=1 and option_selected.get() <= 5:

        choiceWindow.destroy()

        filename = "data" + str(option_selected.get()) + ".json"

        # get the data from the json file
        with open(filename) as f:
            data = json.load(f)

        # set the question, options, and answer
        question = (data['question'])
        options = (data['options'])
        answer = (data['answer'])


        # Create a GUI Window
        mainWindow = Tk()

        # Add image file
        bg = PhotoImage(file = "Background.png")
        
        # Show image using label
        label1 = Label(mainWindow, image = bg)
        label1.place(x = 0, y = 0)

        # set the size of the GUI Window
        mainWindow.geometry("800x450")

        #setting title
        mainWindow.title("QUESTIONAIRE APP")

        mainWindow.resizable(width=False, height=False)
        
        # create an object of the Questionarre Class.
        quiz = Questionarre(mainWindow,question,options,answer)

        # Start the GUI
        mainWindow.mainloop()



if __name__ == "__main__":
    main()





# END OF THE PROGRAM
