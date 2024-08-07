import Get_Nums_Target



#result=Get_Nums_Target.getNumsAndTarget()



nums = [-3,2,5,7,14,11,15,7,4]
target=8
result=[]
for index1,n in enumerate(nums):
    loop_continue=0
    for index2,y in enumerate(nums) :
        if n+y==target :
            print(f"{n}+{y} = {target}")
            loop_continue=1
            result=[index1,index2]
    if loop_continue==1 :
        break


print(result)