i=0
while i<1:
    print('S = ',end="")
    S=input()
    print('V = ',end="")
    V=input()
    print('T = ',end="")
    T=input()
    if(S==''):
        if(V==''):
            print('Please input correct number or blank.')
        elif(T==''):
            print('Please input correct number or blank.')
        else:
            x=int(V)*int(T)
            print('S = '+str(x))
            i=i+1
    elif(V==''):
        if(T==''):
            print('Please input correct number or blank.')
        else:
            x=int(S)/int(T)
            print('V = '+str(x))
            i=i+1
    elif(T==''):
        x=int(S)/int(V)
        print('T = '+str(x))
        i=i+1
    else:
        print('Please input correct number or blank.')