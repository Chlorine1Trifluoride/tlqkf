import subprocess
import sys
import signal
import time
try: import colorama
except ImportError: subprocess.run([sys.executable, '-m', 'pip', 'install', 'colorama'], shell=True)


def handler(signum, frame):print(f'{colorama.Fore.GREEN}[WARNING]{colorama.Fore.LIGHTCYAN_EX} KEYBOARD INTURRUPT is Disaled. Press Ctrl+Shift+C to copy')


signal.signal(signal.SIGINT, handler)

print(colorama.Fore.LIGHTCYAN_EX, '\r')
print('='*10 + '[WINDOWS KILLER]' + '='*10)
time.sleep(10)