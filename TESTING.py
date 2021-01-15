# email = "oren@a.com"
# def check_mail(email):
#     # good@exmaple.com
#     # nice.something.exmaple@gmail.com
#     if email == "":
#         return False
#     else:
#         email = email.split(".")
#
#     if len(email) < 2:
#         return False
#
#     else:
#         print email[-2]
#         if "@" in email[-2] and email[-2].find("@") != len(email[-2]) - 1 and email[-2].find("@") != 0:
#             return True
#         else:
#             return False


def check_name_pass(name_par, password_par, file_par, request_type):
    # request_type => 0 = login / 1 = register
    info_exist = False
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
                if info_exist and request_type == 0 and password_par == file_line[2]:  # User matches database return True
                    return True
                if not info_exist and request_type == 0:
                    return False
                # Conditions for register type:
                if info_exist and request_type == 1:  # User exists in the data base return False
                    return False
                if not info_exist and request_type == 1:
                    return True


print check_name_pass("poortuna", "12345678", "user_data.data", 0)
