import mysql.connector
from DesignColors import *


def CreateDB():
    mydb = mysql.connector.connect(host='localhost', user='root', password='dawitsamson123')
    cursorD = mydb.cursor()
    DataBase_Name = input("Enter DataBase Name: ")
    cursorD.execute("CREATE DATABASE '{}'".format(DataBase_Name))  # This is for creating Database
    mydb.commit()
    print(ColorLab.BOLD + ColorLab.GREEN + 'DATABASE Created.' + ColorLab.END)


def CreateTabel():
    mydb = mysql.connector.connect(host='localhost', user='root', password='dawitsamson123', database='quizgame')
    cursorT = mydb.cursor()
    Tabel_type = input("for AdminUser Tabel >>> 'U' \nfor Question Tabel >>> 'Q' \nfor Players Tabel >>> 'P' \n")
    if Tabel_type == "u" or Tabel_type == "U":
        TabelName = input("Enter Tabel Name: ")
        cursorT.execute("CREATE TABLE {} (UserId int primary key, UserName VARCHAR(20), Password VARCHAR(20))".format(TabelName))  # To Create tabel we use this
        mydb.commit()
        print(ColorLab.BOLD + ColorLab.GREEN + 'TABEL Created.' + ColorLab.END)
    elif Tabel_type == "q" or Tabel_type == "Q":
        TabelName = input("Enter Tabel Name: ")
        cursorT.execute("CREATE TABLE {} (Question_No int primary key, Question VARCHAR(200), Difficulty VARCHAR(50),OptionA VARCHAR(30),OptionB VARCHAR(30),OptionC VARCHAR(30),OptionD VARCHAR(30),Correct_Answer VARCHAR(30),Topic_Category VARCHAR(30))".format(TabelName))  # To Create tabel we use this
        mydb.commit()
        print(ColorLab.BOLD + ColorLab.GREEN + 'TABEL Created.' + ColorLab.END)
    elif Tabel_type == "p" or Tabel_type == "P":
        TabelName = input("Enter Tabel Name: ")
        cursorT.execute("CREATE TABLE {} (PlayersName VARCHAR(20), Score VARCHAR(20))".format(TabelName))  # To Create tabel we use this
        mydb.commit()
        print(ColorLab.BOLD + ColorLab.GREEN + 'TABEL Created.' + ColorLab.END)


def DeleteTabel():
    mydb = mysql.connector.connect(host='localhost', user='root', password='dawitsamson123', database='quizgame')
    cursorDT = mydb.cursor()
    TabelName = input("Enter Tabel Name: ")
    Value = TabelName
    cursorDT.execute("DROP TABLE {}".format(Value))  # To delete the Players' table created
    mydb.commit()
    print(ColorLab.BOLD + ColorLab.GREEN + 'TABEL Deleted.' + ColorLab.END)


def InsertPlayer_Score():
    mydb = mysql.connector.connect(host='localhost', user='root', password='dawitsamson123', database='quizgame')
    cursorAdmin = mydb.cursor()
    Data = "INSERT INTO Players VALUES(%s,%s) "
    PlayerName = input("Enter PlayerName: ")
    Score = input("Enter PlayerScore: ")
    Values = (PlayerName, Score)
    cursorAdmin.execute(Data, Values)
    mydb.commit()
    print(ColorLab.BOLD + ColorLab.GREEN + 'Player Score Inserted Manually.' + ColorLab.END)


def UpdatePlayerScore():
    mydb = mysql.connector.connect(host='localhost', user='root', password='dawitsamson123', database='quizgame')
    Score = input("Enter PlayerScore: ")
    PlayerName = input("Enter PlayerName: ")
    queriesSET = "UPDATE Players SET Score = '{}' WHERE PlayersName = '{}'".format(Score, PlayerName)
    cursorSET = mydb.cursor()
    cursorSET.execute(queriesSET)
    mydb.commit()
    print(ColorLab.BOLD + ColorLab.GREEN + 'Player Score Updated.' + ColorLab.END)
