import random as rand
# ------------------ CONTEXT ---------------------
#   Write a python program that do the following:

    #1. display the initial content of the array
    #2. display a menu of options
    #3. allow user to select item in the menu (check if valid)
    #4. perform the selected option (you may prompt additional info to user when need)
    #5. display the resulting values of the array

# Note: 
#  The program has an array variable containing 10 random numbers
#  You may add other options and features

def InputValidator(EvalueeStr): # Checks Input Eligibility - Separate Function for non-Numeric Input
    if (EvalueeStr.isalpha() == True) or (EvalueeStr.isalnum() == True):
        print(f"{Red}Input must only be a number!{End}")
        return "not valid"
    elif (EvalueeStr.isspace() == True) or (EvalueeStr == None) or (EvalueeStr == ""):
        print(f"{Red}You've typed in an empty value! Please enter a number{End}")
        return "not valid"
    elif " " in EvalueeStr:
        print(f"{Red}Inputs must not have a space!{End}")
        return "not valid"
    elif EvalueeStr.replace("-", "").replace(".", "").isnumeric() == True:
        return "valid"
    else:
        print(f"{Red}Invalid input format. Allowable inputs are positive integer, decimal, and negatives only{End}")
        return "not valid"

Red = "\33[91m" # Decorative Variable Group
Grn = "\33[92m"
Yllw = "\33[93m"
Blue = "\33[94m"
BBlue = "\u001b[34;1m"
End = "\33[0m"
Itlc = "\33[3m"
Bldtxt = "\33[1m"
DCyan = "\u001b[36;1m"
Cyan = "\u001b[36"

_list = []
while len(_list) < 10:
    list_item = rand.randint(1, 100)
    _list.append(list_item)

print("\n",f"Welcome to \33[41m{Bldtxt} List Methods {End}!".center(71, " "), "\n","━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━".center(60, " "),"\n", f"Feel free to {Red}explore{End} the program {Grn}features{End}!".center(77, " "), "\n", f"Manipulate the below list at {Blue}will{End}.".center(69, " "),"\n","\n", f"{_list}".replace("[","").replace("]","").center(60, " "),"\n","\n",f"{Blue}{Itlc}Choose an action from the menu{End}:")

print("\n","\n",f"\33[44m{Bldtxt}        Menu        {End}".center(71, " "),
f"\n\n   Type '{Grn}1\33[0m' or '{Grn}add\33[0m' to add an element.\n   Type '{Red}2\33[0m' or '{Red}delete\33[0m' to delete an element.\n   Type '{Blue}3\33[0m' or '{Blue}mod\33[0m' to modify/change an element.\n   Type '{BBlue}4\33[0m' or '{BBlue}insert\33[0m' to specifically place an element.\n   Type '{DCyan}5\33[0m' or '{DCyan}descend\33[0m' to arrange values in descending order.\n   Type '{Yllw}6\33[0m' or '{Yllw}ascend\33[0m' to arrange values in ascending order.")

while True:
    choices_ = ["1", "2", "3", "4", "5", "6", 'add', 'delete', 'mod', 'insert', 'descend', 'ascend']
    Usr_Decision = input("\n> ").lower()
    if Usr_Decision in choices_:
        if (Usr_Decision == choices_[0]) or (Usr_Decision == choices_[6]):
            print(f"{Grn}{Itlc}What would you like to append?{End}")
            add_val = input("\n> ")
            Action_1 = InputValidator(add_val)
            if Action_1 == "valid":
                if ("-" in add_val) and ("." in add_val):
                    updateval = float(add_val)
                    _list.append(updateval)
                elif ("-" not in add_val) and ("." in add_val):
                    updateval = float(add_val)
                    _list.append(updateval)
                elif ("-" in add_val) and ("." not in add_val):
                    updateval = int(add_val)
                    _list.append(updateval)
                else:
                    updateval = int(add_val)
                    _list.append(updateval)
            print(_list)
            break
        if (Usr_Decision == choices_[1]) or (Usr_Decision == choices_[7]):
            print(f"{Red}{Itlc}What would you like to remove?{End}")
            rem_val = input("\n> ")
            if (("." in rem_val) and ("-" in rem_val)):
                update_val = float(rem_val)
                if rem_val in _list:
                    _list.remove(update_val)
                else:
                    print(f"{Red}The list doesn't contain the specified value.{End}")
            if "." in rem_val:
                update_val = float(rem_val)
                if rem_val in _list:
                    _list.remove(update_val)
                else:
                    print(f"{Red}The list doesn't contain the specified value.{End}")
            else:
                update_val = int(rem_val)
                if rem_val in _list:
                    _list.remove(update_val)
                else:
                    print(f"{Red}The list doesn't contain the specified value.{End}")
            print(_list)
            break
        if (Usr_Decision == choices_[2]) or (Usr_Decision == choices_[8]):
            print(f"{Red}{Itlc}What would you like to modify/replace?{End}")
            mod_val = input("\n> ")
            if (("." in mod_val) and ("-" in mod_val)):
                update_val = float(mod_val)
                if update_val in _list:
                    modvar = _list.index(update_val)
                    print(f"{Red}{Itlc}Enter a replacement value{End}")
                    new_val = input("\n> ")
                    if (("." in new_val) and ("-" in new_val)):
                        newerval = float(new_val)
                        _list[modvar] = newerval
                    elif "." in new_val:
                        newerval = float(new_val)
                        _list[modvar] = newerval
                    else:
                        newerval = int(new_val)
                        _list[modvar] = newerval
                else:
                    print(f"{Red}The list doesn't contain the specified value.{End}")
            if "." in mod_val:
                update_val = float(mod_val)
                if update_val in _list:
                    modvar = _list.index(update_val)
                    print(f"{Red}{Itlc}Enter a replacement value{End}")
                    new_val = input("\n> ")
                    if (("." in new_val) and ("-" in new_val)):
                        newerval = float(new_val)
                        _list[modvar] = newerval
                    elif "." in new_val:
                        newerval = float(new_val)
                        _list[modvar] = newerval
                    else:
                        newerval = int(new_val)
                        _list[modvar] = newerval
                else:
                    print(f"{Red}The list doesn't contain the specified value.{End}")
            else:
                update_val = int(mod_val)
                if update_val in _list:
                    modvar = _list.index(update_val)
                    print(f"{Red}{Itlc}Enter a replacement value{End}")
                    new_val = input("\n> ")
                    if (("." in new_val) and ("-" in new_val)):
                        newerval = float(new_val)
                        _list[modvar] = newerval
                    elif "." in new_val:
                        newerval = float(new_val)
                        _list[modvar] = newerval
                    else:
                        newerval = int(new_val)
                        _list[modvar] = newerval
                else:
                    print(f"{Red}The list doesn't contain the specified value.{End}")
            print(_list)
            break
        if (Usr_Decision == choices_[3]) or (Usr_Decision == choices_[9]):
            print("ins")
            break
        if (Usr_Decision == choices_[4]) or (Usr_Decision == choices_[10]):
            print("desc")
            break
        if (Usr_Decision == choices_[5]) or (Usr_Decision == choices_[11]):
            print("asc")
            break