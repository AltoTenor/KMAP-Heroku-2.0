#Main Part of code which solves the KMAP considering all possible cases
#Includes the following patter- 8   4 (Horizonatally/Vertically/Box)   2 (Horizontally/Vertical)   1 each



def check8(KMAP,ind):
    finalanswerchar=''
    answerchar=''
    t=0
    for i in range(2):
        count=0
        answer=[]
        for i in range(0,5):
            sum_of_row=0
            for j in range (0,4):
                if KMAP[i%4][j]==1:
                    sum_of_row+=1
            if sum_of_row==4:
                count+=1
                answer+=[(i%4)+1]
                if count>=2 and count!=t:
                    t=count
                    break
            else:
                count=0
                answer=[]
        temp=answer[-1:-3:-1]
        temp.reverse()
        if temp==[1,2]:
            answerchar='a\''
        if temp==[2,3]:
            answerchar='b'
        if temp==[3,4]:
            answerchar='a'
        if temp==[4,1]:
            answerchar='b\''
            
        if (answerchar not in finalanswerchar) and( answerchar!=''):
            finalanswerchar+=answerchar+'+'
            if answerchar=='a\'':
                for i in range(0,4):
                    for j in range(0,2):
                        ind[j][i]=1
            elif answerchar=='b':
                for i in range(0,4):
                    for j in range(1,3):
                        ind[j][i]=1
            elif answerchar=='a':
                for i in range(0,4):
                    for j in range(2,4):
                        ind[j][i]=1
            elif answerchar=='b\'':
                for i in range(0,4):
                    for j in (-1,0):
                        ind[j][i]=1



    finalanswerchar2=''
    answerchar1=''
    t=0
    for i in range(2):
        count=0
        answer1=[]
        for i in range(0,5):
            sum_of_column=0
            for j in range (0,4):
                if KMAP[j][i%4]==1:
                    sum_of_column+=1
            if sum_of_column==4:
                count+=1
                answer1+=[(i%4)+1]
                if count>=2 and count!=t:
                    t=count
                    break
            else:
                count=0
                answer=[]
        temp1=answer1[-1:-3:-1]
        temp1.reverse()
        if temp1==[1,2]:
            answerchar1='c\''
        if temp1==[2,3]:
            answerchar1='d'
        if temp1==[3,4]:
            answerchar1='c'
        if temp1==[4,1]:
            answerchar1='d\''

        if (answerchar1 not in finalanswerchar2) and( answerchar1!=''):
            finalanswerchar2+=answerchar1+'+'
            if answerchar1=='c\'':
                for i in range(0,4):
                    for j in range(0,2):
                        ind[i][j]=1
            elif answerchar1=='d':
                for i in range(0,4):
                    for j in range(1,3):
                        ind[i][j]=1
            elif answerchar1=='c':
                for i in range(0,4):
                    for j in range(2,4):
                        ind[i][j]=1
            elif answerchar1=='d\'':
                for i in range(0,4):
                    for j in (-1,0):
                        ind[i][j]=1

    return[finalanswerchar+finalanswerchar2,ind]


def check4H(KMAP,ind):
    s=''
    s1=''
    for i in range(0,4):
        if sum(KMAP[i])==4 and sum(ind[i])<4:
            for j in range (0,4):
                ind[i][j]=1
            s+=str(i+1)
    if '1' in s:
        s1+=("a'b'+")
    if '2' in s:
        s1+=("a'b+")
    if '3' in s:
        s1+=("ab+")
    if '4' in s:
        s1+=("ab'+")
    return[s1,ind]


def check4V(KMAP,ind):
    
    s=''
    s1=''
    for i in range(0,4):
        sumofcolumn=0
        sumofcolumnind=0
        for j in range (0,4):
            sumofcolumn+=KMAP[j][i]
            sumofcolumnind+=ind[j][i]
        if sumofcolumn==4 and sumofcolumnind<4:
            s+=str(i+1)
            
            for j in range (0,4):
                ind[j][i]=1
    if '1' in s:
        s1+=("c'd'+")
    if '2' in s:
        s1+=("c'd+")
    if '3' in s:
        s1+=("cd+")
    if '4' in s:
        s1+=("cd'+")
    return[s1,ind]  


def check4B(KMAP,ind):
    s=''
    s1=''
    final=''
    for i in range(0,4):
        for j in range (0,4):
            if ind[i][j]==0 and KMAP[i%4][j%4]==1:
                if KMAP[(i)%4][(j-1)%4]==1 and KMAP[(i-1)%4][(j-1)%4]==1 and KMAP[(i-1)%4][(j)%4]==1:
                    ind[(i)%4][(j-1)%4]=1 
                    ind[(i-1)%4][(j-1)%4]=1 
                    ind[(i-1)%4][(j)%4]=1
                    ind[i][j]=1
                    s+=str((i)%4+1)
                    s1+=str((j)%4+1)
                elif KMAP[(i-1)%4][(j)%4]==1 and KMAP[(i-1)%4][(j+1)%4]==1 and KMAP[(i)%4][(j+1)%4]==1:
                    ind[(i-1)%4][(j)%4]=1 
                    ind[(i-1)%4][(j+1)%4]=1 
                    ind[(i)%4][(j+1)%4]=1
                    ind[i][j]=1
                    s+=str((i)%4+1)
                    s1+=str((j+1)%4+1)
                elif KMAP[(i)%4][(j+1)%4]==1 and KMAP[(i+1)%4][(j+1)%4]==1 and KMAP[(i+1)%4][(j)%4]==1:
                    ind[(i+1)%4][(j)%4]=1 
                    ind[(i+1)%4][(j+1)%4]=1 
                    ind[(i)%4][(j+1)%4]=1
                    ind[i][j]=1
                    s+=str((i+1)%4+1)
                    s1+=str((j+1)%4+1)
                elif KMAP[(i+1)%4][(j)%4]==1 and KMAP[(i+1)%4][(j-1)%4]==1 and KMAP[(i)%4][(j-1)%4]==1:
                    ind[(i+1)%4][(j)%4]=1 
                    ind[(i+1)%4][(j-1)%4]=1 
                    ind[(i)%4][(j-1)%4]=1
                    ind[i][j]=1
                    s+=str((i+1)%4+1)
                    s1+=str((j)%4+1)

    for i in range(len(s)):
        if s[i]=='1':
            final+='b\''
        elif s[i]=='2':
            final+='a\''
        elif s[i]=='3':
            final+='b'
        elif s[i]=='4':
            final+='a'
        if s1[i]=='1':
            final+='d\''
        elif s1[i]=='2':
            final+='c\''
        elif s1[i]=='3':
            final+='d'
        elif s1[i]=='4':
            final+='c'
        final+='+'

    return[final,ind]


def check2H(KMAP,ind):
    s=''
    s1=''
    final=''
    for i in range(0,4):
        for j in range (0,4):
            if KMAP[i][j]==1 and ind[i][j]==0:
                if KMAP[i][(j+1)%4]==1:
                    ind[i][j]=1
                    ind[i][(j+1)%4]=1
                    s+=str((i)%4+1)
                    s1+=str((j)%4+1)
                elif KMAP[i][(j-1)%4]==1:
                    ind[i][j]=1
                    ind[i][(j-1)%4]=1
                    s+=str((i)%4+1)
                    s1+=str((j-1)%4+1)
    print(s,s1)
    for i in range(len(s)):
        if s[i]=='1':
            final+='a\'b\''
        elif s[i]=='2':
            final+='a\'b'
        elif s[i]=='3':
            final+='ab'
        elif s[i]=='4':
            final+='ab\''
        if s1[i]=='1':
            final+='c\''
        elif s1[i]=='2':
            final+='d'
        elif s1[i]=='3':
            final+='c'
        elif s1[i]=='4':
            print('XXX')
            final+='d\''
        final+='+'
    return[final,ind]
    
    
def check2V(KMAP,ind):
    s=''
    s1=''
    final=''
    for i in range(0,4):
        for j in range (0,4):
            if KMAP[i][j]==1 and ind[i][j]==0:
                if KMAP[(i+1)%4][j]==1:
                    ind[i][j]=1
                    ind[(i+1)%4][j]=1
                    s+=str(i+1)
                    s1+=str(j+1)
                elif KMAP[(i-1)%4][j]==1:
                    ind[i][j]=1
                    ind[(i-1)%4][j]=1
                    s+=str((i-1)%4+1)
                    s1+=str(j+1)
    print(s,s1)
    for i in range(len(s)):
        if s[i]=='1':
            final+='a\''
        elif s[i]=='2':
            final+='b'
        elif s[i]=='3':
            final+='a'
        elif s[i]=='4':
            final+='b\''
        if s1[i]=='1':
            final+='c\'d\''
        elif s1[i]=='2':
            final+='c\'d'
        elif s1[i]=='3':
            final+='cd'
        elif s1[i]=='4':
            final+='cd\''
        final+='+'
    return[final,ind]


def checkrest(KMAP,ind):
    k=[[0,1,3,2],
    [4,5,7,6],
    [12,13,15,14],
    [8,9,11,10]]
    dict_of_minterms={0:"a'b'c'd'",1:"a'b'c'd",2:"a'b'cd'",3:"a'b'cd",4:"a'bc'd'",5:"a'bc'd",6:"a'bcd'",7:"a'bcd",8:"ab'c'd'",9:"ab'c'd",10:"ab'cd'",11:"ab'cd",12:"abc'd'",13:"abc'd",14:"abcd'",15:"abcd"}
    s=''
    for i in range(0,4):
        for j in range(0,4):
            if ind[i][j]==0 and KMAP[i][j]==1:
                ind[i][j]=1
                s+=dict_of_minterms[k[i][j]]+"+"

    return [s,ind]


#Testing arrays
# g=[[1,1,0,0],
#    [0,1,1,0],
#    [0,1,1,0],
#    [0,1,0,0]]

# f=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# print(check8(g,f)[0]+check4H(g,f)[0]+check4V(g,f)[0]+check4B(g,f)[0]+check2H(g,f)[0]+check2V(g,f)[0]+checkrest(g,f)[0])