def is_Palindrome(x) :
    
      if x >=0 :

           w=10
           r=0
           p=0
           palindrome_list1=[]
           palindrome_list2=[]
       
           while(x*10 >= w  ) :
                  r = x%w
                  x = x - r
                  p = r*10/w
                  palindrome_list1.insert(0,p)
                  palindrome_list2.append(p)
                  w = w*10
           if palindrome_list1==palindrome_list2 :
                 return True
           else :
                 return False
      else :
           return False

   

test1=is_Palindrome(-48)

print(test1)