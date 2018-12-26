    ###########################################################
    #  Computer Project #11
    #
    #  Algorithm
    #   class to define a cell component of a CSV
    #       function to initialize the object and its attributes
    #       function to build a formatted string for printing the value
    #           calls on functions to get the width and special formatting
    #           builds formatted string for printing the value
    #       function to return the value from __str__
    #       function to redefine the cell's alignment attribute
    #           cell's alignment attribute is the parameter align
    #       function to return the value from __alignment
    #       function to redefine the cell's value attribute
    #           cell's value attribute is the parameter value
    #       function to return the value from __value
    #   class to process a csv file and store its data for output
    #       function to initialize the worker class
    #           if there is a file pointer, calls on read_file
    #       function to iterate over a file object and store the data
    #           for loop for every row
    #               for loop for every cell in the row
    #                   replace NULL with empty string
    #                   stores width of item
    #               calculates number of columns
    #           set all values in special to be None
    #       function to overload the [] operator to access values in __data
    #       function to overload the [] operator to set values in __data
    #       function to overload the __str__ method to convert data to a string
    #       function to return the value of __str__
    #       function to print the maximum of limit number of lines
    #           if there is no limit, print the data
    #           converts data to string for every line up to limit
    #       function to remove a row of data at an index
    #           reduces the number of rows
    #       function to set the width of the column of __data at index
    #       function to get information about the width of the column
    #       function to linkn special formatting function to the column
    #       function to get special formatting function assigned to the column
    #       function to set the alignment of a specific column
    #       function to get number of columns in the CsvWorker object
    #       function to get number of rows in the CsvWorker object
    #       function to create a new CsvWorker object that is a minimized version
    #           creates list of data same length as number of rows
    #           creates list of widths of each column to add to new CsvWorker
    #           appends cell to list of data
    #           gets special for each cell in columns
    #           adds data to new CsvWorker
    #       function to write the data into a CSV file names by the parameter
    #           writes rows into CSV files until reaches limit
    #       function to write data into a text file
    #           write using the limited_str method
    #       function to find the cell with the minimum value in a column
    #           ensures the cell value is a number
    #           determines cell with minimum value
    #           if cell value is not a number, skip
    #       function to find the cell with the maximum value in a column
    #           ensures the cell value is a number
    #           determines cell with maximum value
    #           if cell value is not a number, skip
    #       function to open a file
    #           open the file inputted
    #           if input a file name not found, reprompt
    #       function to print the value in percentage form
    #           converts the value to a float then prints as a percentage
    #           just print the value if cannot convert to float
    #       function to print the value in a currency form
    #           converts the value to a float then prints as a currency
    #           just print the value if cannot convert to float
    #       function to call on other functions
    #           opens and minimizes a csv file
    #           sets formatting
    #           writes file to a text and csv format
    #           checks maximum and minimum ACTs and Earnings
    ###########################################################
    
import csv
class Cell(object):
    '''Defines a cell component of a CSV.
    '''
    
    def __init__(self, csv_worker = None, value = '', column = 0, alignment = '^'):
        '''Initializes the object and its attributes.
        self: instance of the class
        csv_worker: spreadsheet cell is in
        value: value in the cell
        column: column of the cell
        alignment: alignment formatting 
        '''
        self.__csv_worker = csv_worker  
        self.__value = value            
        self.__column = column          
        self.__alignment = alignment    
    
    def __str__(self):                                            
        '''Builds a formatted string for printing the value.
        self: instance of the class
        Returns formatted string.
        '''
        WWW = self.__csv_worker.get_width(self.__column)
        #get cell width
        special = self.__csv_worker.get_special(self.__column)
        #formatting special values
        if special:
            val = special(self.__value)
        else:
            val = self.__value
        #formatted string
        S = "{:{align}{width}}".format(val, align=self.__alignment, width=WWW) 
        return S                        #return string

    def __repr__(self):
        '''Calls on __str__ and returns the value.
        self: instance of the class
        Returns a shell representation of a Cell object.
        '''
        return self.__str__()
    
    def set_align(self, align):   
        '''Redefines cell's alignment attribute from the parameter.
        self: instance of the class
        align: alignment string, left/right/center
        '''                                         
        self.__alignment = align
        #cell's alignment attribute is the parameter align
        
    def get_align(self): 
        '''Calls on __alignment and returns the value.
        self: instance of the class
        Returns the object's alignment.
        '''                                           
        return self.__alignment
    
    def set_value(self, value):   
        '''Redefines cell's value attribute from the parameter.
        self: instance of the class
        value: new value attribute
        '''                                         
        self.__value = value
        #cell's value attribute is the parameter value
        
    def get_value(self):                 
        ''' Calls on __value and returns the value.
        self: instance of the class
        Returns the object's value.
        '''                           
        return self.__value

class CsvWorker(object):
    '''Takes a csv file as input and processes it, then stores its data for output. 
    '''
    
    def __init__(self, fp = None):
        '''Initializes the worker class.
        self: instance of the class
        fp: file pointer
        '''

        self.__columns = 0
        self.__rows = 0
        self.__data = []    #list of lists of all cells in spreadsheet
        self.__widths = []  #lists of widths of columns
        self.__special = []     #list of special formatting instructions
        #if there is a file pointer
        if fp:
            self.read_file(fp)
    
    def read_file(self, fp):                                            
        '''Iterate over a file object and store the data.
        self: instance of the class
        fp: file pointer
        '''
        reader = csv.reader(fp)
        for line_list in reader:    #loop for every row
            data_list = []
            column_count = 0        #number of columns
            self.__rows += 1        #number of rows
            
            for item in line_list:  #item = cell
                if item == "NULL":  #if the value is "NULL"
                    item = ""
                    
                if len(self.__widths) <= column_count:
                    self.__widths.append(0)
                    #number of widths based on number of columns
                    
                if len(item) > self.__widths[column_count]:
                    self.__widths[column_count] = len(item)
                    #stores width of the item
                
                c = Cell(self,item,column_count)
                data_list.append(c)     #list of cells in row
                column_count += 1
                
            if column_count > self.__columns:
                self.__columns = column_count   #number of columns
            self.__data.append(data_list) #list of lists, list is cells in row
            
        for i in range(self.__columns):
            self.__special.append(None)
            #all values in special should be None

        fp.close()
    
    def __getitem__(self, index):
        '''Overloads the [] operator to access values in __data.
        self: instance of the class
        index: index of data to access
        Returns object's data at the index.
        '''
        return self.__data[index]
    
    def __setitem__(self, index, value):
        '''Overloads the [] operator to set values in __data.
        self: instance of the class
        index: index of data to access
        value: value to set in __data
        '''
        self.__data[index] = value
    
    def __str__(self):    
        '''Overload the __str__ method to convert the class data to a string.
        self: instance of the class
        Returns string of cells and carriage returns
        '''                                        
        my_string = ''
        for row in self.__data:
            for cell in row:
                my_string += str(cell)  #converts class data to string
            my_string += '\n'           #carriage return to each row
        return my_string
    
    def __repr__(self):
        '''Calls on __str__ and returns the value.
        self: instance of the class
        Returns a shell representation of a Cell object.
        '''
        return self.__str__()
    
    def limited_str(self, limit): 
        '''Prints maximum of limit number of lines. 
        self: instance of the class
        limit: how many lines to print
        Returns either the data or a string of cells and carriage returns
        '''                                     
        count = 0    
        result = ''
        if limit == None:           #if there is no limit, print the data
            return str(self)
        for row in self.__data:
            for column in row:
                result += str(column)   #converts data to string
            count += 1                  #line count
            result += '\n'              #carriage return
            if count >= limit:          #once reach line limit
                break
        return result               
    
    def remove_row(self, index):
        '''Removes a row of data at an index.
        self: instance of the class
        index: row of data to remove
        Returns data without the row at the index
        '''
        self.__data.pop(index)  #remove the row at the index
        self.__rows -= 1        #reduce the number of rows
        return self.__data
    
    def set_width(self, index, width):      
        '''Sets width of the column of __data at index.
        self: instance of the class
        index: index of column to alter
        width: new width value of the column
        '''                        
        self.__widths[index] = width

    def get_width(self, index):                
        '''Gets information about the width of the column.
        self: instance of the class
        index: index of column
        Returns width of the column at index.
        '''                            
        return self.__widths[index]

    def set_special(self, column, special):
        '''Links special formatting function to the column.
        self: instance of the class
        column: column to assign to
        special: formatting function 
        '''
        self.__special[column] = special

    def get_special(self, column):
        '''Gets special formatting function assigned to the column.
        self: instance of the class
        column: column to get information of
        Returns special formatting function assigned to a column.
        '''
        return self.__special[column]

    def set_alignment(self, column, align):   
        '''Sets the alignment of a specific column.
        self: instance of the class
        column: column to set
        align: alignment of column
        '''                          
        if align != '<' and align != '>' and align != '^':
            raise TypeError
            #if the alignment is not left, right, center
            
        for row in self.__data:
            row[column].set_align(align)     
            #set alignment of column                      
    
    def get_columns(self):   
        '''Gets number of columns in the CsvWorker object.
        self: instance of the class
        Returns number of columns in the CsvWorker object.
        '''                                         
        return self.__columns
    
    def get_rows(self):  
        '''Gets number of rows in the CsvWorker object.
        self: instance of the class
        Returns number of rows in the CsvWorker object.
        '''                                          
        return self.__rows
    
    def minimize_table(self, columns):   
        '''Creates a new CsvWorker object that is a minimized version \
        of the original.
        self: instance of the class
        columns: columns to add to the new CsvWorker object
        Returns the new CsvWorker object.
        '''
        new_csvworker = CsvWorker()     #create new CsvWorker
        new_list = []
        for rows in self.__data:
            new_list.append([])     
            #creates list of data same length as number of rows
        
        new_widths = []
        for i in columns:                          
            new_widths.append(self.__widths[i])     
            #creates list of widths of each column to add to new CsvWorker object
         
        new_csvworker.__widths = new_widths
        
        for i, row in enumerate(self.__data):
            column_count = 0
            for column in columns:
                cell = Cell(new_csvworker, value = row[column].get_value(), \
                    column = column_count, alignment = row[column].get_align())
                #creates cell
                column_count += 1
                new_list[i].append(cell)
                #append cell to list of data
                
        new_special = []
        
        for i in columns:
            new_special.append(self.__special[i])
            #get special for each in columns
        
        #add data to new CsvWorker
        new_csvworker.__special = new_special
        new_csvworker.__data = new_list
        new_csvworker.__rows = self.__rows
        new_csvworker.__columns = len(columns)
        
        return new_csvworker
        
    def write_csv(self, filename, limit = None):  
        '''Writes the data into a CSV file named by the filename parameter.
        self: instance of the class
        filename: name of CSV file
        limit: limits the number of rows to write in the CSV file
        '''                       
        fp = open(filename, "w", encoding = "utf-8")
        count = 0    
                
        result = ''

        for row in self.__data:
            for column in row:
                result += column.get_value() + ","  #make a CSV
            count += 1
            result = result[:-1]    #remove end comma
            result += '\n'          #add carriage return
            if limit and count >= limit:    #once reach row limit
                break
            
        fp.write(result)    #write data into file

        fp.close()
    
    def write_table(self, filename, limit = None):      
        '''Writes the data into a tabular formatted text file named filename. 
        self: instance of the class
        filename: name of CSV file
        limit: limits the number of rows to write in the CSV file
        '''                  
        fp = open(filename, "w")
        fp.write(self.limited_str(limit))   #write using the limited_str method
        fp.close()
        
    def minimum(self, column):   
        '''Finds the cell with the minimum value in a column.
        self: instance of the class
        column: column of cells
        Returns the cell with the minimum value of a column.
        '''                                         
        min_value = 100000000
        min_cell = None
        for row in self.__data:
            cell = row[column]
            try:
                value = float(cell.get_value())     
                #Ensure the cell value is a number
                if value < min_value:
                    min_value = value   #determine minimum value
                    min_cell = cell     #determine cell with minimum value

            except ValueError:          #if cell value is not a number, skip
                continue
        return min_cell
    
    def maximum(self, column):
        '''Finds the cell with the maximum value in a column.
        self: instance of the class
        column: column of cells
        Returns the cell with the maximum value of a column.
        '''                                            
        max_value = 0
        max_cell = None

        for row in self.__data:
            cell = row[column]
            try:
                value = float(cell.get_value())
                #Ensure the cell value is a number
                if value > max_value:
                    max_value = value   #determine the maximum value
                    max_cell = cell     #determine cell with maximum value

            except ValueError:          #if cell value is not a number, skip
                continue
        return max_cell                                      

def open_file():
    """Open a file.
    Returns a file pointer."""
    
    while True:
        try:
            filename = input("Input a file name: ")   #Open the file inputted
            fp = open(filename, encoding="utf-8")
            return fp
        except FileNotFoundError:            #If input a file name not found
            print("File not found. Try again")
            continue

def percentage(value):
    '''Print value in percentage form.
    value: value to print
    Returns either formatted value or original value.
    '''
    try:
        value = float(value)    #make the value a float
        return "{:.1f}%".format(value)  #percentage form
        
    except ValueError:  #if not a float
        return value

def currency(value):
    '''Print value in currency form.
    value: value to print
    Returns either formatted value or original value.
    '''
    try:
        value = float(value)    #make the value a float
        return "${:,.2f}".format(value)     #currency form
        
    except ValueError:  #if not a float
        return value

def main():                                                            
    '''
    Opens and minimizes a csv file 
    Sets formatting
    Writes file to a text and csv format
    Checks maximum and minimum ACTs and Earnings
    '''
    fp = open_file()
    
    master = CsvWorker(fp)  #creates csv
    
    csv_worker = master.minimize_table([3,5,40,55,116,118,122])     
    #minimizes csv
    
    csv_worker.set_special(3, percentage)
    csv_worker.set_special(6, percentage)
    csv_worker.set_special(4, currency)
    csv_worker.set_special(5, currency)
    #formats columns of csv worker
    
    for i in range(len(csv_worker[0])):
        csv_worker.set_width(i, csv_worker.get_width(i) + 4)
        #sets width at index
    
    csv_worker.write_table("output.txt",10)
    csv_worker.write_csv("output.csv", 10)
    #writes table and csv with limit 10

    max_act = csv_worker.maximum(2)
    min_act = csv_worker.minimum(2)
    #finds min and max act scores
    
    max_earn = csv_worker.maximum(4)
    min_earn = csv_worker.minimum(4)
    #finds min and max earnings
    
    #prints values
    print("Maximum ACT:", str(max_act).strip())
    print("Minimum ACT:", str(min_act).strip())
    print("Maximum Earnings:", str(max_earn).strip())
    print("Minimum Earnings:", str(min_earn).strip())

if __name__ == "__main__":
    main()
