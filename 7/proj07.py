    ###########################################################
    #  Computer Project #7
    #
    #  Algorithm
    #    function to open file and return a file pointer
    #       try and except to open correct file
    #    function to read the file
    #       for loop to read each line
    #           splits line to create list
    #           if statement to check for data
    #           append information to list
    #           calculate avg prescription and unit costs
    #       create and sort list of data
    #   function to sort list of data for a year and select the top ten medications.
    #       sorts list
    #       selects top ten
    #       for loop for each tuple
    #           creates list of brand names and list of values in column
    #   function to get list of medications covered by Medicaid in the specified year.
    #       for loop for each tuple
    #           if year of medication matches year wanted, append to list
    #           if years do not match, do not append
    #       sort the list
    #   function to display the information for each medication in a year
    #       print statements for table
    #       for loop for each tuple
    #           create list of data for each medication for the table
    #           append the information list to the table list
    #       sort the table list
    #       for loop for tuples in table list
    #           print data for each medication in the table
    #   function to plot information of the top ten medications in graphs
    #   function to prompt the user for inputs and call the other functions
    #       input for year
    #       try and except for input that can convert to an int
    #       while loop for when want algorithm to run
    #           if statement for if input year within data range
    #               if statement if want to plot top ten
    #           error message if input year not within data range
    ###########################################################
    
    

from operator import itemgetter
import pylab

def open_file():
    """Open a file.
    Returns a file pointer."""
    
    while True:
        try:
            fp=open(input("Input a file name: "))   #Open the file inputted
            return fp
        except FileNotFoundError:            #If input a file name not found
            print("Unable to open the file. Please try again.")
            continue

def read_data(fp): 
    """Read a file and search through the contents.
    fp: file pointer
    Returns sorted list of data."""
    
    fp.readline()               #skip first line
    data = []
    data_list = []
    for line in fp:             #read each line of the file
        data_list = []
        line_list = line.strip().split(',')  #strip white space, split at comma
        if line_list[3] == "n/a" or line_list[4] == "n/a" or line_list[5] == "n/a":
            continue
            #ignore line if does not have all of the data needed
            
        data_list.append(int(line_list[0]))     #year
        data_list.append(str(line_list[1]))     #brand
        data_list.append(float(line_list[3]))   #total spending on that drug
        data_list.append(int(line_list[4]))     #prescriptions
        data_list.append(int(line_list[5]))     #units
        
        avg_cost_prescription = data_list[2] / data_list[3]
        data_list.append(avg_cost_prescription)
        #calculate and append average cost per prescription
        
        avg_cost_units = data_list[2] / data_list[4]
        data_list.append(avg_cost_units)
        #calculate and append average cost per unit
        
        data_tuple = tuple(data_list)   #convert list to tuple
        data.append(data_tuple)         #append tuple
        
    data.sort()                         #sort the list
    return data                         #return the list

def top_ten_list(column, year_list): 
    """Sorts list of data for a year and selects the top ten medications.
    column: which information from the top ten
    year_list: a sorted list of tuples with all the medications covered by \
        Medicaid during the specified year
    Returns list1, the brand names of the top ten, and list2, the values in \
        the specified column for the top 10 tuples reverse order. """
    
    sorted_list = sorted(year_list, key=itemgetter(column-1,1), reverse = True)
    #sort medications column then brand
    
    top_ten = sorted_list[:10]      #create list of top ten medications
    list1 = []  #brand names
    list2 = []  #values in column
    for tup in top_ten:             #create the two lists
        list1.append(tup[1])
        list2.append(tup[column-1])
    return list1, list2             #return the two lists
           
def get_year_list(year, data):
    """Gets list of medications covered by Medicaid in the specified year.
    year: which year to select medications of
    data: sorted list of data
    Returns a sorted list of tuples with all the medications covered by \
        Medicaid during the specified year"""
    
    year_list = []
    for tup in data:
        if tup[0] == year:          #if medication covered in the year
            year_list.append(tup)
            
        else:                       #don't append if not covered
            continue
    year_list.sort()                #sort the list
    return year_list                #return the list

def display_table(year, year_list):
    """Displays the information for each medication in a year.
    year: which year to display medications of
    year_list: a sorted list of tuples with all the medications covered by \
        Medicaid during the specified year"""
    
    table_list = []
    tup_list = []
    center_statement = "Drug spending by Medicaid in " + str(year)
    print ("{:^80s}".format(center_statement))
    print ("{:<35s}{:>15s}{:>20s}{:>15s}".format("Medication", \
           "Prescriptions", "Prescription Cost", "Total"))
    #table print statements

    for tup in year_list:
        tup_list = [tup[1], tup[3], tup[5], tup[2] / 1000]
        #list of data for each medication for table
        
        table_list.append(tup_list)
        #append the information list to the table list
        
    table_list.sort()       #sort the list
    for tup in table_list:  #print data for each medication in the table
        print ("{:<35s}{:>15,d}{:>20,.2f}{:>15,.2f}".format(tup[0], tup[1], \
               tup[2], tup[3]))  

def plot_top_ten(x, y, title, xlabel, ylabel):   
    '''
        This function plots the top 10 values from a list of medications.
        This function is provided to the students.
        
            x (list) -> labels for the x-axis
            y (list) -> values for the y-axis
            title (string) -> Plot title
            xlabel (string) -> Label title for the x-axis
            ylabel (string) -> Label title for the y-axis
    '''
    
    pos = range(10)
    pylab.bar(pos, y)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.xticks(pos,x, rotation='90')
    pylab.show()
    

def main(): 
    """Prompts the user for inputs and calls the appropriate functions."""
    
    fp = open_file()            #open the file
    data = read_data(fp)        #read the data
    print ("Medicaid drug spending 2011 - 2015")
    input_str = input("Enter a year to process ('q' to terminate): ")
    #which year want data for
    
    while input_str.lower() !="q":      #when input is not terminate
        try:
            input_str = int(input_str)  #string year to integer year
            if input_str < 2016 and input_str > 2010 :  
            #year in range of data
                year_list = get_year_list(input_str,data) 
                display_table(input_str,year_list)
                #call functions
                
                top_ten_input = input("Do you want to plot the top 10 values\
                                      (yes/no)? ")
                #ask if want to plot top ten medications
                
                if top_ten_input.lower() == "yes":
                    column = 4      #number of prescriptions
                    list1,list2=top_ten_list(column, year_list)
                    #call function for lists
                    x=list1
                    y=list2
                    xlabel = "Medication Name"
                    ylabel = "Prescriptions"
                    title = "Top 10 Medications Prescribed in " + str(input_str)
                    plot_top_ten(x, y, title, xlabel, ylabel)
                    
                    column = 3      #Medicaid coverage
                    list1,list2=top_ten_list(column, year_list)
                    #call function for lists
                    x=list1
                    y=list2
                    xlabel = "Medication Name"
                    ylabel = "Amount"
                    title = "Top 10 Medicaid Covered Medications in " + str(input_str)
                    plot_top_ten(x, y, title, xlabel, ylabel)
                    
                    input_str = input("Enter a year to process ('q' to terminate): ")
                    #which year want data for
                    
                elif top_ten_input.lower() == "no":
                    input_str = input("Enter a year to process ('q' to terminate): ")
                    #which year want data for
                    
            else:   #if input_str year not in range
                print("Invalid Year. Try Again!")
                input_str = input("Enter a year to process ('q' to terminate): ")
                #which year want data for
                
        except ValueError:      #if input_str cannot be converted to an int
            print("Invalid Year. Try Again!")
            input_str = input("Enter a year to process ('q' to terminate): ")
            #which year want data for
        
if __name__ == "__main__":
    main()