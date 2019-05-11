import re

print('미터 환산기 : 거리를 입력하세요__ ',end="")
x=input()
compiled = re.compile(r'([0-9]*).*?(km|mm|cm|m)')
s = compiled.search(x)
if s != None:
    a = s.group(1)
    b = s.group(2)
else:
    print('ERROR!!!!')
    exit()
if(b=='km'):
    print((int(a)/1000),'m')
elif(b=='m'):
    print((int(a)),'m')
elif(b=='cm'):
    print((int(a)*100),'m')
elif(b=='mm'):
    print((int(a)*10000),'m')
else:
    print('ERROR!!!!')
