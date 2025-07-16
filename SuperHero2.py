from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont


class NameGenerator:
    def __init__(self) -> None:

        self.root = Tk()
        self.root.configure(bg="white")
        self.light = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\Programming\gui\SuperHero\light.png"
        )
        self.dark = PhotoImage(
            file=r"N:\13PRG\st21146-Louis\Programming\gui\SuperHero\dark.png"
        )

        self.switch_value = True
        title_font = tkFont.Font(family="Arial", size=25, weight="bold")
        subtitle_font = tkFont.Font(family="Arial", size=15, weight="bold")
        text_font = tkFont.Font(family="Arial", size=10, weight="bold")
        self.label_title = Label(
            self.root,
            text="Hero name generator",
            font=title_font,
            fg="white",
            bg="purple",
        )
        self.DarkToggle = Button(
            self.root,
            image=self.light,
            bd=0,
            bg="white",
            activebackground="white",
            command=self.darkmode,
        )

        self.label_adjective = Label(
            self.root,
            text="Choose an adjective...",
            font=subtitle_font,
            bg="white",
        )

        adjectives = ["Happy", "Awesome", "Outgoing", "Funky"]
        self.radio_var = IntVar()
        self.radio_var.set(99)
        self.radio_buttons = []
        for i in range(4):
            radio = Radiobutton(
                self.root,
                text=adjectives[i],
                font=text_font,
                variable=self.radio_var,
                value=i,
                command=self.radio_call,
                bg="white",
            )
            radio.grid(row=4 + i, column=0)
            self.radio_buttons.append(radio)

        self.label_color = Label(
            self.root, text="Enter a color", font=subtitle_font, bg="white"
        )
        self.color_entry = Entry(
            self.root,
        )

        self.label_animal = Label(
            self.root, text="Pick an animal", font=subtitle_font, bg="white"
        )
        self.animals = [
            "Dog",
            "Cat",
        ]
        chosen_animal = StringVar()
        chosen_animal.set("")
        self.my_combobox = ttk.Combobox(
            self.root, textvariable=chosen_animal, state="readonly"
        )
        self.my_combobox["values"] = self.animals

        self.Gobutton = Button(
            self.root, text="Go!", font=subtitle_font, command=self.generate
        )

        self.label_name = Label(
            self.root,
            text="Your name will appear here!",
            font=subtitle_font,
            bg="white",
        )
        self.label_title.grid(
            row=1,
            column=0,
            ipadx=30,
            ipady=10,
        )
        self.DarkToggle.grid(
            row=2,
            column=0,
        )

        self.label_adjective.grid(
            row=3,
            column=0,
        )

        self.label_color.grid(
            row=9,
            column=0,
        )
        self.color_entry.grid(
            row=10,
            column=0,
        )

        self.label_animal.grid(
            row=11,
            column=0,
        )
        self.my_combobox.grid(
            row=12,
            column=0,
        )

        self.Gobutton.grid(
            row=13,
            column=0,
        )

        self.label_name.grid(
            row=14,
            column=0,
        )

    def darkmode(self):
        if self.switch_value == True:
            self.DarkToggle.config(
                image=self.dark, bg="#26242f", activebackground="#26242f"
            )
            self.root.configure(bg="#26242f")
            self.label_title.config(fg="white", bg="#131313")
            self.label_adjective.config(fg="white", bg="#26242f")
            for radio in self.radio_buttons:
                radio.config(fg="white", bg="#26242f")
            self.label_color.config(fg="white", bg="#26242f")
            self.label_animal.config(fg="white", bg="#26242f")
            self.Gobutton.config(fg="white", bg="#26242f")
            self.label_name.config(fg="white", bg="#26242f")
            self.switch_value = False

        else:
            self.DarkToggle.config(
                image=self.light, bg="white", activebackground="white"
            )
            self.root.configure(bg="white")
            self.label_title.config(fg="white", bg="purple")
            self.label_adjective.config(fg="black", bg="white")
            for radio in self.radio_buttons:
                radio.config(fg="black", bg="white")
            self.label_color.config(fg="black", bg="white")
            self.label_animal.config(fg="black", bg="white")
            self.Gobutton.config(fg="black", bg="white")
            self.label_name.config(fg="black", bg="white")
            self.switch_value = True

    def run(self):
        self.root.mainloop()

    def generate(self):
        color = self.color_entry.get().title().strip()
        name = f"You are the {status} {color} {self.my_combobox.get()}!"
        self.label_name.configure(text=name, fg="purple")

    def radio_call(self):
        global status
        status = ""
        if self.radio_var.get() == 0:
            status = "Happy"
        if self.radio_var.get() == 1:
            status = "Awesome"
        if self.radio_var.get() == 2:
            status = "Outgoing"
        if self.radio_var.get() == 3:
            status = "Funky"
