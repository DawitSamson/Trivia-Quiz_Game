from AdminDBDisplay import *
from DBDisplay import *
from SMS import *



def MainFunction():
    while True:
        HomePage_WelcomeText()
        try:
            n = int(input('Enter Your Choice: '))
            if n == 1:
                Topics()
            elif n == 2:
                AllUserDB()
            elif n == 3:
                UserSection()
            elif n == 4:
                AdminSection()
            elif n == 5:
                ThankYouText()
                break
            else:
                Invalid_InputText()
        except Exception as e:
            print(e)
            Invalid_DetailsText()


