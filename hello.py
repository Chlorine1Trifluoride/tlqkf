import menu, HEIL
blacklist = []
class person():
    def __init__(self, name):
        self.name = name
        blacklist.append(self)
    def question(self):
        menu.box("[ OX 퀴즈 ]", [f"{self.name}은(는) 병신입니까?"])
        ans = str(input("답안을 입력하시오. [O/X]: "))
        if ans == "O" or ans == "o": return True
        elif ans == "X" or ans == "x": return False
        else: return None
def quiz(b):
    a = person(str(b))
    ans = a.question()
    if ans == True: HEIL.correct(a.name)
    elif ans == False: print("지랄하네 좆병신새끼가")
    elif ans == None: print("제대로 입력해라 좆병신새끼야")
    else: print("어 씨발 터졌다")