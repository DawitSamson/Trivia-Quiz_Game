import mysql.connector as connector
from DesignColors import ColorLab

# On the DB(DataBase) the below are the operations which will be Done using Python programming
'''
        CREATE(DB, TABLES) 
        INSERT(DATA)
        READ(SELECT DATA)
        UPDATE(DATA)
        DELETE(DATA)
'''


class MySql_Main_DB:
    def __init__(self):
        self.mydb = connector.connect(host='localhost', user='root', password='dawitsamson123', database='quizgame')


class DBAdmin(MySql_Main_DB):
    def __init__(self):
        super().__init__()

    # Inserting Data to Database
    def Insert_AdminUser(self, userid, username, password):
        queries = "INSERT INTO Users VALUES({},'{}','{}')".format(userid, username, password)
        cursor = self.mydb.cursor()
        cursor.execute(queries)
        # Commit means changing in database physically or really.
        # if we don't use commit() then it will only show output in cmd but the real db did not get changed.
        # That's why we have to use commit
        self.mydb.commit()
        print(ColorLab.BOLD + ColorLab.YELLOW + 'The User Saved To Database' + ColorLab.END)

    # Fetch ALL User From Database
    def Display_All_Users(self):
        queries = 'SELECT * FROM Users'
        cursor = self.mydb.cursor()
        cursor.execute(queries)
        for row in cursor:
            print('User Id: ', row[0])
            print('User Name: ', row[1])
            print('Password:', row[2])
            print()

    # Fetch one User From Database
    def Display_One_User(self, idnum):
        queries = 'SELECT * FROM Users WHERE UserId={}'.format(idnum)
        cursor = self.mydb.cursor()
        cursor.execute(queries)
        for row in cursor:
            print('\nUser Id: ', row[0])
            print('User Name: ', row[1])
            print('Password:', row[2])
            print("\n")

    # Delete User from Database
    def delete_user(self, idnum):
        queries = 'DELETE FROM Users WHERE UserId={}'.format(idnum)
        cursor = self.mydb.cursor()
        cursor.execute(queries)
        self.mydb.commit()
        print(ColorLab.BOLD + ColorLab.RED + 'User Record deleted from the database' + ColorLab.END)

    # Update username and password on the Database
    def update_user(self, Userid, NewName, Newpassword):
        queries = "UPDATE Users set UserName = '{}', Password = '{}' WHERE UserId ={}".format(NewName,
                                                                                              Newpassword, Userid)
        cursor = self.mydb.cursor()
        cursor.execute(queries)
        self.mydb.commit()
        print(ColorLab.BOLD + ColorLab.GREEN + 'User Record Updated.' + ColorLab.END)

    # Check the user type Admin or Guest(User)
    def check_user(self, username, password):
        queries = "SELECT * FROM Users WHERE UserName ='{}' AND Password='{}'".format(username, password)
        cursor = self.mydb.cursor()
        cursor.execute(queries)
        for row in cursor:
            print('Welcome user: ', row[1])
            return 1
            # break
        else:
            print(ColorLab.BOLD + ColorLab.RED + '\t\t\t\t\t\t\t Invalid user!' + ColorLab.END)
            return 0


class QuestionAdminDB(MySql_Main_DB):
    def __init__(self):
        super().__init__()

    # Insert Quiz Question
    def Insert_Question(self, QuestionNo, Question, Difficulty, OptionA, OptionB, OptionC, OptionD, Answer, Topic):
        queries = "INSERT INTO Questions VALUES({},'{}','{}','{}','{}','{}','{}','{}','{}')".format(QuestionNo,
                                                                                                    Question,
                                                                                                    Difficulty, OptionA,
                                                                                                    OptionB, OptionC,
                                                                                                    OptionD, Answer,
                                                                                                    Topic)
        cursor = self.mydb.cursor()
        cursor.execute(queries)
        self.mydb.commit()
        print(ColorLab.BOLD + ColorLab.GREEN + 'New Question Saved To database' + ColorLab.END)

    # Display all Quiz
    def fetch_question(self):
        queries = 'SELECT * FROM Questions'
        cursor = self.mydb.cursor()
        cursor.execute(queries)
        for row in cursor:
            print('Question No: ', row[0])
            print('Question: ', row[1])
            print('Difficulty: ', row[2])
            print('Topic Name: ', row[8])
            print('Option 1: ', row[3])
            print('Option 2: ', row[4])
            print('Option 3: ', row[5])
            print('Option 4: ', row[6])
            print('Answer: ', row[7], "\n\n")


class ShowUserScore(MySql_Main_DB):
    # in this class we will Going to show the Top score player descending order (From top to bottom)
    def __init__(self):
        super().__init__()
        queriesShow = 'SELECT PlayersName,Score FROM Players ORDER BY Score DESC'
        # queriesShow = 'SELECT PlayersId,PlayersName,Score FROM Players ORDER BY Score DESC'
        cursorShow = self.mydb.cursor()
        cursorShow.execute(queriesShow)
        for rowShow in cursorShow:
            print(ColorLab.BOLD + ColorLab.YELLOW + 'Player Name: ' + ColorLab.END, rowShow[0])
            print(ColorLab.BOLD + ColorLab.YELLOW + '      Score: ' + ColorLab.END, rowShow[1])
            print()


class UserMainDB(MySql_Main_DB):
    def __init__(self):
        super().__init__()

    def Display_Question(self):
        PlayersName = input("Enter Your First Name: ")
        queryCatagory = 'SELECT DISTINCT(Topic_Category) FROM Questions'
        cursorCatagory = self.mydb.cursor()
        cursorCatagory.execute(queryCatagory)
        # Ask the user to select the topic
        print('Please select Topic for Your Question')
        for Catagory in cursorCatagory:
            print(ColorLab.BOLD, ColorLab.MAGENTA + Catagory[0] + ColorLab.END)
        TopicSelect = input('Write The Topic: ')
        print()
        queriesTopicCatgory = 'SELECT * FROM Questions WHERE Topic_Category="{}"'.format(TopicSelect)
        cursorTopicCatgory = self.mydb.cursor()
        cursorTopicCatgory.execute(queriesTopicCatgory)
        NetScore = 0
        for rowTopic in cursorTopicCatgory:
            print(ColorLab.BOLD + ColorLab.PURPLE + 'Question:', rowTopic[0], ':- ', rowTopic[1])
            print(ColorLab.BOLD + ColorLab.YELLOW + 'Option (1): ', ColorLab.BOLD + ColorLab.BLUE + rowTopic[3], "   ",
                  ColorLab.BOLD + ColorLab.YELLOW + 'Option (2): ', ColorLab.BOLD + ColorLab.BLUE + rowTopic[4], "   ",
                  ColorLab.BOLD + ColorLab.YELLOW + 'Option (3): ', ColorLab.BOLD + ColorLab.BLUE + rowTopic[5], "   ",
                  ColorLab.BOLD + ColorLab.YELLOW + 'Option (4): ', ColorLab.BOLD + ColorLab.BLUE + rowTopic[6],
                  ColorLab.END)
            CorrectAnswer = int(input(ColorLab.BOLD + ColorLab.GREEN + 'Enter the Correct Option: ' + ColorLab.END))
            print()
            # in this we will give the point for topic which are easy "2 point" and for others (hard) it will be "5 points"
            if rowTopic[2].lower() == 'easy':  # ..............difficulty level of the question
                if str(CorrectAnswer) == rowTopic[7]:
                    NetScore += 2  # points
            else:
                if str(CorrectAnswer) == rowTopic[7]:
                    NetScore += 5  # points
        Score = NetScore
        queryplayer = "INSERT INTO Players VALUES('{}','{}')".format(PlayersName, Score)
        cursorplayer = self.mydb.cursor()
        cursorplayer.execute(queryplayer)
        self.mydb.commit()
        print(ColorLab.BOLD + ColorLab.YELLOW + '\n\t\t\t\t\t***********YOUR RESULT***********' + ColorLab.END)
        print(ColorLab.BOLD + ColorLab.DARKCYAN + "\t\t\t\t\tNAME: " + ColorLab.END, PlayersName)
        print(ColorLab.BOLD + ColorLab.GREEN + "\t\t\t\t\tScore: " + ColorLab.END, NetScore)
        print(ColorLab.BOLD + ColorLab.GREEN + "\t\t\t\t\tTopic_Catagory: " + ColorLab.END, TopicSelect)
        print()

        # Ask the user to see the answer for the questions
        went = input('Do you went to see Solution? Press 0 to exit | Press 1/any key to see Solution: ')
        if went != "0":
            queryWent = 'SELECT * FROM Questions WHERE Topic_Category="{}"'.format(
                TopicSelect)  # from the topic selected display
            cursorWent = self.mydb.cursor()
            cursorWent.execute(queryWent)
            print()
            print(ColorLab.BOLD + ColorLab.BLUE + "The Correct Answer are" + ColorLab.END)
            for RowWent in cursorWent:
                print(ColorLab.BOLD + ColorLab.PURPLE + 'Que:', RowWent[0], ':- ', 'Question:', RowWent[1])
                print(ColorLab.BOLD + ColorLab.YELLOW + 'Option 1: ' + ColorLab.END, RowWent[3])
                print(ColorLab.BOLD + ColorLab.YELLOW + 'Option 2: ' + ColorLab.END, RowWent[4])
                print(ColorLab.BOLD + ColorLab.YELLOW + 'Option 3: ' + ColorLab.END, RowWent[5])
                print(ColorLab.BOLD + ColorLab.YELLOW + 'Option 4: ' + ColorLab.END, RowWent[6])
                print(ColorLab.BOLD + ColorLab.GREEN + 'Answer For the Question is :' + ColorLab.END,
                      RowWent[7] + "\n")
