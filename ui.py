import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
BACKGROUND_COLOR = "medium aquamarine"


class QuizzlerUi:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.quiz.score = 0
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(bg=BACKGROUND_COLOR)
        self.window.config(width=400, height=500, padx=10, pady=10)

        self.canvas = Canvas()
        self.canvas.config(width=400, height=400)
        self.text_question = (
            self.canvas.create_text(200, 120, width=340, text="Questions come here...", font=("Arial", 18, "bold")))

        self.label_emp = Label(text="Score: 0/10", bg=BACKGROUND_COLOR, font=("Arial", 12, "bold"))

        self.true_img = PhotoImage(file="images/true.png")
        # or true_img
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.ans_true, padx=5, pady=20)
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.ans_false, padx=5, pady=20)

        self.canvas.grid(row=0, column=0, columnspan=2, sticky="EW", pady=20)
        self.label_emp.grid(row=1, column=0, columnspan=2, pady=20)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.text_question, text=self.quiz.next_question())
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.text_question, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def ans_true(self):
        answer = self.quiz.check_answer("True")
        if answer:
            self.quiz.score += 1
            self.give_feedback(True)
            self.label_emp.config(text="Score: " + str(self.quiz.score) + "/10")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)

    def ans_false(self):
        answer = self.quiz.check_answer("False")
        if answer:
            self.quiz.score += 1
            self.give_feedback(True)
            self.label_emp.config(text="Score: " + str(self.quiz.score) + "/10")
            self.window.after(1000, self.get_next_question)

        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
