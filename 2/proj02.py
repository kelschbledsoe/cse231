    ###########################################################
    #  Computer Project #2
    #
    #  Algorithm to compare 2017 tax to 2018
    #    prompt for an integer
    #    input an integer
    #    while loop to compute tax for 2017 vs 2018
    #       if statements for tax brackets
    #       calculates tax based on bracket
    #       calculate tax difference in cents and percentage
    #       calculations rounded
    #       calculations printed
    #       prompt for another integer
    #       input an integer
    ###########################################################
    
    
#Input income amount
income_str = input ("Enter income as an integer with no commas: ")
income = int(income_str)    #Inputted income as an integer
income_tax17 = 0            
income_tax18 = 0
diff_cents = 0              #Difference between 2017 and 2018 tax in cents
diff_per = 0                #Difference between 2017 and 2018 tax in a percentage



#while loop to compute 2017 and 2018 tax

while income >= 0 :
    print ("Income:", income)
    
    #2017 tax
    if income <= 9325 :                 #10% tax bracket for 2017
        income_tax17 = (income * 0.1)
        
    elif income >= 9326 and income <= 37950 :   #15% tax bracket for 2017
        income_tax17 = (.1 * 9325) + (income - 9325) * (.15)  
        
    elif income >= 37951 and income <= 91900:   #25% tax bracket for 2017
        income_tax17 = (.1 * 9325) + (37950-9325) * (.15) + (income - 37950) * (.25)    
        
    elif income >= 91901 and income <= 191650:  #28% tax bracket for 2017
        income_tax17 = (.1 * 9325) + (37950-9325) * (.15) + (91900 - 37950) * (.25) + (income - 91900) * (.28)
    
    elif income >= 191651 and income <= 416700: #33% tax bracket for 2017
        income_tax17 = (.1 * 9325) + (37950-9325) * (.15) + (91900 - 37950) * (.25) + (191650-91900) * (.28) \
        + (income - 191650) * (.33)
    
    elif income >= 416701 and income <= 418400: #35% tax bracket for 2017
        income_tax17 = (.1 * 9325) + (37950-9325) * (.15) + (91900 - 37950) * (.25) + (191650-91900) * (.28) \
        + (416700 - 191650) * (.33) + (income - 416700) (.35) 
        
    else:                                           #39.6% tax bracket for 2017
        income_tax17 = (.1 * 9325) + (37950-9325) * (.15) + (91900 - 37950) * (.25) + (191650-91900) * (.28) \
        + (416700 - 191650) * (.33) + (418400-416700) * (.35) + (income - 418400) * (.396)


    #2018 tax
    if income <= 9525 :     #10% tax bracket for 2018
        income_tax18 = (income * 0.1)
        
    elif income >= 9526 and income <= 38700 :       #12% tax bracket for 2018
        income_tax18 = (.1 * 9525) + (income - 9525) * (.12)  
        
    elif income >= 38701 and income <= 82500:       #22% tax bracket for 2018
        income_tax18 = (.1 * 9525) + (38700-9525) * (.12) + (income - 38700) * (.22)    
        
    elif income >= 82501 and income <= 157500:      #24% tax bracket for 2018
        income_tax18 = (.1 * 9525) + (38700-9525) * (.12) + (82500 - 38700) * (.22) + (income - 82500) * (.24)
    
    elif income >= 157501 and income <= 200000:     #32% tax bracket for 2018
         income_tax18 = (.1 * 9525) + (38700-9525) * (.12) + (82500 - 38700) * (.22) + (157500-82500) * (.24) \
        + (income - 157500) * (.32)
    
    elif income >= 200001 and income <= 500000:     #35% tax bracket for 2018
        income_tax18 = (.1 * 9525) + (38700-9525) * (.12) + (82500 - 38700) * (.22) + (157500-82500) * (.24) \
        + (200000 - 157500) * (.32) + (income - 200000) * (.35)
    
    else:                                           #37% tax bracket for 2018
        income_tax18 = (.1 * 9525) + (38700-9525) * (.12) + (82500 - 38700) * (.22) + (157500-82500) * (.24) \
        + (200000 - 157500) * (.32) + (500000-200000) * (.35) + (income - 500000) * (.37)
    
    #Calculate difference in taxes in cents and percentage
    diff_cents = (income_tax18 - income_tax17)
    diff_cents = round(diff_cents,2)
    diff_per = (abs((diff_cents / income_tax17) * 100))
    diff_per = round(diff_per, 2)
    
    #Round taxes to cents
    income_tax17 = round(income_tax17, 2)
    income_tax18 = round(income_tax18, 2)
    
    #Print calculation results
    print ("2017 tax:", income_tax17)
    print ("2018 tax:", income_tax18)
    print ("Difference:", diff_cents)
    print ("Difference (percent):", diff_per)

    #Prompt for another income amount
    income_str = input ("Enter income as an integer with no commas: ")
    income = int(income_str) 
   

 