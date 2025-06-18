from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont


class NameGenerator:
    def __init__(self) -> None:

        self.root = Tk()

        title_font = tkFont.Font(family="Arial", size=20)
        subtitle_font = tkFont.Font(family="Arial", size=10)
        self.label_title = Label(
            self.root,
            text="Hero name generator",
            font=title_font,
            fg="white",
            bg="purple",
        )

        self.label_adjective = Label(
            self.root,
            text="Choose an adjective...",
            font=subtitle_font,
        )

        adjectives = ["Happy", "Awesome", "Outgoing", "Funky"]
        self.radio_var = IntVar()
        self.radio_var.set(99)
        for i in range(4):
            radio = Radiobutton(
                self.root,
                text=adjectives[i],
                variable=self.radio_var,
                value=i,
                command=self.radio_call,
            )
            radio.grid(row= 2 +i, column= 0)

        self.label_color = Label(
            self.root,
            text="Enter a color",
            font=subtitle_font,
        )

        self.label_animal = Label(
            self.root,
            text="Pick an animal",
            font=subtitle_font,
        )

        self.Gobutton = Button(
            self.root,
            text="Go!",
            font=subtitle_font,
        )

        self.label_name = Label(
            self.root,
            text="Your name will appear here!",
            font=subtitle_font,
        )
        self.label_title.grid(
            row=1,
            column=0,
            ipadx=30,
            ipady=10,
        )
        self.label_adjective.grid(
            row=6,
            column=0,
        )

        self.label_color.grid(
            row=7,
            column=0,
        )

        self.label_animal.grid(
            row=8,
            column=0,
        )

        self.Gobutton.grid(
            row=9,
            column=0,
        )

        self.label_name.grid(
            row=10,
            column=0,
        )

    def run(self):
        self.root.mainloop()

    def generate(self):
        name = name
        self.label_name.configure(text=name)

    def radio_call(self):
        if self.radio_var.get() == 0:
            status = "Happy"
        if self.radio_var.get() == 1:
            status = "Awesome"
        if self.radio_var.get() == 2:
            status = "Outgoing"
        if self.radio_var.get() == 3:
            status = "Funky"


if __name__ == "__main__":
    app = NameGenerator()
    app.run()
