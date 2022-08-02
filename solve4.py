
from checker import check8,check4H,check4V,check4B,check2H,checkrest,check2V



def solve4(exp):
    KMAP=[[ 0, 1, 3, 2],
          [ 4, 5, 7, 6],
          [12,13,15,14],
          [ 8, 9,11,10]]


    for i in range(0,4):
        for j in range(4):
            if KMAP[i][j] in exp:           #changing KMAP to grid of 1s and 0s from list indexes
                KMAP[i][j]=1
            else:
                KMAP[i][j]=0

    s=0
    for i in range(0,4):
        for j in range(0,4):            #checking which combinations are possible
            s+=KMAP[i][j]

    ind=[[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

    if s==16:                   #reducing time instead of checking all
        return(1)
    elif s>=8:    
        return(check8(KMAP,ind)[0]+check4H(KMAP,ind)[0]+check4V(KMAP,ind)[0]+check4B(KMAP,ind)[0]+check2H(KMAP,ind)[0]+check2V(KMAP,ind)[0]+checkrest(KMAP,ind)[0])
    elif s>=4:
       return(check4H(KMAP,ind)[0]+check4V(KMAP,ind)[0]+check4B(KMAP,ind)[0]+check2H(KMAP,ind)[0]+check2V(KMAP,ind)[0]+checkrest(KMAP,ind)[0])    
    elif s>=2:
        return(check2H(KMAP,ind)[0]+check2V(KMAP,ind)[0]+checkrest(KMAP,ind)[0])
    else:
        return(checkrest(KMAP,ind)[0])