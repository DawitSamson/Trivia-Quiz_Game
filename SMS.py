from DesignColors import ColorLab
import pyfiglet as pyg


# This is a library for all SMS/ Text Displayed Found on this Project.


def HomePage_WelcomeText():
    digital_format = pyg.figlet_format("WELCOME TO DAWIT TRIVIA QUIZ APP", font="digital")
    print(ColorLab.BOLD + ColorLab.GREEN + digital_format + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.MAGENTA + 'Please Choose Which Section You Went To Visit' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + "\t\t\t1. TOPIC'S and CATEGORY'S MENU" + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + '\t\t\t2. TOP PLAYERS' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + '\t\t\t3. USER ' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + '\t\t\t4. ADMIN' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + '\t\t\t5. EXIT' + ColorLab.END)


def AdminSection_WelcomeText():
    digital_format = pyg.figlet_format("WELCOME TO ADMIN DB SECTION", font="digital")
    print(ColorLab.BOLD + ColorLab.MAGENTA + digital_format + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 1 To INSERT NEW User.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 2 To DISPLAY ONE User.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 3 To DISPLAY All User.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 4 To DELETE USER.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 5 To UPDATE User.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 6 To CREATE DATABASE.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 7 To CREATE TABEL.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 8 To Delete TABEL.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 9 To INSERT USER SCORE MANUALLY.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 10 To UPDATE PLAYER SCORE.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 11 HOMEPAGE.\n' + ColorLab.END)


def AdminQuestionSection_WelcomeText():
    digital_format = pyg.figlet_format("WELCOME To ADMIN QUIZ SECTION", font="digital")
    print(ColorLab.BOLD + ColorLab.MAGENTA + digital_format + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 1 To PRINT EXISTING QUESTION.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 2 To INSERT NEW QUESTION.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 3 To HOMEPAGE.' + ColorLab.END)


def AdminOption_Text():
    print((ColorLab.BOLD + ColorLab.YELLOW + 'Please Choose Your Detail Area To Work' + ColorLab.END))
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press (1) For Admin Details \n Press (2) For Quiz Details ' + ColorLab.END)


def UserSection_WelcomeText():
    digital_format = pyg.figlet_format("WELCOME To PLAYER QUIZ SECTION", font="digital")
    print(ColorLab.BOLD + ColorLab.YELLOW + digital_format + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 1 To View The Instruction: ' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 2 To Play The Game: ' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.DARKCYAN + 'Press 3 To HOMEPAGE.\n' + ColorLab.END)


def General_InstructionText():
    digital_format = pyg.figlet_format("GENERAL INSTRUCTIONS:", font="digital")
    print(ColorLab.BOLD + ColorLab.DARKCYAN + digital_format + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.WHITE + '\t\t\t1.Each Question has Multiple-Choice Questions.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.WHITE + '\t\t\t2.Each Question has 4 options.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.WHITE + '\t\t\t3.Read Each Question and Answer carefully before choice your answer.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.WHITE + '\t\t\t4.Choice The Best Answer.' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.WHITE + '\t\t\t5.Use Your Name For Registration' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.GREEN + '\t\t\t************************ BEST OF LUCK 👍👍👍👍 ************************.' + ColorLab.END)


def Question_TopicText():
    digital_format = pyg.figlet_format("QUIZ OVERALL TOPIC", font="digital")
    print(ColorLab.BOLD + ColorLab.MAGENTA + digital_format + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.YELLOW + '\t\t\t1.CITY' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.YELLOW + '\t\t\t2.SPORT' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.YELLOW + '\t\t\t3.MOVIE' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.YELLOW + '\t\t\t4.TECHNOLOGY' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.YELLOW + '\t\t\t5.IQ' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.YELLOW + '\t\t\t6.GENERAL KNOWLEDGE' + ColorLab.END)
    print(ColorLab.BOLD + ColorLab.YELLOW + '\t\t\t7.HISTORY' + ColorLab.END)


def Invalid_InputText():
    print(ColorLab.BOLD + ColorLab.RED + '\t\t\t\t\t\t\tInvalid Input Please Try again.\n' + ColorLab.END)


def Invalid_DetailsText():
    print(ColorLab.BOLD + ColorLab.RED + '\t\t\t\t\t\t\tInvalid Details Please Try again.\n' + ColorLab.END)


def ThankYouText():
    print(ColorLab.BOLD + ColorLab.YELLOW + '\n\t\t\t\t\t\tThank You For Your Time. \n' + ColorLab.END)
