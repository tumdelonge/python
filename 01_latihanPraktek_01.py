# buat program untuk meminta inputan nama klub sepakbola, jumlah pertandingan yg dimenangkan, jumlah seri, jumlah kekalahan, dan jumlah total pertandignan, lalu tampilkan presentase kemenangan

clubName = input('Club Name : ')
w = input('Win : ')
d = input('Draw :')
l = input('Lose :')

print('')
print('--------------------------------------')
print('Club Name : ',clubName)
print('--------------------------------------')
print('Win Total : ',int(w))
print('Draw Total : ',int(d))
print('Lose Total : ',int(l))
print('--------------------------------------')

p = int(w) + int(d) + int(l)
print('Play Total : ',int(p))
print('--------------------------------------')
print('')
print('')

print('--------------------------------------')
# details points
print('*Detail Points*')
print('--------------------------------------')
#win points
winPoints = int(w) * 3
print('-Win Points (w * 3)')
print('-',int(w),' * 3',' = ',winPoints)

# draw points
drawPoints = int(d) * 1
print('-Draw Points (d * 1)')
print('-',int(d),' * 1',' = ',drawPoints)

# lose points
losePoints = int(l) * 0
print('-Lose Points (l * 0)')
print('-',int(l),' * 0',' = ',losePoints)

# Total Points
totalPoins = int(winPoints) + int(drawPoints) + int(losePoints)
print('* Total Points : ',int(totalPoins))
print('--------------------------------------')
print('')
print('')


print('--------------------------------------')
print('Precentage')
print('--------------------------------------')
# win precentage
wp = float(w) / float(p) * 100
print('Win Precentage : ',float(wp),' / ',round(wp, 2), ' %')

# draw precentage
dp = float(d) / float(p) * 100
print('Draw Precentage : ',float(dp), ' / ', round(dp, 2), ' %')

# lose precentag
lp = float(l) / float(p) * 100
print('Lose Precentage : ',float(lp), ' / ', round(lp, 2),' %')