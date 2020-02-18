import subprocess
import psutil
import os
import time
from bot_actions import *
from key_words import  *


def open_process(process_name):
    try:
        subprocess.call([str(process_name)])
    except:
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
    except:
        bot_negative("block")


def turn_of_pc(argument):
    current_time = time.strftime('%H:%M:%S', time.localtime())
    if argument == "now":
        os.system("shutdown now")
    elif argument == "reboot":
        os.system("shutdown -r")
    elif argument == "":
        os.system("shutdown")
    else:
        bot_not_encounter(argument)


def alert(argument):
    if is_in_dict(argument, "accept"):
        return True
    elif is_in_dict(argument, "decline"):
        return False
    else:
        raise ValueError("Answer given is not currently recognized")
