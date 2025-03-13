
##########################################################
##   My training project in the Python training class   ##
##########################################################
'''
**** After running the program, enter the numbers to the desired and then use the letter or NO to exit and view the result ****

'''

def max_list():
    numbers = []  
    maxi = None   

    while True:
        inp = input("enter a number or 'n' to exit: ")
        if inp.lower() in ["n", "no"]:
            break  
        
        try:
            inp = int(inp)
            numbers.append(inp) 
            
            
            if maxi is None or inp > maxi:
                maxi = inp
        
        except ValueError:
            print("please enter a number!")
    print(numbers)
    return maxi  

print("max number in list : ", max_list())
