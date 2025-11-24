import subprocess
import sys
import signal
import time
import os
import CustomFolderRemover as cfr
try: import colorama
except ImportError: subprocess.run([sys.executable, '-m', 'pip', 'install', 'colorama'], shell=True)


def handler(signum, frame):print(f'{colorama.Fore.GREEN}[WARNING]{colorama.Fore.LIGHTCYAN_EX} KEYBOARD INTURRUPT is Disaled. Press Ctrl+Shift+C to copy')


signal.signal(signal.SIGINT, handler)

print(colorama.Fore.LIGHTCYAN_EX)
print('='*10 + '[ System Auto Task ]' + '='*10)

if input("Press Enter to Start... ") !=  None: pass



print(colorama.Fore.YELLOW, '\r')
print('='*10 + '[ DELETE System32! ]' + '='*10)
# time.sleep(10)
print(colorama.Fore.RED, '\r')
print(f'{colorama.Fore.BLACK}{colorama.Back.LIGHTGREEN_EX}[WARNING]{colorama.Fore.GREEN}{colorama.Back.RESET} This action will DELETE C:\\Windows\System32!')
print(f'{colorama.Fore.BLACK}{colorama.Back.LIGHTGREEN_EX}[WARNING]{colorama.Fore.GREEN}{colorama.Back.RESET} DELETING C:\\Windows\System32 causes your Windows to be COMPLETELY COLLAPSE!!')

print('\n')
#os.makedirs(r'C:\\Windows\System32!')
