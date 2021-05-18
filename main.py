from tkinter import *
names = []

class QuizStarter:
    def __init__(self, parent):
      background_color="OldLace"

      #frame set up
      self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
      #
      self.quiz_frame.grid()
    
      #
      self.heading_label=Label(self.quiz_frame, text="Health Survey", font=("Comfortaa","18","bold"), bg=background_color)
      #
      self.quiz_frame.grid(row=0, padx=20)

      #
      self.var1=IntVar()

      #
      self.user_label=Label(self.quiz_frame, text="Enter your name below to get started", font=("Comfortaa", "16"), bg=background_color)
      self.user_label.grid(row=1, padx=20, pady=20)

      #
      self.entry_box=Entry(self.quiz_frame)
      self.entry_box.grid(row=1, padx=20, pady=20)

      #
      self.continue_button=Button(self.quiz_frame, text="Continue", font=("Comfortaa", "13", "bold"), bg="light green", command=self.name_collection)
      self.continue_button.grid(row=2, padx=20, pady=20)


      def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        self.quiz_frame.destroy()


if __name__ == "__main__":
  root = Tk()
  root.title("Health Survey")
  quiz_instance = QuizStarter(root)
  root.mainloop()