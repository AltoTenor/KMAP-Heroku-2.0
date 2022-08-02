
from Changing_Input_To_Indexes import citi
from solve4 import solve4

#DRIVER CODE

def kmap4(oc,exp,a,b,c,d):

    if oc==1:
        storage=[]
        for i in exp:
            if i not in storage and i!='+' and i!="'" and i!=" ":
                storage+=[i]
        if (len(storage)<4 ):
            for i in ['A','B','C','D']:
                if i not in storage:
                    storage+=[i]
                if len(storage)==4:
                    break
                
        a,b,c,d=storage
        print(a,b,c,d)
        finalans=(solve4(citi(exp,a,b,c,d)))
        
    else:
        print("EXP IS",exp)
        finalans=(solve4(exp))

    s=''
    print(finalans)
    if finalans==1:
        s="1"
    else:
        for i in range(len(finalans)-1):
            
            if finalans[i]=='a':
                s=s+a+' '
        
            elif finalans[i]=='b':
                s=s+b+' '
        
            elif finalans[i]=='c':
                s=s+c+' '

            elif finalans[i]=='d':
                s=s+d+' '
    
            elif finalans[i]=='+':
                s=s+'+ '
    
            else:
                s+=finalans[i]
            
    return s

# kmap_size=int(input("How many variables does your expression have? (2/3/4)\n"))
# while True:
#     option_choice=int(input("Enter how you want to input the terms\n 1.Sum of Minterms\n 2.Indexes of Minterms\n"))
#     if option_choice in (1,2):
#         break
#     else:
#         print("Inavlid Choice. ")
    
# if option_choice==1:
#     exp=input("Enter the expression (Eg:a'b'c'd+abc'd with no spaces) : ")
# else:
#     exp=list(map(int,input("Enter the indexes seperated by spaces: ").split()))
#     a=input("Enter the variable names.\nFirst: ")
#     b=input("Second: ")
#     c=input("Third: ")
#     d=input("Fourth: ")

# if kmap_size==4:
#     kmap4(option_choice,exp,a,b,c,d)
# elif kmap_size==3:
#     print("ONLY size 4 available for now")
# #     kmap3(option_choice)
# elif kmap_size==2:
#     print("ONLY size 4 available for now")
# #     kmap2(option_choice)
# else:
#     print("Out of scope. ")

kmap4(1,"abc+a'+b'+c'","a",'b',"c","A")