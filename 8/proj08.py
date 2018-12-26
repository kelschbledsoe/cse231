    ###########################################################
    #  Computer Project #8
    #
    #  Algorithm
    #    function to open file and return a file pointer
    #       try and except to open correct file
    #    function to read the file
    #       for loop to read each line
    #           if AQI blank, record is invalid and not added
    #           make all pollutant means in parts per billion
    #           make list of city, date, and pollutant data
    #           if statement to ignore duplicate records
    #           if statement, add data as value to dict, state is key
    #       return the dictionary of data
    #   function to calculate the total pollution for each pollutant for \
    #   the state over 16 years
    #       if state is a key in the dictionary
    #           for every list in the value
    #               get year from list
    #               add data from value list to data list
    #           for list in data list
    #               add contents to different list
    #           find maximum and minimum pollution values
    #           create tuple of data list, max and min pollution values
    #           return data tuple
    #   function to create dictionary of total average pollution per city \
    #   for a state and year
    #       if state is a key in the dictionary
    #           for every list in the value
    #               get year from list
    #               if year from list is the year wanted
    #                   if city from list in dictionary
    #                       add data from list to dictionary
    #                   else create new value for city
    #       return dictionary 
    #   function to find top 5 months with greatest total pollution for \
    #   each pollutant
    #       for loop, every list in the value of dictionary, key is state
    #           get year of data
    #           if year of data matches wanted year
    #               append list of data to year list
    #       for loop for list in year list
    #           get month of data
    #           add pollution data to data month list
    #       sort month list by each pollutant from largest to smallest
    #       create list for top months for each pollutant
    #       return tuple of lists for pollutants
    #   function to display the values calculated by the other functions
    #       prints max and min pollution values
    #       for loop to print pollution totals by year for each pollutant
    #       for loop to print pollution data for each city from dictionary
    #       for loop to print top 5 months for each pollutant
    #   function to plot information of total avg pollution per year, \
    #   max and min pollution values
    #   function to prompt the user for inputs and call the other functions
    #       prompt for which state want data from
    #       while loop for when want algorithm to run
    #           if state not in dictionary, prompt again
    #           prompt for year to get data from
    #           if input quit, stop
    #           call functions to get data and display
    #           prompt if want to plot the data
    #           if statement to plot data
    #           if do not want to plot, prompts for new state
    ###########################################################

import csv
import pylab
from operator import itemgetter

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
            
def read_file(fp):  
    """Read a file and sort through the contents.
    fp: file pointer
    Returns dictionary of data."""    
        
    reader = csv.reader(fp)     #csv reader
    header = next(reader,None)
    data_dict = {}
    state = ''
    date = ''

    previous_city = ''
    previous_date = ''
        
    for line_list in reader:    #read every line
         
        
        if line_list[13] == '' or line_list[18] == '' or line_list[23] == '' or \
        line_list[28] == '':
            continue
            #record invalid if AQI is blank
            
        no2_mean_bil = float(line_list[10])     #no2 mean
        o3_mean_bil = float(line_list[15])      #o3 mean
        so2_mean_bil = float(line_list[20])     #so2 mean
        co_mean_bil = float(line_list[25])      #co mean
        
        #all mean values in parts per billion
        if "million" in line_list[9]:           
            no2_mean_bil = float(line_list[10])*1000
            
        if "million" in line_list[14]:
            o3_mean_bil = float(line_list[15])*1000
            
        if "million" in line_list[19]:
            so2_mean_bil = float(line_list[20])*1000
        
        if "million" in line_list[24]:
            co_mean_bil = float(line_list[25])*1000
  
        #record_list = city, date, no2mean, o3mean, so2mean, comean
        record_list = [line_list[7], line_list[8], \
    no2_mean_bil, o3_mean_bil, so2_mean_bil, co_mean_bil]

        state = line_list[5]
        city = line_list[7]
        date = line_list[8]
        
        #ignore duplicate records with same city and date
        if city == previous_city and date == previous_date:
            continue
        
        previous_city = city
        previous_date = date
        
        #add data as value in dictionary, state is the key
        if state in data_dict:
            data_dict[state].append(record_list)
        
        else:
            data_dict[state] = [record_list]
    
    #return the dictionary
    return data_dict

def total_years(D, state):      
    '''Calculates total pollution for each pollutant for the state over 16 years.
    D: dictionary from read_file() function
    state: state to calculate pollutant from
    Returns tuple with list of average total pollution per year per pollutant, \
    maximum and minimum pollution values of all pollutants.'''
    
    
    data_list = [[0,0,0,0] for i in range(17)]
    A_list = []
    if state in D.keys():   #if state is a key in the dictionary
        value = D[state]
        for a_list in value:    #for every list in the value
            year_int = int(a_list[1].split('/')[-1]) #year of data
            year_int = year_int%2000
        
            data_list[year_int][0] += a_list[2]    #no2mean sum
            data_list[year_int][1] += a_list[3]    #o3mean  sum
            data_list[year_int][2] += a_list[4]    #so2mean sum
            data_list[year_int][3] += a_list[5]    #comean sum
  
        
        for a_list in data_list:
            A_list.extend(a_list)   #adds contents of a_list to A_list
            
            
        max_val = max(A_list)       #maximum pollution value
    
        min_val = min(A_list)       #minimum pollution value
        
        data_tuple = (data_list, max_val, min_val)
        
        return data_tuple           #returns tuple of data
        

def cities(D, state, year):  
    '''Creates dictionary of total average pollution per city for a state and year.
    D: dictionary from read_file() function
    state: state to extract cities from
    year: year to extract data from
    Returns dictionary of cities with their pollution data.'''
    
    cities_dict = {}            
    if state in D.keys():   #if state is a key in the dictionary
        value = D[state]
        for a_list in value:    #for every list in the value
            list_year = int(a_list[1].split('/')[-1])   #year of data
            
            if year == list_year:   #year of data matches wanted year
                city = a_list[0]
                if city in cities_dict:     #if city is a key
                    
                    #add data to existing values
                    cities_dict[city][0] += a_list[2]    #no2mean sum
                    cities_dict[city][1] += a_list[3]    #o3mean  sum
                    cities_dict[city][2] += a_list[4]    #so2mean sum
                    cities_dict[city][3] += a_list[5]    #comean sum
                
                else:
                    #no current data for city, create new value
                    cities_dict[city] = a_list[2:]
            
    return cities_dict      #return the dictionary
    
def months(D,state,year):
    '''Finds top 5 months with greatest total pollution for each pollutant.
    D: dictionary from read_file() function
    state: state to extract data from
    year: year to extract data from
    Returns tuple of four lists, each has top 5 months for each pollutant.'''
    
    data = D[state]     #data is value of dictionary, key is state
    year_list = []
    for a_list in data:     
        list_year = int(a_list[1].split('/')[-1]) #year of data
        
        if year == list_year:   #year of data matches wanted year
            year_list.append(a_list) #append list of data
            
    month_list = []
    month_list = [[0,0,0,0] for i in range(12)]
    
    for a_list in year_list:
        month= (int(a_list[1].split('/')[0]))-1  #month of data
        data_month = month_list[month]
        
        data_month[0] += a_list[2]  #no2
        data_month[1] += a_list[3]  #o3
        data_month[2] += a_list[4]  #so2
        data_month[3] += a_list[5]  #co
        
    #sort list largest to smallest    
    
    #top months for no2
    month_list_sorted = sorted(month_list, key=itemgetter(0), reverse = True)
    no2_top = month_list_sorted[:5]
    no2_top = [b_list[0] for b_list in no2_top]
    
    #top months for o3
    month_list_sorted = sorted(month_list, key=itemgetter(1), reverse = True)
    o3_top = month_list_sorted[:5]
    o3_top = [b_list[1] for b_list in o3_top]
        
    #top months for so2
    month_list_sorted = sorted(month_list, key=itemgetter(2), reverse = True)
    so2_top = month_list_sorted[:5]
    so2_top = [b_list[2] for b_list in so2_top]    

    #top months for co
    month_list_sorted = sorted(month_list, key=itemgetter(3), reverse = True)
    co_top = month_list_sorted[:5]
    co_top = [b_list[3] for b_list in co_top]
    
    #tuple of lists of data
    months_top = (no2_top, o3_top, so2_top, co_top)
    
    return months_top       #return tuple
    
def display(totals_list,maxval,minval,D_cities,top_months):     
    '''Displays the values calculated by the other functions.
    totals_list: list of avg total pollution per yr per pollutant from total_years
    maxval: maximum pollution values of all pollutants from total_years
    minval: minimum pollution values of all pollutants from total_years
    D_cities: dictionary of cities with their pollution data from cities
    top_months: tuple of four lists, each has top 5 months for each pollutant \
    from months'''
    
    #print minimum and maximum pollution values
    print ("\nMax and Min pollution")
    print ("\n{:>10s}{:>10s}".format("Minval", "Maxval"))
    print ("{:>10.2f}{:>10.2f}".format(minval, maxval))   
    
    
    print ("\nPollution totals by year")
    print ("\n{:<6s}{:>8s} {:>8s} {:>8s} {:>8s}".format("Year", "NO2", \
           "O3", "SO2", "CO"))
       
    for i, data_list in enumerate(totals_list):   
        if data_list == [0,0,0,0]:
            continue
        i = i + 2001    #year of data
    
        #print pollution totals by year for each pollutant
        print ("{:<6d}{:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f}" \
        .format(i, data_list[0], data_list[1], data_list[2], data_list[3]))
    
            
    print("\nPollution by city")
    print("\n{:<16s}{:>8s} {:>8s} {:>8s} {:>8s}".format("City", "NO2", \
           "O3", "SO2", "CO"))
    
    #print pollution data for each city from dictionary
    #key is city
    for key,value in D_cities.items():
        print("{:<16s}{:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f}" \
              .format(key, value[0], value[1], value[2], value[3]))

    print("\nTop Months")
    print("\n{:>8s} {:>8s} {:>8s} {:>8s}".format("NO2", "O3", "SO2", "CO"))    

    #print top 5 months for each pollutant
    for month in range(5):
        print("{:>8.2f}{:>8.2f} {:>8.2f} {:>8.2f} " \
              .format(top_months[0][month], top_months[1][month], \
                      top_months[2][month], top_months[3][month]))

  
def plot_years(totals_list,maxval,minval):
    no2 = []
    so2 = []
    o3 = []
    co = []
    years = []

    for i in range(2000,2017):
        years.append(i)

    for i in totals_list:
        no2.append(i[0])
        o3.append(i[1])
        so2.append(i[2])
        co.append(i[3])

    fig, ax = pylab.subplots()
    pylab.ylabel('Average Concentration')
    pylab.xlabel('Year')
    pylab.title('Total Average Pollution Per Year')
    ax.plot(years,no2, 'ro')
    ax.plot(years,o3, 'bo')
    ax.plot(years,so2, 'go')
    ax.plot(years,co, 'yo')
    ax.plot(years,no2, 'ro', label='NO2')
    ax.plot(years,o3, 'bo', label='O3')
    ax.plot(years,so2, 'go', label='SO2')
    ax.plot(years,co, 'yo', label='CO')


    ax.legend(loc='upper right', shadow=True, fontsize='small')

    pylab.show()

def main():  
    """Prompts the user for inputs and calls the appropriate functions."""
     
    fp = open_file()            #open the file
    data = read_file(fp)        #dictionary from read_file

    #which state want data from
    input_state = input("Enter a state ('quit' to quit): ")
   
    while input_state.lower() !="quit":      #when input not quit
        
        #if state not in dictionary:
        if input_state not in data:
            print("Invalid state.")
            input_state = input("Enter a state ('quit' to quit): ")
            continue
        
        input_year = input("Enter a year ('quit' to quit): ")
        if str(input_year).lower() == "quit":   #if input is quit
            break
        
        input_year = int(input_year) 
        data_tuple = total_years(data, input_state) #tuple form total_years
        totals_list = data_tuple[0]     #list from data_tuple
        max_val = data_tuple[1]         #max pollution value
        min_val = data_tuple[2]         #min pollution value
        
        #dictionary of cities with their pollution data from cities
        D_cities = cities(data, input_state, input_year)
        
        #tuple of four lists, each has top 5 months for each pollutant from months
        top_months = months(data, input_state, input_year)
        
        #display the data
        display(totals_list, max_val, min_val, D_cities, top_months)

        #ask if want to plot data
        plot_input = input("Do you want to plot (yes/no)? ")
        if plot_input.lower() == "yes":
            plot_years(totals_list,max_val,min_val)
            
        elif plot_input.lower() == "no":
            #prompt for another state
            input_state = input("Enter a state ('quit' to quit): ")
            
 
if __name__ == "__main__":
    main()          
