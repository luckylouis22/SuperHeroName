from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont


class NameGenerator:
    def __init__(self) -> None:

        self.root = Tk()

        title_font = tkFont.Font(family="Arial", size=25,weight= "bold")
        subtitle_font = tkFont.Font(family="Arial", size=15,weight= "bold")
        text_font = tkFont.Font(family="Arial", size=10, weight="bold" )
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
                font=text_font,
                variable=self.radio_var,
                value=i,
                command=self.radio_call,
            )
            radio.grid(row= 3 +i, column= 0)

        self.label_color = Label(
            self.root,
            text="Enter a color",
            font=subtitle_font,
        )
        self.color_entry = Entry(
            self.root,  
        )

        self.label_animal = Label(
            self.root,
            text="Pick an animal",
            font=subtitle_font,
        )
        self.animals = ["Dog", "Cat",]
        chosen_animal = StringVar()
        chosen_animal.set("")
        self.my_combobox = ttk.Combobox(self.root, textvariable=chosen_animal, state="readonly")
        self.my_combobox["values"] = self.animals

        self.Gobutton = Button(
            self.root,
            text="Go!",
            font=subtitle_font,
            command= self.generate
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
            row=2,
            column=0,
        )

        self.label_color.grid(
            row=8,
            column=0,
        )
        self.color_entry.grid(
            row= 9, 
            column=0,
        )

        self.label_animal.grid(
            row=10,
            column=0,
        )
        self.my_combobox.grid(
            row=11,
            column=0,
        )

        self.Gobutton.grid(
            row=12,
            column=0,
        )

        self.label_name.grid(
            row=13,
            column=0,
        )

    def run(self):
        self.root.mainloop()

    def generate(self):
        color  = self.color_entry.get().title().strip()
        name = f"You are the {status} {color} {self.my_combobox.get()}!" 
        self.label_name.configure(text=name, fg = "purple")

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


if __name__ == "__main__":
    app = NameGenerator()
    app.run()
