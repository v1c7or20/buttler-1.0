from voicecomands import *
import time

action(get_voice_command())
print("hola mundo")
open_process("firefo")
kill_process("firefo")
current = time.strftime('%H:%M:%S', time.localtime())
print(current)
#block_pc()
