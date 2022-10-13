# menghitung presentase kemenangan klub sepak bola
clubName = input('Club Name  : ')
win = input('Win Total  : ')
draw = input('Draw Total : ')
lose = input('Lose Total : ')
print('--------------------------------')
print()

# print inputan
print('Club Name    : ',clubName)
print('Win Total    : ',int(win))
print('Draw Total   : ', int(draw))
print('Lose Total   : ',int(lose))
print('------------------------------')
play = int(win)+int(draw)+int(lose)
print('Total Play   : ',int(play))
print('----------------------------------')
print()

#  point
winPoint = int(win)*3
drawPoint = int(draw)*1
losePoint = int(lose)*0
totalPoint = int(winPoint)+int(drawPoint)+int(losePoint)

print('*')
print('Win Point    : ',int(winPoint))
print('Draw Point   : ',int(drawPoint))
print('Lose Point   : ',int(losePoint))
print('----------------------------------')
print('Total Point  : ',int(totalPoint))
print('----------------------------------')
print()

# precentage
winPrec = (float(win)/float(play))*100
drawPrec = (float(draw)/float(play))*100
losePrec = (float(lose)/float(play))*100
#
print('Precentage')
print('Win Precentage   : ',float(winPrec))
print('Draw recentage   : ',float(drawPrec))
print('Lose Precentage  : ',float(losePrec))
