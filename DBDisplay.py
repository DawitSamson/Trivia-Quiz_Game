from DB import *
from SMS import *
from DB_DML import *


def AdminDetailMainDB():
    AdminDB = DBAdmin()  # DATABASE ADMIN
    while True:
        AdminSection_WelcomeText()
        try:
            Choice = int(input("Enter Your Choice: "))
            if Choice == 1:
                print(
                    ColorLab.BOLD + ColorLab.YELLOW + "To Insert a new Admin User Please give the details information" + ColorLab.END)
                UserId = int(input('\t\t\t\tEnter user Id number: '))
                UserName = input("\t\t\t\tEnter User Name: ")
                UserPassword = input("\t\t\t\tEnter User Password: ")
                AdminDB.Insert_AdminUser(UserId, UserName, UserPassword)
            elif Choice == 2:
                UserId = input("To Display a User please enter exist UserID: ")
                AdminDB.Display_One_User(int(UserId))
            elif Choice == 3:
                print(ColorLab.BOLD + ColorLab.YELLOW + "\nDetail in DATABASE" + ColorLab.END)
                print()
                AdminDB.Display_All_Users()
            elif Choice == 4:
                UserId = input("To Delete a Single User please enter exist UserID: ")
                AdminDB.delete_user(int(UserId))
            elif Choice == 5:
                print(ColorLab.BOLD + ColorLab.YELLOW + "\nTo update a user Please file the details:" + ColorLab.END)
                UserId = int(input("User ID for Existing User: "))
                UserName = input("Enter New Name for the Existing User: ")
                UserPassword = int(input("Enter New Password of user: "))
                AdminDB.update_user(UserId, UserName, UserPassword)
            elif Choice == 6:
                CreateDB()  # To create Database on MYSQL
            elif Choice == 7:
                CreateTabel()  # To Create Tabel on The DataBase
            elif Choice == 8:
                DeleteTabel()  # To Delete Tabel on The DataBase
            elif Choice == 9:
                InsertPlayer_Score()  # To Insert Players on The DataBase
            elif Choice == 10:
                UpdatePlayerScore()  # To Update Players on The DataBase
            elif Choice == 11:
                return
            else:
                Invalid_InputText()
        except Exception as e:
            print(e)
            Invalid_DetailsText()


def AdminQuizMain():
    QuestionDB = QuestionAdminDB()
    while True:
        AdminQuestionSection_WelcomeText()
        try:
            Choice = int(input("\nEnter Your Choice: "))
            if Choice == 1:
                print(ColorLab.BOLD + ColorLab.BLUE + "\nAll Question available on the Quiz DataBase\n" + ColorLab.END)
                QuestionDB.fetch_question()
            elif Choice == 2:
                print(
                    ColorLab.BOLD + ColorLab.BLUE + "To insert a New Question Please Fill the details Below" + ColorLab.END)
                QuestionNo = int(input("Enter Question id Number: "))
                Question = input("Enter the Question: ")
                Difficulty = input("Enter the Difficulty level: ")
                OptionA = input("Enter Option 1: ")
                OptionB = input("Enter Option 2: ")
                OptionC = input("Enter Option 3: ")
                OptionD = input("Enter Option 4: ")
                Answer = int(input("Enter Answer Number ? 1 | 2 | 3 | 4 => "))
                Topic = input("Enter Topic Name: ")
                QuestionDB.Insert_Question(QuestionNo, Question, Difficulty, OptionA, OptionB, OptionC, OptionD, Answer,
                                           Topic)
            elif Choice == 3:
                break
            else:
                Invalid_InputText()
        except Exception as e:
            print(e)
            Invalid_DetailsText()


def UserSection():
    UserDB = UserMainDB()

    while True:
        UserSection_WelcomeText()
        try:
            Choice = int(input("Enter Your Choice: "))
            if Choice == 1:
                General_InstructionText()
            elif Choice == 2:
                print(ColorLab.BOLD + ColorLab.GREEN + 'Are You Ready to Take The Exam? ' + ColorLab.END)
                try:
                    Selected = input(f"{ColorLab.BOLD + ColorLab.YELLOW + ' Enter Yes (Y) / No (N) : ' + ColorLab.END}")
                    if Selected == "y" or Selected == "Y" or Selected == "yes" or Selected == "Yes" or Selected == "YES":
                        UserDB.Display_Question()
                except Exception as e:
                    print(e)
                    Invalid_DetailsText()
            elif Choice == 3:
                break
            else:
                Invalid_InputText()
        except Exception as e:
            print(e)
            Invalid_DetailsText()


def Topics():
    Question_TopicText()


def AllUserDB():
    print(ColorLab.BOLD + ColorLab.GREEN + '\n************ALL PLAYER SCORE BORD ************\n' + ColorLab.END)
    ShowUserScore()


def CheckUserTypeDB():
    UserName = input("Enter User Name: ")
    UserPassword = input("Enter Password: ")
    CheckDB = DBAdmin()
    check = CheckDB.check_user(UserName, UserPassword)
    return check
