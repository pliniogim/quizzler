from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
BACKGROUND_COLOR = "medium aquamarine"


class QuizzlerUi:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(bg=BACKGROUND_COLOR)
        self.window.config(width=400, height=600, padx=10, pady=10)

        self.canvas = Canvas()
        self.canvas.config(width=400, height=600)
        self.text_question = (
            self.canvas.create_text(200, 120, text="Questions come here...", font=("Arial", 18, "bold")))

        self.label_emp = Label(text="Score: 0/10", bg=BACKGROUND_COLOR, font=("Arial", 12, "bold"))

        self.true_img = PhotoImage(file="images/true.png")
        # or true_img
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=ans_true, padx=5, pady=20)
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=ans_false, padx=5, pady=20)

        self.canvas.grid(row=0, column=0, columnspan=2, sticky="EW", pady=20)
        self.label_emp.grid(row=1, column=0, columnspan=2, pady=20)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question():
        self.quiz.

def ans_true():
    pass

def ans_false():
    pass


