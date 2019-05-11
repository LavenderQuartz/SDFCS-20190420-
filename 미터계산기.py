import re

i = 0
while i<1:
    try:
        print('미터 환산기 : 거리를 입력하세요__(km~~mm까지만 가능) ',end="")
        x=input()
        compiled = re.compile(r'([0-9]*).*?(km|mm|cm|m)')
        s = compiled.search(x)
        if s != None:
            a = s.group(1)
            b = s.group(2)
        else:
            print('ERROR!!!!')
        if(b=='km'):
            print((int(a)/1000),'m')
            i = i+1
        elif(b=='m'):
            print((int(a)),'m')
            i = i+1
        elif(b=='cm'):
            print((int(a)*100),'m')
            i = i+1
        elif(b=='mm'):
            print((int(a)*10000),'m')
            i = i+1
        else:
            print('ERROR!!!!')
    except:
        print('ERROR!!!!')
