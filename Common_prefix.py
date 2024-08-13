

strs=["a"]
strs_list=[]
result=''

print("#"*20)
prev_value=''
index=0
for s in strs[0]:
    
    validate=False
  
    print(f"current value is {s}")
    for j in range(0,len(strs)):
        if index < len(strs[j]):
            if s == strs[j][index]:
                print(f"la valeur de strs[j] est : {strs[j][index]} ")
                validate=True
            else :
                validate=False
                break
        else :
            validate=False
            break

    index=index+1
    if validate:
        result=result+s
    else:
        break
        
print(result)

    