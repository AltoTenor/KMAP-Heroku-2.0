def citi(exp,a,b,c,d):
    variables_used=[a,b,c,d]
    exp1=""
    for i in exp:
        if i!=" ":
            exp1+=i

    exp=exp1
    
    list_of_terms=exp.split("+")  #List of terms

    for i in range(len(list_of_terms)):   #Adding Space at the end of every string to make checking for ' easier
        list_of_terms[i]+=" "
    print(list_of_terms)
    binaryterms=[]

    for i in list_of_terms:              #Converting terms to 1s and 0s and Xs
        s=''
        for j in variables_used:  
            if j in i:
                print(i)
                print(j)
                if i[i.index(j)+1]=="'":
                    s+='0'
                else:
                    s+='1'
            else:
                s+='X'
        binaryterms+=[s]
    i=0
    while(True):
        try:
            while('X' in binaryterms[i]):     #Converting X to 1s and 0s
                for j in range(len(binaryterms[i])):
                    if binaryterms[i][j]=='X':
                        binaryterms+=[binaryterms[i][:j]+'1'+binaryterms[i][j+1:]]
                        binaryterms[i]=binaryterms[i][:j]+'0'+binaryterms[i][j+1:]
            i+=1
        except:
            break

            #Converting binary numbers to minterm indexes

    dict_of_minterms={"0000":0,"0001":1,"0010":2,"0011":3,"0100":4,"0101":5,"0110":6,"0111":7,"1000":8,"1001":9,"1010":10,"1011":11,"1100":12,"1101":13,"1110":14,"1111":15}
    answer=[]
    answer1=[]

    for i in binaryterms:
        answer+=[dict_of_minterms[i]]
    answer.sort()
    for i in answer:
        if i not in answer1:
            answer1+=[i]
    return(answer1)
    