import random
from tkinter import Tk, messagebox, Label, Button, Text


class TypingTest(Tk):

    def __init__(self):
        super().__init__()
        self.count = 60
        self.WORDS_LIST = [
            "An ever-growing number of complex and rigid rules plus hard-to-cope-with regulations are now being "
            "legislated "
            "from state to state. Key federal regulations were formulated by the FDA, FTC, and the CPSC. Each of these "
            "federal agencies serves a specific mission.",
            "Laws sponsored by the Office of the Fair Debt Collection Practices prevent an agency from purposefully "
            "harassing "
            "clients in serious debt. The Fair Packaging and Labeling Act makes certain that protection from "
            "misleading "
            "packaging of goods is guaranteed to each buyer of goods carried in small shops as well as in large "
            "supermarkets.",

            "Two common terms used to describe a salesperson are 'Farmer' and 'Hunter'. The reality is that most "
            "professional "
            "salespeople have a little of both. A hunter is often associated with aggressive personalities who use "
            "aggressive "
            "sales technique.",
            "One study examining 30 subjects, of varying different styles and expertise, has found minimal difference "
            "in "
            "typing speed between touch typists and self-taught hybrid typists. According to the study, 'The number of "
            "fingers does not determine typing speed... People using self-taught typing strategies were found to be "
            "as fast "
            "as trained typists... instead of the number of fingers, there are other factors that predict typing speed.",
            "Closed captions were created for deaf or hard of hearing individuals to assist in comprehension. They "
            "can also "
            "be used as a tool by those learning to read, learning to speak a non-native language, or in an "
            "environment where "
            "the audio is difficult to hear or is intentionally muted.",
            "A freelancer or freelance worker, is a term commonly used for a person who is self-employed and is not "
            "necessarily committed to a particular employer long-term. Freelance workers are sometimes represented by "
            "a "
            "company or a temporary agency that resells freelance labor to clients; others work independently or use "
            "professional associations or websites to get work. "
        ]
        self.ERROR = 0
        self.random_sentence = ""
        self.net_rate = 0
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.rand_typ()
        self.widgets()

    def rand_typ(self):
        """Creates a random sentence and a random_sentence_list from the word list"""
        self.random_sentence = random.choice(seq=self.WORDS_LIST)
        self.random_sentence_list = [each_sentence for each_sentence in self.random_sentence.split(' ')]
        print(self.random_sentence_list)
        return self.random_sentence

    def user_answer_to_list(self, answer):
        """Takes the users input as answer and calculates the word_per_minute"""
        self.user_answer_list = [_ for _ in answer.split(' ')]
        self.calculate_wpm()
        return self.user_answer_list

    def calculate_wpm(self):
        """Calculates the word per minute."""
        self.net_rate = 0
        self.ERROR = 0
        try:
            for each in range(len(self.user_answer_list)):
                if self.user_answer_list[each] == self.random_sentence_list[each]:
                    pass
                else:
                    self.ERROR += 1
                    # for index, user_letter in enumerate(self.user_answer_list[each]):
                    #     if user_letter != self.random_sentence_list[each][index]:
                    #
                    #         print(user_letter)

        except IndexError as e:
            print(e)

        else:
            print(self.ERROR)
            words_per_minute = len(self.user_answer_list)

            print("{} wpm".format(words_per_minute))
            total_error = round((self.ERROR / (len(self.user_answer_list))) * 100)
            accuracy = 100 - total_error
            print(f"Accuracy {accuracy}")
            self.net_rate = (accuracy * words_per_minute) / 100
            return self.net_rate

    def widgets(self):
        """Creates all the required widgets to show on the screen."""
        # Title Name
        self.title("Type Testing")

        # Screen Size
        self.geometry(f"{self.width}x{self.height}")

        # Screen Background Color
        self.config(bg='lightblue')

        # Creates a label "Typing Test!"
        label = Label(master=self, text="Typing Test!", font="Helvetica 30 bold", bg='lightblue')
        label.pack()

        # Creates a count label

        self.timer = Label(text="", master=self, font="times 20 bold", fg="red", bg="lightblue")
        self.timer.pack(pady=15)

        # Creates a label of random_sentence

        text = Label(self, width=400, height=10, text=self.random_sentence, fg="black", font='times 25',
                     wraplength=1500)
        text.pack(pady="50")

        # Creates a text-box for user to input
        self.entry = Text(width=100, height=5, font='times 25')
        self.entry['state'] = 'disabled'
        self.entry.pack()

        # Creates a button to start the counter
        self.start = Button(master=self, width=20, font='times 14', text="Start", command=self.start_timer)
        self.start.place(x=760, y=820)

        self.reset = Button(master=self, width=20, font='times 14', text="Reset", command=self.reset_timer)
        self.reset.place(x=1000, y=820)

    def start_timer(self):
        """Starts the timer and enables the text field to type"""
        self.count = 60
        self.timer.config(text=self.count)
        self.start['state'] = 'disabled'
        self.entry['state'] = 'normal'
        self.entry.focus()
        self.update_timer()

    def update_timer(self):
        """Calculates the words per minute after a min."""
        if self.count != 0:
            self.after(1000, func=self.update_timer)
            self.count -= 1
            self.timer.config(text=self.count)
        else:
            self.entry['state'] = 'disabled'
            self.user_answer_to_list(self.entry.get("1.0", 'end-1c'))
            print(self.net_rate)

            messagebox.showinfo(title="Words per minute", message=f"Your Test Score is : {self.net_rate}")


    def reset_timer(self):
        self.entry.delete("1.0", "end")
        self.entry['state'] = 'disabled'
        self.start['state'] = 'normal'
        self.count = 0

        self.timer.config(text="")


if __name__ == "__main__":
    tt = TypingTest()
    tt.mainloop()