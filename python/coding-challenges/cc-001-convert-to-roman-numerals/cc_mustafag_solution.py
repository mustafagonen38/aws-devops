number = input('''
###  This program converts decimal numbers to Roman Numerals ###
(To exit the program, please type "exit")
Please enter a number between 1 and 3999, inclusively : 
''')
if number.isdigit() :

    if int(number) >= 1 or int(number) <= 3999 :
        a = (int(number) // 1000)
        

    

else :
    print("Not Valid Input !!!")

