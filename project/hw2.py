import random
import time
import string
import subprocess
import sys
try: import colorama
except ImportError: 
    subprocess([sys.executable,'-m', 'pip', 'install', 'colorama' ])
    import colorama
print()
print()
strlist = ('G','H','O','L','Y','A','E','U','R','W','D',' ', '[', ']')
#           0   1   2   3   4   5   6   7   8   9   10  11  12    13
numlist = ( 11, 4, 2, 7, 11, 5, 8, 6, 11, 0, 5, 4, 11 )
#               Y  O  U      A  R  E      G  A  Y
#subprocess.run('clear')
pr=colorama.Fore.YELLOW +''
for i in range(25):
    time.sleep(0.01)
    pr+= '='
    print(pr, end='\r')
pr+='['+colorama.Fore.LIGHTCYAN_EX
print(pr, end='\r')
for i in numlist:
    if i == 11:
        pr += strlist[i]
    else: 
        for j in range(20):
            letter = random.choice(string.ascii_letters)
            print( pr + letter, end='\r')
            time.sleep(0.03)
        pr +=strlist[i]
pr+=colorama.Fore.YELLOW + ']'
print(pr, end='\r')
for i in range(0,25):
    time.sleep(0.01)
    pr+= '='
    print(pr, end='\r')
print(colorama.Fore.LIGHTCYAN_EX + '\n \n \n                           뭘 봐 게이야 \n \n' + colorama.Fore.YELLOW)
l=''
for i in range(65):
    time.sleep(0.01)
    l+= '='
    print(l, end='\r')
print('\n')


