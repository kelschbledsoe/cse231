    ###########################################################
    #  Computer Project #3
    #
    #  Algorithm to convert currency
    #    prompt for currencies to convert between
    #    prompt for value to convert
    #    ensure value is an integer
    #    url to pull conversion value
    #    find information from url
    #       find first digit for left bound
    #    find right bound
    #    splice the info for the currency equivalent
    #    print currency conversion
    #    ask if want to calculate another value
    ###########################################################


import urllib.request
 
ask = "yes"
while ask.lower() != "no":  #calculation while loop
  
    #prompt for original currency
    currency_orig = input("What is the original currency? ")    
    #uppercase for URL to work 
    currency_orig = currency_orig.upper() 
    #prompt for desired currency                  
    currency_final = input("What currency do you want to convert to? ")     
    #uppercase for URL to work
    currency_final = currency_final.upper()                     
    #prompt for value want to convert
    amount_orig = input("How much do you want to convert (int)? ")  
    
    while not amount_orig.isdigit():        #ensure value inputted is an integer
       print ("The value you input must be an integer. Please try again.")
       #prompt for new value if not an integer
       amount_orig = input("How much do you want to convert (int)? ")   

    url_part_1 = "https://finance.google.com/finance/converter?a=" + amount_orig 
    url_part_2 = "&from=" + currency_orig + "&to=" + currency_final
    full_url = url_part_1 +  url_part_2     #url to pull conversion value
    
    response = urllib.request.urlopen(full_url)
    result = str(response.read())
    
    #locate conversion value from long string
    result.find("span")
    index = result.find("span")
    #select small part of long string which contains the conversion value
    info = result [index:]      
    left_bound = 0
    right_bound = 0
    
    #make left bound of splice the first digit in the small string
    for char in info :  
        if char.isdigit():
            left_bound = info.index(char)
            break
        
    #make right bound of slice the desired currency
    right_bound = info.find(currency_final)   #right bound of split    
    
    #the converted currency        
    info_needed = info [left_bound : right_bound]
        
    amount_converted = float(info_needed)
    
    #printing results    
    print ()
    print (amount_orig, currency_orig, "is", "{:.2f}".format(amount_converted),\
           currency_final )    

    #ask if want to convert again
    ask = input ("Do you want to convert another currency? ")