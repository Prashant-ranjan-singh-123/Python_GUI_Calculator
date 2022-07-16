from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as mess
import webbrowser
from PIL import ImageTk, Image
import os
import pyperclip


class AskingWhatToDo:
    def __init__(self):
        self.run_next_program = False
        self.programmer_description_string = '''(#)This Program is made on July 16, 2022
by Prashant Ranjan Singh.


(#) This Program is basically an offline
Calculator


(#) Linkedin Profile of mine :-'''
        self.working_of_program_explain_str = '''--> It is an basic standard calculator which are used in daily life.

--> It follow bodmas rule for calculating math problem. 

--> Valid Inputs : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                            '+', '-', '*', '/', '.', '^', '(', ')', '%']
--> Shortcuts are :-
1) ctrl+s / ctrl+S --> Saving all the calculation after running this app.
2) ctrl+h / ctrl+H --> For Opening Help Menu
3) ESC --> Clear Button Shortcut
4) Backspace --> Removing last input
5) Enter --> For calculating Expression.
6) alt+f4 --> Exiting application.
7) ctrl+c / ctrl+C --> For copy result into clipboard'''
        background = 'white'

        # Screen
        self.screen = Tk()
        self.screen.geometry('600x620')
        self.screen.minsize(600, 620)
        self.screen.maxsize(600, 620)
        self.screen.title('Calculator By Prashant Ranjan Singh')
        self.screen.config(bg=background, padx=50, pady=50)
        self.screen.resizable(False, False)

        # image
        self.password_image = ImageTk.PhotoImage(Image.open("Program Images/Mine_photo.jpg"))
        self.image = Label(width=250, height=250, image=self.password_image, borderwidth=0)

        # Label
        self.text = Label()
        self.about_programmer = Label(text='About Programmer', font=('LatinModernRomanDunhill', 12, 'bold'),
                                      background=background)
        self.text.configure(text=self.programmer_description_string, bg='white', justify=LEFT)
        self.link = Label(text="www.linkedin.com", fg="blue", cursor="hand2", bg=background)
        self.link.bind("<Button-1>", lambda e: self.callback("www.linkedin.com/in/prashant-ranjan-singh-b9b6b9217"))
        self.working_heading = Label(text='Working of Program', font=('LatinModernRomanDunhill', 12, 'bold'),
                                     bg=background)
        self.working_of_program_explain = Label(text=self.working_of_program_explain_str, bg='white', justify=LEFT)

        # Create a Label to display the link
        self.image.grid(column=0, row=0)
        self.about_programmer.grid(column=1, row=0, sticky=NE, padx=70)
        self.text.grid(column=1, row=0, sticky=NW, pady=50, padx=10)
        self.link.grid(column=1, row=0, sticky=SW, padx=35, pady=30)
        self.working_heading.grid(column=0, row=1, padx=50, columnspan=2, pady=5)
        self.working_of_program_explain.grid(column=0, row=2, columnspan=3, sticky=W)
        self.screen.mainloop()

    @staticmethod
    def callback(url):
        webbrowser.open_new_tab(url)


class Calculator:

    def on_key_press(self, key):
        input_is = key.char
        if len(input_is) == 0:
            pass
        else:
            input_is = ord(input_is)
            if input_is == 13:
                self.calculate_button_function()
            if input_is == 27:
                self.clr_calculation_area_entry()
            if input_is == 9:
                self.calculation_area_entry.focus()
            if 45 <= input_is <= 57 or 40 <= input_is <= 43 or input_is == 37 or input_is == 94 \
                    or input_is == 13 or input_is == 27 or input_is == 8 or input_is == 9:
                pass
            else:
                self.clr_last_entry_from_calculation_area_entry(is_remove_label=False)

    def copy_result(self):
        r = None
        for ir, (key, value) in enumerate(self.calculation.items()):
            if ir == len(self.calculation.items()) - 1:
                r = str(value)
        pyperclip.copy(r)

    def about_programmer_command(self):
        self.window.destroy()
        AskingWhatToDo()
        Calculator()

    def append_item_to_calculation_area_entry(self, symbol):
        self.calculation_area_entry.insert(END, symbol)

    def clr_calculation_area_entry(self, is_remove_label=True):
        self.calculation_area_entry.delete(0, END)
        if is_remove_label:
            self.previous_solution_label.config(text='')

    def clr_last_entry_from_calculation_area_entry(self, is_remove_label=True):
        cal_area_value = self.calculation_area_entry.get()
        cal_area_value = cal_area_value[:len(cal_area_value) - 1]
        if is_remove_label:
            self.clr_calculation_area_entry()
        else:
            self.clr_calculation_area_entry(is_remove_label=False)
        self.calculation_area_entry.insert(0, cal_area_value)

    def calculate_button_function(self):
        right_input = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                       '+', '-', '*', '/', '.', '√', '^', '(', ')', '%']
        cal_area_value = self.calculation_area_entry.get()
        for words in cal_area_value:
            if words not in right_input:
                mess.showerror(title='Wrong Input', message='Illegal expression are passed for calculation, please '
                                                            'check expression once.')
                return

        try:
            if '^' in cal_area_value:
                ask = mess.askyesno(title='Alert', message='Program found that power operator is used. \n\n'
                                    ''
                                    'Note:-\n'
                                    'If you are passing big power (Like: 12345^54321) then this program will freeze.\n'
                                    'Are you sure you want to calculate.')
                if not ask:
                    return
            for word in cal_area_value:
                if word in right_input[10:20]:
                    if cal_area_value.find('^'):
                        cal_area_value = cal_area_value.replace('^', '**')
                    if cal_area_value.find('%'):
                        cal_area_value = cal_area_value.replace('%', '*.01')

                    result = eval(cal_area_value)

                    if cal_area_value.find('**'):
                        cal_area_value = cal_area_value.replace('**', '^')
                    if cal_area_value.find('*.01'):
                        cal_area_value = cal_area_value.replace('*.01', '%')
                    self.calculation_area_entry.delete(0, END)
                    self.calculation_area_entry.insert(0, result)
                    if not cal_area_value == result:
                        self.calculation[cal_area_value] = result
                        self.previous_solution_label.config(text=cal_area_value)
        except:
            mess.showerror(title='Wrong Input', message='Illegal inputs are passed for calculation.')

    def export_calculation_button_function(self):
        current_dir = os.getcwd()
        if os.access(current_dir, os.F_OK) and os.access(current_dir, os.R_OK) and os.access(current_dir, os.W_OK):
            if self.calculation.items():
                file = filedialog.asksaveasfilename(
                    filetypes=[("txt file", ".txt")],
                    defaultextension=".txt")
                if file.__class__.__name__ != 'tuple':
                    if file != '':
                        with open(file, 'w') as f:
                            for index, (key, value) in enumerate(self.calculation.items()):
                                f.write(f'{index + 1}) {key} = {value}\n')
                        mess.showinfo(title='Success', message='Data Exported Successfully.')
            else:
                mess.showerror(
                    title='Null Calculations',
                    message='There isn\'t any results to store')

        else:
            mess.showerror(title='Permission Issue', message='You won\'t have reading Reading/Writing Permission.')

    def __init__(self):

        self.calculation = {}
        self.cursor_on_button = 'spraycan'

        self.window = Tk()
        self.window.configure(cursor='arrow')
        self.window.geometry("326x503")
        self.window.title('Prashant\'s Calculator')
        self.window.configure(bg="#1f1f1f")
        canvas = Canvas(
            self.window,
            bg="#1f1f1f",
            height=503,
            width=326,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        img1 = PhotoImage(file=f"Program Images/img1.png")
        self.seven_button = Button(
            cursor=self.cursor_on_button,
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('7'),
            relief="flat")

        self.seven_button.place(
            x=10, y=276,
            width=72,
            height=49)

        img2 = PhotoImage(file=f"Program Images/img2.png")
        self.four_button = Button(
            cursor=self.cursor_on_button,
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('4'),
            relief="flat")

        self.four_button.place(
            x=10, y=332,
            width=72,
            height=49)

        img3 = PhotoImage(file=f"Program Images/img3.png")
        self.one_button = Button(
            cursor=self.cursor_on_button,
            image=img3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('1'),
            relief="flat")

        self.one_button.place(
            x=10, y=387,
            width=72,
            height=49)

        img7 = PhotoImage(file=f"Program Images/img7.png")
        self.eight_button = Button(
            cursor=self.cursor_on_button,
            image=img7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('8'),
            relief="flat")

        self.eight_button.place(
            x=88, y=276,
            width=72,
            height=49)

        img8 = PhotoImage(file=f"Program Images/img8.png")
        self.five_button = Button(
            cursor=self.cursor_on_button,
            image=img8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('5'),
            relief="flat")

        self.five_button.place(
            x=88, y=332,
            width=72,
            height=49)

        img9 = PhotoImage(file=f"Program Images/img9.png")
        self.two_button = Button(
            cursor=self.cursor_on_button,
            image=img9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('2'),
            relief="flat")

        self.two_button.place(
            x=88, y=387,
            width=72,
            height=49)

        img10 = PhotoImage(file=f"Program Images/img10.png")
        self.zero_button = Button(
            cursor=self.cursor_on_button,
            image=img10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('0'),
            relief="flat")

        self.zero_button.place(
            x=88, y=442,
            width=72,
            height=49)

        img4 = PhotoImage(file=f"Program Images/img4.png")
        self.percent_button = Button(
            cursor=self.cursor_on_button,
            image=img4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('%'),
            relief="flat")

        self.percent_button.place(
            x=10, y=442,
            width=72,
            height=49)

        img0 = PhotoImage(file=f"Program Images/img0.png")
        self.right_bracket_button = Button(
            cursor=self.cursor_on_button,
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('('),
            relief="flat", )
        self.right_bracket_button.place(
            x=10, y=221,
            # x=10, y=166,
            width=72,
            height=49)

        img11 = PhotoImage(file=f"Program Images/img11.png")
        self.left_bracket_button = Button(
            cursor=self.cursor_on_button,
            image=img11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry(')'),
            relief="flat")

        self.left_bracket_button.place(
            x=88, y=221,
            width=72,
            height=49)

        img6 = PhotoImage(file=f"Program Images/img6.png")
        self.clear_button = Button(
            cursor=self.cursor_on_button,
            image=img6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.clr_calculation_area_entry(),
            relief="flat")

        self.clear_button.place(
            x=10, y=166,
            #     x=10, y=221,
            width=150,
            height=49)

        img12 = PhotoImage(file=f"Program Images/img12.png")
        self.backspace_button = Button(
            cursor=self.cursor_on_button,
            image=img12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.clr_last_entry_from_calculation_area_entry(),
            relief="flat")

        self.backspace_button.place(
            x=166, y=167,
            width=150,
            height=49)

        img17 = PhotoImage(file=f"Program Images/img17.png")
        self.power_button = Button(
            cursor=self.cursor_on_button,
            image=img17,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('^'),
            relief="flat")

        self.power_button.place(
            x=166, y=221,
            width=72,
            height=49)

        img13 = PhotoImage(file=f"Program Images/img13.png")
        self.nine_button = Button(
            cursor=self.cursor_on_button,
            image=img13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('9'),
            relief="flat")

        self.nine_button.place(
            x=166, y=276,
            width=72,
            height=49)

        img14 = PhotoImage(file=f"Program Images/img14.png")
        self.six_button = Button(
            cursor=self.cursor_on_button,
            image=img14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('6'),
            relief="flat")

        self.six_button.place(
            x=166, y=332,
            width=72,
            height=49)

        img15 = PhotoImage(file=f"Program Images/img15.png")
        self.three_button = Button(
            cursor=self.cursor_on_button,
            image=img15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('3'),
            relief="flat")

        self.three_button.place(
            x=166, y=387,
            width=72,
            height=49)

        img16 = PhotoImage(file=f"Program Images/img16.png")
        self.dot_button = Button(
            cursor=self.cursor_on_button,
            image=img16,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('.'),
            relief="flat")

        self.dot_button.place(
            x=166, y=442,
            width=72,
            height=49)

        img18 = PhotoImage(file=f"Program Images/img18.png")
        self.divide_button = Button(
            cursor=self.cursor_on_button,
            image=img18,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('/'),
            relief="flat")

        self.divide_button.place(
            x=244, y=221,
            width=72,
            height=49)

        img19 = PhotoImage(file=f"Program Images/img19.png")
        self.multiply_button = Button(
            cursor=self.cursor_on_button,
            image=img19,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('*'),
            relief="flat")

        self.multiply_button.place(
            x=244, y=276,
            width=72,
            height=49)

        img20 = PhotoImage(file=f"Program Images/img20.png")
        self.subtract_button = Button(
            cursor=self.cursor_on_button,
            image=img20,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('-'),
            relief="flat")

        self.subtract_button.place(
            x=244, y=332,
            width=72,
            height=49)

        img21 = PhotoImage(file=f"Program Images/img21.png")
        self.addition_button = Button(
            cursor=self.cursor_on_button,
            image=img21,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_item_to_calculation_area_entry('+'),
            relief="flat")

        self.addition_button.place(
            x=244, y=387,
            width=72,
            height=49)

        img22 = PhotoImage(file=f"Program Images/img22.png")
        self.equal_to_button = Button(
            cursor=self.cursor_on_button,
            image=img22,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.calculate_button_function(),
            relief="flat")

        self.equal_to_button.place(
            x=244, y=442,
            width=72,
            height=49)

        img23 = PhotoImage(file=f"Program Images/img23.png")
        self.export_cal_button = Button(
            cursor=self.cursor_on_button,
            image=img23,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.export_calculation_button_function(),
            relief="flat",
            background='#1f1f1f',
            activebackground='#1f1f1f')

        self.export_cal_button.place(
            x=240, y=19,
            width=71,
            height=47)

        entry0_img = PhotoImage(file=f"Program Images/img_textBox0.png")
        canvas.create_image(
            164.0, 119.0,
            image=entry0_img)

        self.calculation_area_entry = Entry(
            bd=0,
            bg="#1f1f1f",
            highlightthickness=0,
            font=('arial', 15, 'bold'),
            foreground='white',
            justify='right')
        self.calculation_area_entry.place(
            x=11, y=86,
            width=306,
            height=64)
        self.calculation_area_entry.focus()

        self.previous_solution_label = Label(
            bg="#1f1f1f",
            foreground='white',
            font=('InriaSerif-Regular', 6))

        self.previous_solution_label.place(x=11, y=82)

        canvas.create_text(
            90.0, 42.5,
            text="Prashant's \nCalculator",
            fill="#ffffff",
            font=("InriaSerif-Regular", int(18.0)))

        img24 = PhotoImage(file=f"Program Images/img24.png")
        self.about_programmer = Button(
            cursor=self.cursor_on_button,
            image=img24,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.about_programmer_command(),
            relief="flat",
            background='#1f1f1f',
            activebackground='#1f1f1f')

        self.about_programmer.place(
            x=160, y=19,
            width=71,
            height=47)
        self.window.bind('<Key>', lambda i: self.on_key_press(i))
        self.window.bind('<Control-s>', lambda a: self.export_calculation_button_function())
        self.window.bind('<Control-S>', lambda a: self.export_calculation_button_function())
        self.window.bind('<Control-h>', lambda a: self.about_programmer_command())
        self.window.bind('<Control-H>', lambda a: self.about_programmer_command())
        self.window.bind('<Control-c>', lambda a: self.copy_result())
        self.window.bind('<Control-C>', lambda a: self.copy_result())
        self.window.resizable(False, False)
        self.window.mainloop()


class Errors:
    def file_missing(cls,
                     url='https://github.com/Prashant-ranjan-singh-123/MyAllProgramsInOneRepo/tree/main/'
                         '4)%20Python%20Language/GUI%20Program/Library%20Management',
                     show_name_of_url='www.github.com'):
        def callback(url):
            webbrowser.open_new_tab(url)

        root = Tk()
        cls.background = 'white'
        root.geometry('500x310')
        root.resizable(False, False)
        root.title('Calculator by Prashant Singh')
        root.config(background=cls.background, borderwidth=30)

        def exit_command():
            nonlocal root
            root.destroy()
            is_rerun = False

        # Heading Label
        cls.L1 = Label(root, text='Prashant\'s Calculator', font='LatinModernRomanDunhill 20 bold',
                       background=cls.background)
        cls.L1.pack(anchor='center')

        # Label
        cls.error = Label(root, text='Error', foreground='red', font='arial 30 bold', justify=CENTER,
                          background=cls.background)
        cls.error.pack(anchor='center', pady=20)

        cls.what_to_do = Label(root, text=f'You wont have essential component\'s for proper \n'
                                          f'execution of program please download it from \n'
                                          f'official github repository from below link :-',
                               font=('arial', 12, 'bold'), justify=CENTER, bg=cls.background)
        cls.what_to_do.pack()

        cls.link = Label(text=show_name_of_url, fg="blue", cursor="hand2", bg=cls.background,
                         font=('arial', 12, 'bold'))
        cls.link.bind("<Button-1>", lambda e: callback(url))
        cls.link.pack(anchor='center')

        # Button
        exit_button = Button(text='Previous Menu', bg='#ff4d4d', padx=40, borderwidth=2, highlightbackground='black',
                             activebackground='#ff0000', command=exit_command)
        exit_button.place(x=480, y=300)
        root.mainloop()


if __name__ == '__main__':
    # Calculator()
    all_file_there = True
    if os.path.exists('Program Images'):
        if not os.path.exists('Program Images/img_textBox0.png'):
            all_file_there = False
        for i in range(25):
            if not os.path.exists(f'Program Images/img{i}.png'):
                all_file_there = False
    else:
        all_file_there = False
    if not os.path.exists('Program Images/Mine_photo.jpg'):
        all_file_there = False

    if all_file_there:
        Calculator()

    else:
        Errors().file_missing()
