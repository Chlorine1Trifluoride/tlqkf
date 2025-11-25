import os
import shutil
import random
import colorama
import time

colorset = colorama.Style.RESET_ALL
color1 = colorset + colorama.Fore.YELLOW
color2 = colorset
color3 = colorset + colorama.Fore.CYAN
color4 = colorset + colorama.Fore.LIGHTBLACK_EX + colorama.Style.BRIGHT
color5 = colorset + colorama.Fore.BLACK + colorama.Style.DIM
color6 = colorset + colorama.Fore.GREEN
color7 = colorset + colorama.Fore.MAGENTA
color8 = colorset + colorama.Fore.GREEN + colorama.Style.DIM


def launch():os.makedirs(os.path.join('C','Windows','System32!'), exist_ok=True)
def nums(period,count):
    rep = 0
    while True:
        time.sleep(period)
        print(random.randint(0,1), end='', flush = True)
        rep += 1
        if rep > count: break
def ints():
    print(color8+'\n\n')
    nums(0.5, 3)
    nums(0.2, 10)
    nums(0.1, 17)
    nums(0.02, 30)
    nums(0.005, 100)
    nums(0.001, 200)
    nums(0.0005, 300)
    nums(0.0001, 500)
    nums(0.00001, 30000)
    nums(0.0001, 500)
    nums(0.001, 200)
    nums(0.02, 30)
    nums(0.1, 20)
    nums(0.5, 3)
    
    nums
    print(color2)
def remove(path):
    shutil.rmtree(str(path)+'!')
    repeat = True
    sum = 0
    print('\033[?25l')
    while repeat:
        rand = random.randint(0,3)
        time.sleep(0.05)
        if rand == 0:print('\r\r', end = '\r')
        else:
            a = random.randint(1,150)*random.randint(1,300)
            sum += a
            perc = float(str((sum/536267)*100)[:5])
            if perc > 100: 
                sum = 536267
                perc=100
            else: 
                print(f'{color1}Removing System32!{color2}({color3}{sum}{color2}/536267): {color3}{perc}%{color2} Processing... \n{color4}{'#'*int(perc//2)}{color5}{'.'*(50-int(perc//2))}\r', end = '\033[F')
                if perc == 100:
                    print(f'{color1}Removing System32!{color2}({color3}536267{color2}/536267): {color3}100%{color2} Processing... \n{color4}{'#'*50}\r', end = '\033[F')
                    time.sleep(2)
                    ints()
                    time.sleep(2)
                    print(f'\n\n\n\n{color1}[INFORMATION] COMPLETELY DELETED SYSTEM32!\n')
                    time.sleep(3)
                    repeat = False
    print(f'        {color6}/\\{color4}  I am not Anonymous.')
    time.sleep(0.5)
    print(f'       {color6}/  \\{colorset}')
    time.sleep(0.5)
    print(f'      {color6}/    \\{color4}  I am not Legion.')
    time.sleep(0.5)
    print(f'     {color6}/      \\{colorset}')
    time.sleep(0.5)
    print(f'    {color6}/ {color8}/‾‾‾‾\\{color6} \\{color4}  I am not forgiven.')
    time.sleep(0.5)
    print(f'   {color6}/ {color8}<  {color7}(){color8}  >{color6} \\{colorset}')
    time.sleep(0.5)
    print(f'  {color6}/   {color8}\\____/{color6}   \\{color4}  I am not forgotten.')
    time.sleep(0.5)
    print(f' {color6}/              \\{colorset}')
    time.sleep(0.5)
    print(f'{color6}/________________\\{color4}  plz dont Expect ME.')
    time.sleep(5)
    print('\033[?25h')

'''
if __builtins__: 
    if input('') != False: remove('C')
'''