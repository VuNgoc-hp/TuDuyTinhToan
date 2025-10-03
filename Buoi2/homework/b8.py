name=input('Ten chu ho: ')
lastind=int(input('Chi so thang truoc: '))
nowind=int(input('Chi so thang nay: '))
if nowind<=50:
    cost=nowind*1984
elif nowind<=100:
    cost=nowind*2050
elif nowind<=200:
    cost=nowind*2380
elif nowind<=300:
    cost=nowind*2998
elif nowind<=400:
    cost=nowind*3350
else:
    cost=nowind*3460
print(f'Ho va ten: {name}')
print(f'Tien phai tra la: {cost}')
