class Solution(object):
    def romanToInt(self, s):
        result=0
        roman_dic={
              "I":1,
              "V":5,
              "X":10,
              "L":50,
              "C":100,
              "D":500,
              "M":1000 
            }
        roman_num = list(s)
        roman_num.reverse()
        prevent_value=0
        print(roman_num)
        for var in roman_num :
    
            if var in roman_dic :
                
                
                if prevent_value <= roman_dic[var]:
                    result=result + roman_dic[var]
                    print(f"the result is {result}")
                else :
                    result=result-roman_dic[var]
                    print(f"the result is {result}")

        
        
                prevent_value=roman_dic[var]
        
            else :
                print("it s not roman number")
                break
            
        return result
        
    x=romanToInt('x',"III")
    print(x)