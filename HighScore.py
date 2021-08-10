def game():
    return 5769

score=game()

with open("highscore.txt") as h:
    r=int(h.read())

if score>r:
    with open('highscore.txt','w') as a:
        b=a.write(str(score))