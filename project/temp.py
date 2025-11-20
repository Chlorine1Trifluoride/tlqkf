import colorama

forecolor=[colorama.Fore.RESET, colorama.Fore.RED, colorama.Fore.LIGHTRED_EX, colorama.Fore.BLUE, colorama.Fore.LIGHTBLUE_EX, colorama.Fore.GREEN, colorama.Fore.LIGHTGREEN_EX, colorama.Fore.BLACK, colorama.Fore.LIGHTBLACK_EX, colorama.Fore.WHITE, colorama.Fore.LIGHTWHITE_EX, colorama.Fore.CYAN, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.MAGENTA, colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.YELLOW, colorama.Fore.LIGHTYELLOW_EX]

backcolor=[colorama.Back.RESET, colorama.Back.RED, colorama.Back.LIGHTRED_EX, colorama.Back.BLUE, colorama.Back.LIGHTBLUE_EX, colorama.Back.GREEN, colorama.Back.LIGHTGREEN_EX, colorama.Back.BLACK, colorama.Back.LIGHTBLACK_EX, colorama.Back.WHITE, colorama.Back.LIGHTWHITE_EX, colorama.Back.CYAN, colorama.Back.LIGHTCYAN_EX, colorama.Back.MAGENTA, colorama.Back.LIGHTMAGENTA_EX, colorama.Back.YELLOW, colorama.Back.LIGHTYELLOW_EX]

style=[colorama.Style.NORMAL, colorama.Style.BRIGHT, colorama.Style.DIM]
for i in backcolor:

    for j in forecolor:
            
            for k in style:
                  print(i+j+k+'ABC', end=' ')
