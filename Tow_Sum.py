import Get_Nums_Target



def twoSum(self, nums, target):
        result=[]
        loop_continue=0

        for index1,n in enumerate(nums):
            
            for index2,y in enumerate(nums) :
                print(f"the  is in index1 is {index1} index2 {index2}")
                           
                if index1 != index2 and n+y==target :
                   print(f"le somme de {n} et {y} = {target}")
                   print(f"l index est {index2}")
                   loop_continue=1
                   result=[index1,index2]
                   break
            if loop_continue==1 :
                 break


        print(result)

twoSum("x",[3,2,4],6)