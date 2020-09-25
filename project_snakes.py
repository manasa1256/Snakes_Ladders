import random
print('Enter no of players:')
n = int(input())
l=[]
name=[]
for i in range(n):
    print('Enter Player',i+1,'name')
    name.append(input())
    
for i in range(n):
    l.append(0)
L_start_pos=[5,10,18,23,49,57,61,73,81,88]
L_end_pos=[26,39,37,32,67,76,78,86,98,91]
S_start_pos=[13,24,38,44,51,60,75,85,92,99]
S_end_pos=[3,6,19,2,37,30,58,70,80,60]
i=0
dice=0
#print(random.randint(1,6))
while(1):
    print("\n",name[i],"'s turn")
    print("Press enter to roll dice")
    inp=input()
    #print(inp)
    if(inp==''):
        #print("fgf")
        dice = random.randint(1,6)
        print('The number rolled is ',dice)
        d=dice
        while(d==6):
            print('Woww..! You got an extra chance')
            if(input()==''):
                d=random.randint(1,6)
                print('The number rolled is:',d)
                if(d+l[i]<=100):
                    l[i]+=d
    if(dice+l[i]<=100):
        l[i]=l[i]+dice
        #print("Player ",i," pos is ",l[i])
    if(l[i]==100):
        print("Hurray..! Winner is player ",name[i])
        break
    if l[i] in L_start_pos:
        ind=L_start_pos.index(l[i])
        l[i]=L_end_pos[ind]
        print("Yaay! ",name[i],"got a ladder")
    elif l[i] in S_start_pos:
        ind=S_start_pos.index(l[i])
        l[i]=S_end_pos[ind]
        print("Oops..! ",name[i],"got bitten by a snake")
    print("Player ",name[i]," pos is:",l[i])
    if(i==n-1):
        i=0
    else:
        i+=1
    
