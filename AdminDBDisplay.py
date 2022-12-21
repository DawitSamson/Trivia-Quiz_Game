from DBDisplay import *
from SMS import *
# This ia where the AdminUser or User which can check the Admin Detail or Quiz Detail


def MainAdmin():
    AdminOption_Text()
    try:
        Selected = int(input("Your Choice "))
        if Selected == 1:
            AdminDetailMainDB()
        elif Selected == 2:
            AdminQuizMain()
        else:
            Invalid_InputText()
            return MainAdmin()

    except Exception as e:
        print(e)
        Invalid_DetailsText()


def AdminSection():  # This is the function to call on the App Python file
    CheckAdminType = CheckUserTypeDB()
    if CheckAdminType == 1:
        return MainAdmin()
