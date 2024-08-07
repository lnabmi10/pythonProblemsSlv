

def getNumsAndTarget():

    array_len=0

    while array_len==0 :
        numbersOfNums=input("please enter the numbers of num you will use :" )
        if numbersOfNums.isdigit():
           numbersOfNums=int(numbersOfNums)
           if  numbersOfNums > 2 :
               array_len=numbersOfNums-1
           else :
            numbersOfNums=input("your numbers is wrong ,your number must be more than 2 :" )
               
        else : 
            numbersOfNums=input("your numbers is wrong ,please enter valid numbers of num you will use :" )

    print(f"your array len is {array_len}")   

    currentNum = 1

    nums=[]


    while currentNum < numbersOfNums :
        number=input("please enter your number :" )

        if number.isdigit():
            number=int(number)
            nums.append(number)
            currentNum += 1
        elif number.startswith("-") :
            if (number[1:]).isdigit():
                number=int(number)
                nums.append(number)
        else :
            print("your numbers is wrong " )
    for num in nums:
        print (f"this num is {num}")

    target=0
    while(target==0):
        x=input("inter your target : ")
        if x.isdigit():
            if x==0:
               break
            else :
               target=int(x)
        else : 
            print("your number is wrong")

    print(f"your target is {target}")

    return (target,nums)

