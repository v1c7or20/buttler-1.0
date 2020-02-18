import subprocess
import psutil
import os
from bot_actions import *
from key_words import *


def open_process(process_name):
    try:
        subprocess.call([str(process_name)])
    except ValueError as err:
        bot_negative(process_name)
        pass


def kill_process(process_name):
    for process in psutil.process_iter(["name", "exe", "cmdline"]):
        if process.info['name'] == str(process_name):
            process.terminate()
            bot_aproval(process_name)
            break
    bot_not_encounter(process_name)
    return 0


def block_pc():
    try:
        os.system("systemctl suspend")
    except ValueError as err:
        bot_negative("block")


def turn_of_pc(argument, answer):
    try:
        if alert(answer):
            if argument == "now":
                os.system("shutdown now")
            elif argument == "reboot":
                os.system("shutdown -r")
            elif argument == "":
                os.system("shutdown")
            else:
                bot_not_encounter(argument)
        else:
            bot_aproval(argument)
    except ValueError as err:
        bot_cancel_process(err)


def reboot(answer):
    try:
        if alert(answer):
            os.system("reboot")
        else:
            bot_cancel_process("reboot")
    except ValueError as err:
        bot_cancel_process(err)


def alert(answer):
    if is_in_dict(answer, "accept"):
        return True
    elif is_in_dict(answer, "decline"):
        return False
    else:
        raise ValueError("Answer given is not currently recognized")
