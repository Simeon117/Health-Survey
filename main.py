from tkinter import *
names = []

class Quiz:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="DarkOliveGreen1"#

        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        #

        self.quiz_frame.grid()#
               
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="Health Survey", font=("Arial","18","bold"),bg=background_color)
        self.heading_label.grid(row=0, padx=20) 
        self.var1=IntVar() #holds value of radio buttons
        
        #label for username
        self.user_label=Label(self.quiz_frame, text="Enter your name below to get started", font=("Helvetica","16"),bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20) 
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Exit", font=("Arial", "13", "bold"), bg="light salmon", command=self.name_collection)
        self.continue_button.grid(row=3,  padx=20, pady=20)        
        
        #image
        #logo = PhotoImage(file="road.gif")
        #self.logo = Label(self.quiz_frame, image=logo)  
        #self.logo.grid(row=4,padx=20, pady=20) 
       

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #
        self.continue_button.destroy()
        self.entry_box.destroy() #
      
           

if __name__ == "__main__":
    root = Tk()
    root.title("Health Survey") 

    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear
 
