    ###########################################################
    #  Computer Project #5
    #
    #  Algorithm
    #    function to open file and return a file pointer
    #       try and except to open correct file
    #    function to read the file
    #       for loop to read each line
    #           splits line at comma to create list
    #           indexes the list as variables
    #           if statements to search data lines based on country or region name
    #       calculates average happiness of countries from search results
    #       prints results
    #   function to print search results
    #   function to prompts the user for inputs and calls the other function
    #       while loop for correct search input
    ###########################################################

def open_file():
    """Open a file.
    Returns a file pointer."""
    while True:
        try:
            fp=open(input("Input a file name: "))   #Open the file inputted
            return fp
        except FileNotFoundError:   #If input a file name not found
            print("Unable to open the file. Please try again.")
            continue
    
def read_data(fp, input_str, search_str):
    """Read a file and search through the contents. Print the results.
    fp: file data
    input_str: search through data as country name (1) or region name (2)
    search_str: word to search for
    """
    
    happy_total = 0
    happy_num = 0
    fp.readline()
    print ("{:24s}{:<32s}{:<17s}".format("Country", "Region", "Happiness Score"))
    print ("-----------------------------------------------------------------------")
    for line in fp:                     #Read each line of the file        
        data_line = line.split(",")     #Create a list by splitting at each comma
        country_name = data_line [0]    #List variable at index 0 is country name
        region_name = data_line [1]     #List variable at index 1 is region name       
        happiness_score = float(data_line [2])  
        #List variable at index 2 is happiness score
        if input_str == "1":                #Searching based on country name
            if search_str.lower() in country_name.lower():  
                happy_total += happiness_score
                happy_num += 1
                display_line(country_name,region_name,happiness_score)                   
            
        if input_str == "2":                #Searching based on region name
            if search_str.lower() in region_name.lower():
                happy_total += happiness_score
                happy_num += 1
                display_line(country_name,region_name,happiness_score)
    happiness_avg = happy_total/happy_num   
    #Calculate average happiness of countries from search results    
    print ("-----------------------------------------------------------------------")
    print ("{:24s}{:<17.2f}".format("Average Happiness Score", happiness_avg))
    #Print average happiness
    
def display_line(country_name, region_name, happiness_score): 
    """Prints values using formatting.
    country_name: name of country
    region_name: name of region of country
    happiness_score: happiness score of country
    """
    
    print ("{:24s}{:<32s}{:<17.2f}".format(country_name, region_name, happiness_score))
    #Print information of countries from search results
    
def main():
    """Prompts the user for inputs and calls the appropriate functions."""
    
    fp = open_file()
    input_str = input("Input 1 to search in country names, 2 to search in regions: ")
    while input_str !="1" and input_str !="2":  
    #Must input 1 or 2 to define what to search by             
        print("Invalid choice, please try again!")
        input_str = input("Input 1 to search in country names, 2 to search in regions: ")
        
    search_str = input("What do you want to search for? ")
    read_data(fp, input_str, search_str)

if __name__ == '__main__':
   main()
