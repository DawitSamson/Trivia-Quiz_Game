from tkinter import *
from tkinter import ttk
from APP import *

root = Tk()


def Gui():
    # Display the title and label
    root.title("TRIVIA/QUIZ GAME by Dawit Belay")
    label = Label(root, text="🎮" * 15, font=('arial', 15, 'bold'), bg="black", fg="Yellow")
    label.pack(side=TOP, fill=X)
    # label = Label(root, text="", font=('arial', 15, 'bold'), bg="black", fg="yellow")
    # label.pack(side=TOP, fill=X)

    # welcome label
    label = Label(root, text="WELCOME To DAWIT-TRIVIA GAME APP", font=('arial', 12, 'bold'), bg="Blue", fg="Yellow")
    label.pack(side=TOP, fill=X)

    # Set up labels for Admin User Name
    label = Label(root, text="User Name", font=('arial', 13, 'bold'), fg="Black")
    label.place(x=30, y=135)
    # Create string variables
    UserName_entry = StringVar()
    # Set up text entry boxes
    UserName_entry = ttk.Entry(root, textvariable=UserName_entry)
    UserName_entry.place(x=190, y=135)
    UserName_entry.focus()

    # Set up labels for Password
    label = Label(root, text="Password", font=('arial', 13, 'bold'), fg="Red")
    label.place(x=30, y=170)
    # Create string variables
    UserPassword_entry = StringVar()
    # Set up text entry boxes
    UserPassword_entry = ttk.Entry(root, textvariable=UserPassword_entry)
    UserPassword_entry.place(x=190, y=170)

    def CheckAdmin():
        mydb = connector.connect(host='localhost', user='root', password='dawitsamson123', database='quizgame')
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM Users WHERE UserName =%s AND Password=%s",(UserName_entry.get(), UserPassword_entry.get()))
        # cursor.execute()
        for row in cursor:
            if row[1] == UserName_entry.get():
                print('Welcome user: ', row[1])
                MainFunction()  # Once the admin is confirmed we continue working with the Console
            else:
                print(ColorLab.BOLD + ColorLab.RED + '\t\t\t\t\t\t\t Invalid user!' + ColorLab.END)
                exit()

    # Creating Button to CheckAdmin Details and Save data using click button
    ButtonCheckAdmin = ttk.Button(root, text="   Signin\n As Admin", command=CheckAdmin)
    ButtonCheckAdmin.place(x=180, y=210, width=100, height=50)

    # Creating, razing and instance the window
    root.geometry('600x600')
    root.resizable(False, False)
    root.mainloop()




