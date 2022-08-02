kmap_size=int(input("How many variables does your expression have? (2/3/4)\n"))
while True:
    option_choice=int(input("Enter how you want to input the terms\n 1.Sum of Minterms\n 2.Indexes of Minterms\n"))
    if option_choice in (1,2):
        break
    else:
        print("Inavlid Choice. ")
    
if option_choice==1:
    exp=input("Enter the expression (Eg:a'b'c'd+abc'd with no spaces) : ")
else:
    exp=list(map(int,input("Enter the indexes seperated by spaces: ").split()))
    a=input("Enter the variable names.\nFirst: ")
    b=input("Second: ")
    c=input("Third: ")
    d=input("Fourth: ")

if kmap_size==4:
    kmap4(option_choice,exp,a,b,c,d)
elif kmap_size==3:
    print("ONLY size 4 available for now")
#     kmap3(option_choice)
elif kmap_size==2:
    print("ONLY size 4 available for now")
#     kmap2(option_choice)
else:
    print("Out of scope. ")