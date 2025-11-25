# 엥? 소스 코드를 보다니...
# 고작 고1따리가 만든 코드인데...
# 쫄았나...?

import subprocess
import sys
import signal
import time
import os
import CustomFolderRemover as cfr
import shutil
try: import colorama
except ImportError: subprocess.run([sys.executable, '-m', 'pip', 'install', 'colorama'], shell=True)

#if os.name == 'nt':
time.sleep(0.3)
print(colorama.Fore.GREEN + colorama.Back.BLACK + colorama.Style.DIM + 'Please wait. Process starting... \r')
time.sleep(0.5)
print(colorama.Style.RESET_ALL)
#else: print("뭐야.... 윈도우에서 다시 실행하세요")          

def timer(t) : 
    time.sleep(t)
    return True
def handler(signum, frame):print(f'{colorama.Fore.GREEN}[WARNING]{colorama.Fore.LIGHTCYAN_EX} KEYBOARD INTURRUPT is Disaled. Press Ctrl+Shift+C to copy' + colorama.Back.BLACK)


signal.signal(signal.SIGINT, handler)

print(colorama.Fore.LIGHTCYAN_EX)
print('='*10 + '[ System Auto Task ]' + '='*10)
print('\n')
print('본 코드는 재미를 위하여 제작되었으며 시스템에 어떠한 위해도 가하지 않음을 알려드립니다.')
print('\n\n')
if input("Press Enter to Start... ") !=  None: pass
print('\n\n\n\n\n\n\n\n\n')
print(colorama.Fore.YELLOW)
print('='*10 + '[ DELETE System32! ]' + '='*10)
time.sleep(1)
print(colorama.Fore.RED, '\r')
print(f'{colorama.Fore.BLACK}{colorama.Back.LIGHTYELLOW_EX}[WARNING]{colorama.Fore.YELLOW}{colorama.Back.RESET} This action will DELETE {os.path.join('C','Windows','System32!')}\n')
print(f'{colorama.Fore.BLACK}{colorama.Back.LIGHTYELLOW_EX}[WARNING]{colorama.Fore.YELLOW}{colorama.Back.RESET} DELETING {r'C\\\Windows\\System32'} causes your Windows to be COMPLETELY COLLAPSE!!')

print('\n\n\n\n')
print('Would You REALLY Continue?')
if input("Y/N: ") != None: print(colorama.Fore.GREEN + '\n\n')
print("If You REALLY UNDERSTAND the RISK of this task, Press Enter...\n")
if  timer(3): pass
cfr.launch()
print(colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + "THIS IS THE LAST CHANCE. UNLESS YOU SERIOUSLY DO NOT WANT TO STOP IT, NEVER PRESS ENTER...")
if  timer(5): print(colorama.Style.RESET_ALL)
cfr.remove(os.path.join(r'C','Windows', 'System32'))
print('\n\n\n\n\n')
print(colorama.Style.NORMAL + colorama.Back.RESET + colorama.Fore.LIGHTCYAN_EX + '지금까지 정말 순수 장난이였습니다. 당신의 시스템은 안전합니다. 쩔죠? \n\n')
time.sleep(3)
print(colorama.Style.RESET_ALL)
print(r"""
Traceback (most recent call last):
  File "/workspaces/tlqkf/project/danger.py", line 523, in <module>
    shutil.rmtree(r'C:\\Windows\System32') #FATAL EXECUTION
    ^^^^^^
NameError: name 'shutil' is not defined. Did you forget to import 'shutil'?      
""")
print(colorama.Fore.LIGHTCYAN_EX + '어라?')
print(colorama.Style.RESET_ALL)
time.sleep(8)
try: subprocess.run('cls')
except: subprocess.run('clear')
print(colorama.Style.RESET_ALL)
print('당신의 시스템은 정말로 안전합니다.')
if input('Press Enter to EXIT...')!= None: pass