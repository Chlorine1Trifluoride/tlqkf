import random
import time
import string
import subprocess
import menu

strlist = ['G','H','O','L','Y','A','E','U','R','W','D',' ']
#           0   1   2   3   4   5   6   7   8   9   10  11
numlist = [ 1, 6, 3, 3, 2, 11, 9, 2, 8, 3, 10, 11, 4, 2, 7, 11, 5, 8, 6, 11, 0, 5, 4 ]
#           H  E  L  L  O      W  O  R  L   D      Y  O  U      A  R  E      G  A  Y
subprocess.run('clear')
pr = ''
for i in numlist:
    for j in range(50):
        letter = random.choice(string.ascii_letters)
        print( pr + letter, end='\r')
        time.sleep(0.005)
    pr +=strlist[i]
print(pr)
        
