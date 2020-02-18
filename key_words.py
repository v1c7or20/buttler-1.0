
accept_dict = ["yes", "of course", "si", "claro", "sure", "do it"]
decline_dict = ["no", "not really", "detener", "stop"]


def is_in_dict(argument, dictionary):
    if dictionary == "accept":
        for i in accept_dict:
            if i == argument:
                return True
        return False
    else:
        for i in decline_dict:
            if i == argument:
                return True
        return False


