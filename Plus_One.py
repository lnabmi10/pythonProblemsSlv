digits = [9]
l=len(digits)
result=0
if digits[-1]==9 :
    
    for d in digits:
        result=result+d*(10**(l-1))
        l=l-1
    result+=1
    s_result=str(result)
    l_result=list(s_result)
    mylist =list(map(lambda d : int(d),l_result)) 
    
    print(mylist) 
    

else:
    digits[-1]+=1
