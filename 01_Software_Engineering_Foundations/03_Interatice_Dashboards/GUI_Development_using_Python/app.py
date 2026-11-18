from tkinter import *
from mydb import Database
from tkinter import messagebox
class NLPApp:
    def __init__(self):
        # login ka gui

        self.dbo = Database()
        self.root = Tk()
        self.root.title("NLP Application")
        self.root.iconbitmap(r"D:\GENAI\DSMP_Course\00_Miscellenious\02_GUI_Development\resources\favicon.ico")
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f0f0")

        self.login_gui()



        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp",font = ("Helvetica", 24, "bold"), bg="#f0f0f0",fg='#333333')
        heading.pack(pady=(30,30))

        label1 = Label(self.root, text='Enter Email : ')
        label1.pack(pady=(10,5))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5,10),ipady=5)

        label2 = Label(self.root, text='Enter Password : ')
        label2.pack(pady=(10,5))

        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5,10),ipady=5)

        login_button = Button(self.root,text ="Login",command = self.perform_login)
        login_button.pack(pady=(20,10),ipady=5, ipadx=10)

        label3 = Label(self.root, text='Not a member? Sign up now!',fg='#333333',bg='#f0f0f0',font = ("Helvetica", 10,"bold"))
        label3.pack(pady=(10,5))

        redirect_button = Button(self.root,text = 'Sign Up',command=self.signup_gui)
        redirect_button.pack(pady=(5,10),ipady=5,ipadx=10)


    def signup_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp",font = ("Helvetica", 24, "bold"), bg="#f0f0f0",fg='#333333')
        heading.pack(pady=(30,30))
        
        label0 = Label(self.root, text='Enter Name : ')
        label0.pack(pady=(10,5))
        
        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(5,10),ipady=5)
        
        label1 = Label(self.root, text='Enter Mail : ')
        label1.pack(pady=(10,5))
        
        self.mail_input = Entry(self.root, width=30)
        self.mail_input.pack(pady=(5,10),ipady=5)

        label2 = Label(self.root, text='Enter Password : ')
        label2.pack(pady=(10,5))
                
        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5,10),ipady=5)
        
        signup_button = Button(self.root,text ="Sign Up",command=self.perform_signup)
        signup_button.pack(pady=(20,10),ipady=5, ipadx=10)
        
        label3 = Label(self.root, text='Already a member? Sign in now!',fg='#333333',bg='#f0f0f0',font = ("Helvetica", 10,"bold"))
        label3.pack(pady=(10,5))
        
        redirect_button = Button(self.root,text = 'Sign In',command=self.login_gui)
        redirect_button.pack(pady=(5,10),ipady=5,ipadx=10)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def perform_signup(self):
        name = self.name_input.get()
        mail = self.mail_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,mail,password)

        if response:
            messagebox.showinfo("Sign Up Successful", "You have been successfully signed up!")
        else:
            messagebox.showerror("Sign Up Failed", "Email already exists. Please try again with a different email.")

    def perform_login(self):
        mail = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search_data(mail, password)

        if response:
            messagebox.showinfo("Login Successful", "You have been successfully logged in!")
            self.home_gui()
        else:
            messagebox.showerror("Login Failed", "Invalid email or password. Please try again.")

    def home_gui(self):
        self.clear()
        heading = Label(self.root, text="Welcome to NLPApp!",font = ("Helvetica",24,"bold"),bg="#f0f0f0",fg="#333333")
        heading.pack(pady=(30,30))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4,
                               command=self.perform_registration)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4,
                               command=self.perform_registration)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))


        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
            txt = txt + i + ' -> ' + str(result['sentiment'][i]) + '\n'

        print(txt)
        self.sentiment_result['text'] = txt






nlp = NLPApp()