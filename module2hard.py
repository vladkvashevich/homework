import random
def dveri():
    shifr = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    win = random.choice(shifr)
    return win

win = dveri()
print(win)
code = []
for i in range(1, win+1):
    for j in range(i+1, win+1):
        if win == i + j or win % (i + j) == 0:
            code.append(i)
            code.append(j)
            continue
print(" win: ", win, " code: ", code)
