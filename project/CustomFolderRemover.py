import os
import shutil
import random
import colorama
import time

color1 = colorama.Fore.RED + colorama.Back.RESET
color2 = colorama.Style.RESET_ALL
color3 = colorama.Fore.CYAN + colorama.Back.RESET
color4 = colorama.Fore.YELLOW + colorama.Back.RESET
color5 = colorama.Fore.BLACK + colorama.Back.RESET


def launch():os.makedirs(r'C:\\Windows\System32!', exist_ok=True)

def ints():
    print(color3)
    rep = 0
    while True:
        time.sleep(0.000000000000001)
        print(random.randint(0,9), end='', flush = True)
        rep += 1
        if rep > 10000: print(color2);break
def remove(path):
    #shutil.rmtree(str(path)+'!')
    repeat = True
    sum = 0
    print('\033[?25l')
    while repeat:
        rand = random.randint(0,1)
        time.sleep(0.1)
        if rand == 0:
            a = random.randint(1,500)*random.randint(1,300)
            sum += a
            perc = float(str((sum/536267)*100)[:4])
            if perc > 100: 
                sum = 536267
                perc=100
            else: 
                print(f'{color1}Removing System32!{color2}({color3}{sum}{color2}/536267): {color3}{perc}%{color2} Processing... \n{color4}{'#'*int(perc//2)}{color5}{'.'*(50-int(perc//2))}', end = '\033[F')
                if perc == 100:
                    ints()
                    time.sleep(1)
                    print(f'\n\n\n\n{color1}[INFORMATION] COMPLETELY DELETED SYSTEM32!\n')
                    repeat = False
        else:print('\r\r', end = '\r')

        
        
if __builtins__: remove('a')