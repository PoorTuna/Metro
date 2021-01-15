# Functions:
def check_mail(email_par):
    # good@exmaple.com
    # nice.something.exmaple@gmail.com
    if email_par == "":
        return False
    else:
        email_par = email_par.split(".")

    if len(email_par) < 2:
        return False

    else:
        if "@" in email_par[-2] and email_par[-2].find("@") != len(email_par[-2]) - 1 and email_par[-2].find("@") != 0:
            return True
        else:
            return False


def check_name_pass(name_par, password_par, file_par, request_type):
    # request_type => 0 = login / 1 = register
    info_exist = False
    file_line = None

    if name_par == "" or password_par == "":
        return False
    else:
        if len(name_par) <= 3 or name_par.isdigit() or len(password_par) < 8:
            return False
        else:
            with open(file_par, "r") as file_handling:
                for file_line in file_handling.readlines():
                    file_line = file_line.split(';')
                    if file_line != "" and len(file_line) == 3:
                        if name_par == file_line[1]:
                            info_exist = True
                            break
                # Conditions for login type:
                if info_exist and request_type == 0 and password_par == file_line[
                    2]:  # User matches database return True
                    return True
                if not info_exist and request_type == 0:
                    return False
                # Conditions for register type:
                if info_exist and request_type == 1:  # User exists in the data base return False
                    return False
                if not info_exist and request_type == 1:
                    return True
