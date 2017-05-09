def To_Bool(arg):
    a = arg.lower()
    if a == "y" or a == "yes" or a == "true" or a == "affirmative":
        return True
    elif a == "n" or a == "no" or a == "false" or a == "negative":
        return False
    else:
        return None


def print_text(text, end="\n"):
    if text is not None:
        print(text, end=end)


def Prompt(text=None, confirm=False):
    # the token used to show player input
    end="\n"
    token = "> "
    confirmed = False

    # ask the user to confirm their choice
    if confirm:
        while not confirmed:
            print_text(text)
            action = input(token)
            print("\"%s\"? Is this correct? " % action, end="")
            confirmed = Prompt_Bool()
    # simple dialog
    else:
        print_text(text, end=end)
        action = input(token)

    return action


def Prompt_Bool():
    result = None
    while result is None:
        result = To_Bool(Prompt(text="[Y/n]"))
    return result


def Get_Name():
    name = None
    while name is None:
        name = Prompt(text="Please tell me your name.", confirm=True)
        # basic input validation
        if len(name) == 0:
            name = None
            continue
        if name[0] == " ":
            name = None
            continue

    return name
