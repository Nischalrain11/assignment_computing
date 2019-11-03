"""
This is the final assignment of introduction to algorithm.
"""

import sys

try:
    from tkinter import *
    from tkinter import ttk, messagebox as mb
    import mysql.connector as mc
    import hashlib
    import datetime

except ModuleNotFoundError:
    print('Module not found')
    sys.exit()

try:
    connector = mc.connect(user='root', passwd='eth!c@lhack', host='localhost')
    db_cursor = connector.cursor(prepared=True)
    db_cursor.execute('create database if not exists student_management_system')
    connector.database = 'student_management_system'
    db_cursor.execute('create table if not exists student_information('
                      'id int, '
                      'f_name varchar(50), '
                      'l_name varchar(50), '
                      'contact varchar(20),'
                      'address varchar(50), '
                      'dob date, '
                      'gender varchar(6), '
                      'degree varchar(40),'
                      'constraint pk_id primary key(id))')

    db_cursor.execute("create table if not exists user_credential("
                      "username varchar(30), "
                      "password varchar(150), "
                      'f_name varchar(50), '
                      'l_name varchar(50), '
                      'contact varchar(20),'
                      'address varchar(50), '
                      'dob date, '
                      'gender varchar(6), '
                      'degree varchar(40),'
                      "constraint pk_username primary key(username))")

except mc.ProgrammingError as err:
    error_window = Tk()
    error_window.withdraw()
    mb.showerror('Error', err)
    sys.exit()


def open_connection():
    global connector, db_cursor
    connector = mc.connect(user='root', passwd='eth!c@lhack', host='localhost', database='student_management_system')
    db_cursor = connector.cursor(prepared=True)


def close_connection():
    if db_cursor:
        db_cursor.close()
    if connector:
        connector.close()


class MyEntry(Entry):
    def __init__(self, window, default_msg='', **kwargs):
        super().__init__(window, **kwargs)
        self.config(fg='#9ea0a3', font='Arial 14', highlightthickness=1, highlightbackground='#4584F1', bd=1,
                    highlightcolor='#4584F1', relief='flat')
        self.label = default_msg
        self.on_exit()
        self.bind('<FocusIn>', lambda e: self.on_entry())
        self.bind('<FocusOut>', lambda e: self.on_exit())

    def on_entry(self):
        if self.get() == self.label:
            self.delete(0, END)
            self.config(fg='#1D254F', highlightthickness=1, highlightbackground='#4584F1', highlightcolor='#4584F1')
        else:
            self.config(fg='#1D254F', highlightthickness=1, highlightbackground='#4584F1', highlightcolor='#4584F1')

    def on_exit(self):
        if not self.get():
            self.insert(0, self.label)
            self.config(fg='#9ea0a3', highlightthickness=0)

        else:
            self['foreground'] = '#1D254F'
            self.config(highlightthickness=0)


class MyButton(Button):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.config(relief='flat', highlightcolor='black', activebackground='light blue', highlightthickness=1)


class MyLabel(Label):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.config(anchor=E, bg='light blue')


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Set on exit protocol for tkinter window
        self.protocol('WM_DELETE_WINDOW', self.exit_function)

        # setup frame
        self.container_frame = Frame(self)
        self.container_frame.pack(side='top', fill='both', expand=True)

        self.container_frame.grid_rowconfigure(0, weight=1)
        self.container_frame.grid_columnconfigure(0, weight=1)

        self.pages = {}

        for page in (LoginPage, CreateAccount, User, ForgotPassword):
            frame = page(self.container_frame, self)
            self.pages[page] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(LoginPage)

    def show_frame(self, context):
        frame = self.pages[context]
        frame.tkraise()

    def exit_function(self):
        confirm = mb.askyesno('Quit', 'Are you sure you want to exit?')
        if confirm:
            db_cursor.close()
            connector.close()
            self.destroy()


class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid_propagate(0)
        self.config(bg='light blue')
        self.control = controller

        photo = PhotoImage(file='login_head_picture.PNG')
        lbl_photo = MyLabel(self, image=photo)
        lbl_photo.photo = photo
        lbl_photo.place(x=304, y=25)

        self.username = MyEntry(self, 'Username', font='arial 11 bold', bg='white', width=30)
        self.password = MyEntry(self, 'PasswordHere', font='arial 11 bold', bg='white', show='*', width=30)
        self.password.bind('<Return>', lambda e: self.login())

        self.username.place(x=220, y=193)
        self.password.place(x=220, y=245)

        self.btn_forgot_password = MyButton(self, text="Forgot password?", fg='#4760EB', font='arial 12 underline',
                                            bg='light blue', command=lambda: self.control.show_frame(ForgotPassword))
        self.btn_login = MyButton(self, width=10, fg='white', text="Login", bg='#4760EB', font='arial 12 bold',
                                  command=self.login)
        self.btn_create_account = MyButton(self, text="Create a new account", bg='light blue', fg='#4760EB',
                                           font='arial 12 underline',
                                           command=lambda: self.control.show_frame(CreateAccount))
        self.btn_forgot_password.place(x=426, y=275)
        self.btn_login.place(x=325, y=330)
        self.btn_create_account.place(x=315, y=470)

        self.lbl_no_account = MyLabel(self, font='arial 14 bold', text='I don\'t have an account.')
        self.lbl_no_account.place(x=285, y=435)

    def login(self):
        username = self.username.get()
        password = self.password.get()
        hashing_password = hashlib.sha512(password.encode('UTF-8'))
        hashed_password = hashing_password.hexdigest()

        values = (username, hashed_password)
        query = 'select username, password from user_credential where username=%s and password=%s'

        open_connection()
        db_cursor.execute(query, values)
        result = db_cursor.fetchall()
        close_connection()

        if result:
            root.geometry('1300x680+20+15')
            self.password.delete(0, END)
            self.focus()
            self.control.show_frame(User)
        else:
            mb.showinfo('Login Error', 'Invalid username or password.')


class CreateAccount(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(bg='light blue')
        self.grid_propagate(0)
        self.control = controller

        label = MyLabel(self, text='Sign Up', anchor=W, font='arial 26 bold')
        label2 = MyLabel(self, text='It\'s quick and easy.', anchor=W, font='arial 15')
        label3 = MyLabel(self, text='Date of Birth', anchor=W, font='arial 13')

        label.place(x=240, y=15)
        label2.place(x=240, y=70)
        label3.place(x=235, y=320)

        self.mem_id = MyEntry(self, 'User ID', font='arial 10 bold', bg='white', width=30)
        self.f_name = MyEntry(self, 'First Name', font='arial 10 bold', bg='white', width=14)
        self.l_name = MyEntry(self, 'Last Name', font='arial 10 bold', bg='white', width=14)
        self.entry_password = MyEntry(self, 'New Password', font='arial 10 bold', bg='white', width=30, show='*')
        self.contact = MyEntry(self, 'Phone Number', font='arial 10 bold', bg='white', width=30)
        self.address = MyEntry(self, 'Address', font='arial 10 bold', bg='white', width=30)

        self.btn_show_pass = MyButton(self, text="Show", font='arial 11 bold', command=self.password_show)

        self.mem_id.place(x=240, y=120)
        self.f_name.place(x=240, y=153)
        self.l_name.place(x=415, y=153)
        self.entry_password.place(x=240, y=186)
        self.btn_show_pass.place(x=630, y=186)
        self.contact.place(x=240, y=240)
        self.address.place(x=240, y=273)

        # 3 combo boxes
        self.dt = datetime.datetime.today()
        self.combo_day = ttk.Combobox(self, width=3, font='arial 12')
        self.combo_day['values'] = tuple(i for i in range(1, 32))
        self.combo_day.current(self.dt.day - 1)
        self.combo_day.place(x=250, y=356)

        self.combo_month = ttk.Combobox(self, width=3, font='arial 12')
        self.combo_month['values'] = tuple(i for i in range(1, 13))
        self.combo_month.current(self.dt.month - 1)
        self.combo_month.place(x=300, y=356)

        self.combo_year = ttk.Combobox(self, width=6, font='arial 12')
        self.combo_year['values'] = tuple(i for i in range(1900, self.dt.year + 1))
        self.combo_year.current(self.dt.year - 1900)
        self.combo_year.place(x=350, y=356)

        # 3 radio buttons
        label4 = MyLabel(self, text='Gender', anchor=W, font='arial 13')
        label4.config(font='arial 13')
        label4.place(x=235, y=400)

        self.gender = StringVar()
        self.radio_male = Radiobutton(self, variable=self.gender, text='Male', bg='light blue', value='Male')
        self.radio_male.invoke()
        self.radio_female = Radiobutton(self, variable=self.gender, text='Female', value='Female', bg='light blue')
        self.radio_custom = Radiobutton(self, variable=self.gender, text='Custom', value='Custom', bg='light blue')
        self.radio_male.place(x=260, y=430)
        self.radio_female.place(x=330, y=430)
        self.radio_custom.place(x=400, y=430)

        # combo box
        label5 = MyLabel(self, text='Degree', font='arial 13', anchor=W)
        label5.place(x=235, y=465)

        self.combo_degree = ttk.Combobox(self, width=22, font='arial 12')
        self.combo_degree['values'] = ('Computing', 'Ethical Hacking', 'Commerce', 'Civil Engineering')
        self.combo_degree.current(0)
        self.combo_degree.place(x=234, y=496)

        self.btn_back = MyButton(self, width=10, fg='white', text="Back", bg='#4760EB', font='arial 12 bold',
                                 command=self.back)
        self.btn_back.place(x=235, y=555)

        self.btn_signup = MyButton(self, width=10, fg='white', text="Sign Up", bg='#4760EB', font='arial 12 bold',
                                   command=self.sign_up)
        self.btn_signup.place(x=465, y=555)
        self.password_show_state = False

    def password_show(self):
        if not self.password_show_state:
            self.entry_password.config(show='')
            self.password_show_state = True
        else:
            self.entry_password.config(show='*')
            self.password_show_state = False

    def back(self):
        self.control.show_frame(LoginPage)
        self.clear()

    def sign_up(self):
        try:
            teacher_id = self.mem_id.get()
            f_name = self.f_name.get().title()
            l_name = self.l_name.get().title()
            contact = self.contact.get()
            address = self.address.get().title()
            dob = self.combo_year.get() + '-' + self.combo_month.get() + '-' + self.combo_day.get()
            gender = self.gender.get()
            degree = self.combo_degree.get()

            password = self.entry_password.get()
            hashing_password = hashlib.sha512(password.encode('UTF-8'))
            hashed_password = hashing_password.hexdigest()

            if teacher_id == 'Teacher ID' or teacher_id == '':
                mb.showinfo('ID', 'Enter your teacher ID')
                return
            if f_name == 'First Name' or f_name == '':
                mb.showinfo('First Name', 'Enter your first name')
                return
            if l_name == 'Last Name' or l_name == '':
                mb.showinfo('Last Name', 'Enter your last name')
                return
            if password == 'New Password' or password == '':
                mb.showinfo('Password', 'Enter your new password')
                return
            if contact == 'Phone Number or email' or contact == '':
                mb.showinfo('Contact', 'Enter your contact')
                return
            if address == 'Address' or address == '':
                mb.showinfo('Address', 'Enter your address')
                return
            if not f_name.isalpha() or not l_name.isalpha():
                mb.showinfo('Name --> Alphabets', 'Name should contain alphabets only.')
                return
            if not contact.isdigit():
                mb.showinfo('Contact --> Numbers', 'Contact should contain number only.')
                return
            if len(contact) < 8:
                mb.showinfo('Phone number', 'Number should be of length more than 7')
                return
            if dob > f'{self.dt.year}-{self.dt.month}-{self.dt.day}':
                mb.showinfo('Date of birth --> Future', 'Student date of birth is more than current time.')
                return

            query = 'insert into user_credential() values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            values = (teacher_id, hashed_password, f_name, l_name, contact, address, dob, gender, degree)

            open_connection()
            db_cursor.execute(query, values)
            connector.commit()
            close_connection()
            mb.showinfo('Sign Up', 'Account created successfully.')
            self.clear()

        except mc.IntegrityError as error:
            if str(error)[0:4] == '1062':
                mb.showinfo('Duplicate Entry', "Data already exists in the database.")
        except mc.InterfaceError:
            mb.showinfo('Data too long', 'Try shorter value.')

    def clear(self):
        self.mem_id.delete(0, END)
        self.f_name.delete(0, END)
        self.l_name.delete(0, END)
        self.entry_password.delete(0, END)
        self.contact.delete(0, END)
        self.address.delete(0, END)

        self.mem_id.focus()
        self.f_name.focus()
        self.l_name.focus()
        self.entry_password.focus()
        self.contact.focus()
        self.address.focus()
        self.focus()


class ForgotPassword(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(bg='#F87281')
        self.control = controller

        self.frame_forgot_password = Frame(self, width=400, height=420, bg='#FFFFFF', relief=RIDGE,
                                           highlightthickness=2, highlightbackground='#4584F1',
                                           highlightcolor='#4584F1')
        self.frame_forgot_password.pack_propagate(0)
        self.frame_forgot_password.place(x=195, y=90)

        self.lbl_forgot_password = MyLabel(self.frame_forgot_password, text="Forgot Your Password?",
                                           font='arial 24 bold')
        self.lbl_forgot_password.config(bg='white', fg='#F87281', anchor=W)
        self.lbl_forgot_password_info = MyLabel(self.frame_forgot_password, text="It\'s quick and easy to change.",
                                                font='arial 15', anchor=W)
        self.lbl_forgot_password_info.config(bg='white')
        self.lbl_forgot_password.place(x=15, y=25)
        self.lbl_forgot_password_info.place(x=15, y=76)

        self.username = MyEntry(self.frame_forgot_password, 'User ID', width=22, font='arial 11')
        self.new_pass = MyEntry(self.frame_forgot_password, 'Your New Password', width=22, font='arial 11', show='*')
        self.confirm_new_pass = MyEntry(self.frame_forgot_password, 'Confirm Password ', width=22, font='arial 11',
                                        show='*')
        self.confirm_new_pass.bind('<Return>', lambda e: self.reset())
        self.btn_show_password = Button(self.frame_forgot_password, width=8, text='Show', font='arial 11',
                                        command=self.password_show)

        self.username.place(x=30, y=150)
        self.new_pass.place(x=30, y=200)
        self.confirm_new_pass.place(x=30, y=250)
        self.btn_show_password.place(x=300, y=250)

        self.btn_back = Button(self.frame_forgot_password, width=8, text='Back', font='arial 11', command=self.back)
        self.btn_reset = Button(self.frame_forgot_password, width=8, text='Reset', font='arial 11', fg='green',
                                command=self.reset)

        self.btn_back.place(x=65, y=343)
        self.btn_reset.place(x=237, y=343)
        self.password_show_state = False

    def password_show(self):
        if not self.password_show_state:
            self.new_pass.config(show='')
            self.confirm_new_pass.config(show='')
            self.password_show_state = True
        else:
            self.new_pass.config(show='*')
            self.confirm_new_pass.config(show='*')
            self.password_show_state = False

    def back(self):
        self.control.show_frame(LoginPage)
        self.clear()

    def clear(self):
        self.username.delete(0, END)
        self.new_pass.delete(0, END)
        self.confirm_new_pass.delete(0, END)

        self.username.focus()
        self.new_pass.focus()
        self.confirm_new_pass.focus()
        self.frame_forgot_password.focus()

    def reset(self):
        username = self.username.get()
        new_pass = self.new_pass.get()
        retyped_pass = self.confirm_new_pass.get()

        if new_pass == retyped_pass:
            try:
                if len(new_pass) >= 8:
                    query = 'select username from user_credential where username=%s'

                    open_connection()
                    db_cursor.execute(query, (username,))
                    user = db_cursor.fetchall()

                    if user:
                        hashing_password = hashlib.sha512(new_pass.encode('UTF-8'))
                        hashed_password = hashing_password.hexdigest()
                        values = (hashed_password, username)
                        query = 'update user_credential set password=%s where username=%s'
                        db_cursor.execute(query, values)
                        connector.commit()
                        mb.showinfo('Success', 'Password successfully changed.')
                        self.clear()

                    else:
                        mb.showinfo('Invalid Username!!', 'User does not exist.')

                    close_connection()

                else:
                    mb.showinfo('Weak Length', 'Password must be 8 character long.')

            except mc.IntegrityError as error:
                print(error)

        else:
            mb.showinfo('Error', 'Password did not match.\nRetype your password again.')


class User(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(bg='light blue')
        self.control = controller

        show_frame = Frame(self, width=830, height=392, relief=RIDGE, bd=4)
        show_frame.pack_propagate(0)
        show_frame.place(x=30, y=140)

        frame_add_student = Frame(self, width=330, height=470, relief=RIDGE, bd=4, bg='light blue')
        frame_add_student.pack_propagate(0)
        frame_add_student.place(x=928, y=140)

        self.entry_search = MyEntry(self, 'Search', width=28, font='arial 11')
        self.btn_search = Button(self, width=8, text='Search', font='arial 11', command=self.search)
        self.btn_logout = Button(self, width=8, text='Log Out', font='arial 11', command=self.logout)

        self.entry_search.place(x=340, y=20)
        self.btn_search.place(x=700, y=20)
        self.btn_logout.place(x=1190, y=15)

        self.lbl_search_by = MyLabel(self, text="Search By", font='arial 13', bg='light blue')
        self.lbl_sort_by = MyLabel(self, text="Sort By", font='arial 13', bg='light blue')

        self.lbl_search_by.place(x=785, y=70)
        self.lbl_sort_by.place(x=1035, y=70)

        self.combo_search = ttk.Combobox(self, width=12, font='arial 12')
        self.combo_search['values'] = ('Id', 'First Name', 'Last Name', 'Contact', 'Address', 'Date of Birth',
                                       'Gender', 'Degree')
        self.combo_search.current(0)

        self.combo_sort = ttk.Combobox(self, width=12, font='arial 12')
        self.combo_sort['values'] = ('Id', 'First Name', 'Last Name', 'Contact', 'Address', 'Date of Birth', 'Gender',
                                     'Degree')
        self.combo_sort.current(0)

        self.combo_search.place(x=875, y=70)
        self.combo_sort.place(x=1105, y=70)

        self.order_by = StringVar()
        self.radio_ascending = Radiobutton(self, variable=self.order_by, text='Ascending', value='ascending',
                                           bg='light blue')
        self.radio_ascending.invoke()
        self.radio_descending = Radiobutton(self, variable=self.order_by, text='Descending', value='descending',
                                            bg='light blue')
        self.radio_ascending.place(x=1045, y=100)
        self.radio_descending.place(x=1160, y=100)

        # ---------------- Entry of the form ----------------
        self.lbl_add_student = MyLabel(frame_add_student, text="Add Student", font='arial 14 bold', bg='light blue')
        self.lbl_add_student.place(x=10, y=5)

        self.entry_id = MyEntry(frame_add_student, 'Student ID', width=26, font='arial 9')
        self.entry_f_name = MyEntry(frame_add_student, 'First Name', width=12, font='arial 9')
        self.entry_l_name = MyEntry(frame_add_student, 'Last Name', width=12, font='arial 9')
        self.entry_contact = MyEntry(frame_add_student, 'Contact', width=26, font='arial 9')
        self.entry_address = MyEntry(frame_add_student, 'Address', width=26, font='arial 9')

        self.entry_id.place(x=10, y=40)
        self.entry_f_name.place(x=10, y=70)
        self.entry_l_name.place(x=164, y=70)
        self.entry_contact.place(x=10, y=100)
        self.entry_address.place(x=10, y=130)

        self.lbl_dob = MyLabel(frame_add_student, text="Date of Birth", font='arial 13', anchor=W)
        self.lbl_dob.place(x=10, y=170)

        self.dt = datetime.datetime.today()
        self.combo_day = ttk.Combobox(frame_add_student, width=4, font='arial 12')
        self.combo_day['values'] = tuple(i for i in range(1, 32))
        self.combo_day.current(self.dt.day - 1)
        self.combo_day.place(x=60, y=200)

        self.combo_month = ttk.Combobox(frame_add_student, width=4, font='arial 12')
        self.combo_month['values'] = tuple(i for i in range(1, 13))
        self.combo_month.current(self.dt.month - 1)
        self.combo_month.place(x=118, y=200)

        self.combo_year = ttk.Combobox(frame_add_student, width=6, font='arial 12')
        self.combo_year['values'] = tuple(i for i in range(1900, self.dt.year + 1))
        self.combo_year.current(self.dt.year - 1900)
        self.combo_year.place(x=176, y=200)

        # 3 radio buttons
        label4 = MyLabel(frame_add_student, text='Gender', font='arial 13', anchor=W)
        label4.place(x=10, y=230)

        self.gender = StringVar()
        self.radio_male = Radiobutton(frame_add_student, variable=self.gender, text='Male', bg='light blue',
                                      value='Male')
        self.radio_male.invoke()
        self.radio_female = Radiobutton(frame_add_student, variable=self.gender, text='Female', value='Female',
                                        bg='light blue')
        self.radio_custom = Radiobutton(frame_add_student, variable=self.gender, text='Custom', value='Custom',
                                        bg='light blue')
        self.radio_male.place(x=50, y=260)
        self.radio_female.place(x=130, y=260)
        self.radio_custom.place(x=210, y=260)

        # combo box
        label5 = MyLabel(frame_add_student, text='Degree', anchor=W)
        label5.config(font='arial 13')
        label5.place(x=10, y=290)

        self.combo_degree = ttk.Combobox(frame_add_student, width=22, font='arial 12')
        self.combo_degree['values'] = ('BSc. Computing', 'BSc. Ethical Hacking', 'Commerce', 'Civil Engineering')
        self.combo_degree.current(0)
        self.combo_degree.place(x=10, y=320)

        # ------------ Tree view ------------------
        self.scroll_x = Scrollbar(show_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(show_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(show_frame, height=17, column=('id', 'f_name', 'l_name', 'contact', 'address',
                                                                         'date_of_birth', 'gender', 'degree'),
                                          xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.student_table.place(x=0, y=0)

        self.student_table.column('id', width=80)
        self.student_table.column('f_name', width=100)
        self.student_table.column('l_name', width=100)
        self.student_table.column('contact', width=108)
        self.student_table.column('address', width=115)
        self.student_table.column('date_of_birth', width=96)
        self.student_table.column('gender', width=90)
        self.student_table.column('degree', width=112)
        self.student_table['show'] = 'headings'

        self.student_table.heading('id', text='ID', anchor=W)
        self.student_table.heading('f_name', text='First Name', anchor=W)
        self.student_table.heading('l_name', text='Last Name', anchor=W)
        self.student_table.heading('contact', text='Contact', anchor=W)
        self.student_table.heading('address', text='Address', anchor=W)
        self.student_table.heading('date_of_birth', text='Date of Birth', anchor=W)
        self.student_table.heading('gender', text='Gender', anchor=W)
        self.student_table.heading('degree', text='Degree', anchor=W)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)

        self.btn_add = Button(frame_add_student, width=8, text='Add', fg='green', font='TimesNewRoman 13',
                              command=self.add_info)
        self.btn_show = Button(self, width=8, text='Show All', font='TimesNewRoman 11', command=self.show)
        self.btn_delete = Button(self, width=8, text='Delete', fg='red', font='TimesNewRoman 11', command=self.delete)
        self.btn_update = Button(self, width=8, text='Update', fg='green', font='TimesNewRoman 11', command=self.update)
        self.btn_clear = Button(frame_add_student, width=8, text='Clear', fg='red', font='TimesNewRoman 13',
                                command=self.clear)

        self.btn_add.place(x=60, y=390)
        self.btn_show.place(x=215, y=567)
        self.btn_delete.place(x=445, y=567)
        self.btn_update.place(x=675, y=567)
        self.btn_clear.place(x=185, y=390)

        self.entry_search.bind('<Return>', lambda e: self.search())
        self.student_table.bind('<ButtonRelease-1>', lambda e: self.pointer())

        self.show()

    def add_info(self):
        try:
            std_id = self.entry_id.get()
            f_name = self.entry_f_name.get().title()
            l_name = self.entry_l_name.get().title()
            contact = self.entry_contact.get()
            address = self.entry_address.get().title()
            dob = self.combo_year.get() + '-' + self.combo_month.get() + '-' + self.combo_day.get()
            gender = self.gender.get().title()
            degree = self.combo_degree.get()
            self.dt = datetime.datetime.today()

            if std_id == 'Student ID':
                mb.showinfo('ID', 'Enter ID')
                return

            if not std_id.isdigit():
                mb.showinfo('ID', 'ID should contain numbers only.')
                return
            else:
                std_id = int(std_id)

            if f_name == 'First Name' or f_name == '':
                mb.showinfo('Name', 'Please enter your first name.')
                return

            if l_name == 'Last Name' or l_name == '':
                l_name = ''

            if contact == 'Contact' or contact == '':
                mb.showinfo('Contact', 'Please enter your contact.')
                return

            if address == 'Address' or address == '':
                mb.showinfo('Address', 'Please enter your address.')
                return

            if not f_name.isalpha() or not l_name.isalpha():
                mb.showinfo('Name --> Alphabets', 'Name should contain alphabets only.')
                return

            if not contact.isdigit():
                mb.showinfo('Contact --> Numbers', 'Contact should contain number only.')
                return

            if len(f_name) > 50:
                mb.showinfo('First Name', 'First name should be less than 50')
                return

            if len(l_name) > 50:
                mb.showinfo('Last Name', 'Last name should be less than 50')
                return

            if len(contact) > 20:
                mb.showinfo('Contact', 'Contact number should be less than 20')
                return

            if len(address) > 50:
                mb.showinfo('Address', 'Address should be less than 50')
                return

            if not 8 < len(contact) < 20:
                mb.showinfo('Phone number', 'Number should be of length more than 7 and less than 20')
                return

            if dob > f'{self.dt.year}-{self.dt.month}-{self.dt.day}':
                mb.showinfo('Date of birth --> Future', 'Student date of birth is more than current time.')
                return

            values = (std_id, f_name, l_name, contact, address, dob, gender, degree)
            query = 'insert into student_information() values(%s, %s, %s, %s, %s, %s, %s, %s)'

            open_connection()
            db_cursor.execute(query, values)
            mb.showinfo('Success', "Data inserted successfully.")
            connector.commit()
            close_connection()

            self.show()

        except mc.IntegrityError as error:
            if str(error)[0:4] == '1062':
                mb.showinfo('Duplicate Entry', 'Data already exists in the database.')
            else:
                print(error)

    def clear(self):
        self.entry_id['state'] = 'normal'
        self.entry_id.delete(0, END)
        self.entry_f_name.delete(0, END)
        self.entry_l_name.delete(0, END)
        self.entry_contact.delete(0, END)
        self.entry_address.delete(0, END)
        self.combo_day.set(self.dt.day)
        self.combo_month.set(self.dt.month)
        self.combo_year.set(self.dt.year)
        self.radio_male.invoke()
        self.combo_degree.set('BSc. Computing')

        self.entry_id.focus()
        self.entry_f_name.focus()
        self.entry_l_name.focus()
        self.entry_contact.focus()
        self.entry_address.focus()
        self.entry_search.focus()
        self.btn_clear.focus()

    def show(self):
        records = self.student_table.get_children()
        self.student_table.delete(*records)

        query = 'select * from student_information'

        open_connection()
        db_cursor.execute(query)
        results = db_cursor.fetchall()
        close_connection()

        self.quick_sort(results, 0, len(results)-1)
        for row in results:
            self.student_table.insert('', 'end', values=row)

    def search(self, array=None):
        try:
            if array is None:
                query = f"select * from student_information"

                open_connection()
                db_cursor.execute(query)
                results = db_cursor.fetchall()
                close_connection()
            else:
                results = array

            self.quick_sort(results, 0, len(results)-1)

            records = self.student_table.get_children()
            self.student_table.delete(*records)

            search_by = self.combo_search.get()
            target = self.entry_search.get()

            if search_by == 'Id':
                column_index = 0
                target = int(self.entry_search.get())
            elif search_by == 'First Name':
                column_index = 1
                target = self.entry_search.get().title()
            elif search_by == 'Last Name':
                column_index = 2
                target = self.entry_search.get().title()
            elif search_by == 'Contact':
                column_index = 3
            elif search_by == 'Address':
                column_index = 4
                target = self.entry_search.get().title()
            elif search_by == 'Date of Birth':
                column_index = 5
                try:
                    target = datetime.date(*(int(i) for i in self.entry_search.get().split('-')))
                except ValueError or TypeError or OverflowError:
                    mb.showinfo('Sorry!!', 'Please enter valid date in format like 2000-01-02.')
            elif search_by == 'Gender':
                column_index = 6
                target = self.entry_search.get().title()
            else:
                column_index = 7

            final_result = []

            for row in results:
                if target == row[column_index]:
                    final_result.append(row)

            for row in final_result:
                self.student_table.insert('', 'end', values=row)

            return final_result

        except ValueError:
            pass

    def partition(self, sort_array, low, high):
        sort_by = self.combo_sort.get()
        if sort_by == 'Id':
            column_index = 0
        elif sort_by == 'First Name':
            column_index = 1
        elif sort_by == 'Last Name':
            column_index = 2
        elif sort_by == 'Contact':
            column_index = 3
        elif sort_by == 'Address':
            column_index = 4
        elif sort_by == 'Date of Birth':
            column_index = 5
        elif sort_by == 'Gender':
            column_index = 6
        else:
            column_index = 7

        order_by = self.order_by.get()
        if order_by == 'ascending':
            i = (low - 1)  # Set the low value to i
            pivot = sort_array[high][column_index]  # Set the pivot
            for j in range(low, high):
                if sort_array[j][column_index] <= pivot:  # If true
                    i += 1  # Increase i by 1
                    sort_array[i], sort_array[j] = sort_array[j], sort_array[i]  # swap
            sort_array[i + 1], sort_array[high] = sort_array[high], sort_array[i + 1]  # swap pivot with last
            return i + 1

        else:
            i = (low - 1)  # Set the low value to i
            pivot = sort_array[high][column_index]  # Set the pivot
            for j in range(low, high):
                if sort_array[j][column_index] >= pivot:  # If true
                    i += 1  # Increase i by 1
                    sort_array[i], sort_array[j] = sort_array[j], sort_array[i]  # swap
            sort_array[i + 1], sort_array[high] = sort_array[high], sort_array[i + 1]  # swap pivot with last
            return i + 1

    def quick_sort(self, sort_array, low, high):
        if low < high:
            pi = self.partition(sort_array, low, high)  # call above partition function
            self.quick_sort(sort_array, pi + 1, high)  # call itself to sort larger numbers'
            self.quick_sort(sort_array, low, pi - 1)  # call itself to sort smaller numbers'

    def update(self):
        try:
            f_name = self.entry_f_name.get().title()
            l_name = self.entry_l_name.get().title()
            contact = self.entry_contact.get()
            address = self.entry_address.get().title()
            dob = self.combo_year.get() + '-' + self.combo_month.get() + '-' + self.combo_day.get()
            gender = self.gender.get()
            degree = self.combo_degree.get()

            if self.pointer() is None:
                mb.showinfo('Select student', 'Select student to update their detail.')
                return

            if f_name == 'First Name' or f_name == '':
                mb.showinfo('Name', 'Please enter your first name.')
                return

            if l_name == 'Last Name' or l_name == '':
                l_name = ''

            if contact == 'Contact' or contact == '':
                mb.showinfo('Contact', 'Please enter your contact.')
                return

            if address == 'Address' or address == '':
                mb.showinfo('Address', 'Please enter your address.')
                return

            if not f_name.isalpha() or not l_name.isalpha():
                mb.showinfo('Name --> Alphabets', 'Name should contain alphabets only.')
                return

            if not contact.isdigit():
                mb.showinfo('Contact --> Numbers', 'Contact should contain number only.')
                return

            if len(f_name) > 50:
                mb.showinfo('First Name', 'First name should be less than 50')
                return

            if len(l_name) > 50:
                mb.showinfo('Last Name', 'Last name should be less than 50')
                return

            if len(contact) > 20:
                mb.showinfo('Contact', 'Contact number should be less than 20')
                return

            if len(address) > 50:
                mb.showinfo('Address', 'Address should be less than 50')
                return

            if not 8 < len(contact) < 20:
                mb.showinfo('Phone number', 'Number should be of length more than 7 and less than 20')
                return

            if dob > f'{self.dt.year}-{self.dt.month}-{self.dt.day}':
                mb.showinfo('Date of birth --> Future', 'Student date of birth is more than current time.')
                return

            values = (f_name, l_name, contact, address, dob, gender, degree, self.pointer())
            query = 'update student_information set f_name=%s, l_name=%s, contact=%s, address=%s, dob=%s, gender=%s,' \
                    ' degree=%s where id=%s'

            open_connection()
            db_cursor.execute(query, values)
            connector.commit()
            close_connection()

            self.clear()
            self.show()

        except ValueError as error:
            print(error)

        except mc.InterfaceError:
            mb.showinfo('Data too long', 'Try shorter value.')

    def delete(self):
        if self.pointer() is None:
            mb.showinfo('Select student', 'Select student from table to delete.')
        else:
            query = 'delete from student_information where id=%s'
            values = (self.pointer(),)

            open_connection()
            db_cursor.execute(query, values)
            connector.commit()
            close_connection()

            self.show()
            self.clear()

    def pointer(self):
        try:
            self.clear()
            point = self.student_table.focus()
            content = self.student_table.item(point)
            row = content['values']
            self.entry_id.insert(0, row[0])
            self.entry_id['state'] = 'disabled'
            self.entry_f_name.insert(0, row[1])
            self.entry_l_name.insert(0, row[2])
            self.entry_contact.insert(0, row[3])
            self.entry_address.insert(0, row[4])

            this_date = row[5].split('-')
            self.combo_year.set(this_date[0])
            self.combo_month.set(this_date[1])
            self.combo_day.set(this_date[2])

            if row[6] == 'Male':
                self.radio_male.invoke()
            elif row[6] == 'Female':
                self.radio_female.invoke()
            else:
                self.radio_custom.invoke()

            self.combo_degree.set(row[7])
            return row[0]

        except IndexError:
            pass

    def logout(self):
        confirm = mb.askyesno('Confirm logout.', 'Are you sure you want to logout?')
        if confirm:
            self.control.show_frame(LoginPage)
            self.entry_search.delete(0, END)
            self.clear()
            root.geometry('780x620+280+30')


if __name__ == '__main__':
    root = MainWindow()
    root.title("Student Management System")
    root.geometry('780x620+280+30')
    root.mainloop()
