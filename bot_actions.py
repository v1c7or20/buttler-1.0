import pyttsx3

engine = pyttsx3.init()


def bot_negative(error_encounter):
    engine.say('Could not realize ' + error_encounter)
    engine.runAndWait()
    pass


def bot_aproval(program_done):
    engine.say('Command execution ' + program_done + ' completed')
    engine.runAndWait()
    pass


def bot_not_encounter(process_name):
    engine.say('Not encounter ' + process_name)
    engine.runAndWait()


def bot_cancel_process(process_name):
    pass


def bot_not_found_process(process_name):
    pass
