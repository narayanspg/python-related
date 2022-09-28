#this program will decode the given string with cipher. add 13 and ..... from FI
input="lbh_unir_cnffrq_guvf_grfg"
res=""
for i in input:
    if(i.isalpha()):
        #convert i to number - store in j
        j=ord(i)-96
        print("J value: " + str(j))
        c=j+13
        if c>26:
            c=c-26
        print("c value: " + str(c))
    #convert to char - store in p
        p=chr(c+96)
        print("p value: " + str(p))
        res=res+p
print(res)

