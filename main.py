import subprocess
import psutil


def bot_negative(error_encounter):
    return 0


def bot_aproval(program_done):
    return 0


def bot_not_encounter(process_name):
    return 0


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
            bot_aproval()
            break
    bot_not_encounter(process_name)
    return 0


print("hola mundo")
open_process("firefo")
kill_process("firefo")
