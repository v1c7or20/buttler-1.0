from pc_comands import *
import time




print("hola mundo")
open_process("firefo")
kill_process("firefo")
current = time.strftime('%H:%M:%S', time.localtime())
print(current)
#block_pc()
