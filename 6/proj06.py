    ###########################################################
    #  Computer Project #6
    #
    #  Algorithm
    #    function to open file and return a file pointer
    #       try and except to open correct file
    #    function to read the file
    #       for loop to read each line
    #           splits line to create list
    #           indexes the list as variables
    #           try and except for index error
    #       puts variables in list and sorts
    #   function to extract gene information for chromosome
    #       for loop to read each line
    #           indexes the list as variables
    #       puts variables in list and sorts
    #   function to extract gene information for each chromosome
    #       for loop to read each line
    #       puts variables in list and sorts
    #   function to do calculations of each gene
    #       calculates gene length
    #       calculates average length and standard deviation
    #   function to display calcultions
    #   function to prompts the user for inputs and calls the other functions
    #       while loop for correct input
    #           if statements call different functions based on input
    ###########################################################

CHROMOSOMES = ['chri','chrii','chriii','chriv','chrv','chrx']

def open_file():                    
    """Open a file.
    Returns a file pointer."""
    
    while True:
        try:
            fp=open(input("Input a file name: "))   #Open the file inputted
            return fp
        except FileNotFoundError:            #If input a file name not found
            print("Unable to open file.")
            continue

def read_file(fp):
    """Read a file and search through the contents.
    fp: file pointer
    Returns sorted list of genes."""
    
    genes_list = []
    for line in fp:                        #Read each line of the file
        if "#" not in line:                #Skip #
            try:
                data_list = line.split()     
                #Create a list by splitting at white space
                chromosome = data_list [0]    
                #List variable at index 0 is chromosome name  
                gene_start = int(data_list [3])     
                #List variable at index 1 is gene start
                gene_end = int(data_list [4])       
                #List variable at index 2 is gene end
                gene_tuple = (chromosome, gene_start,gene_end)
                genes_list.append(gene_tuple)       #add gene info to list
            except IndexError:     #If there is no data for a certain variable
                continue
    genes_list.sort()       #sort the list
    return genes_list       #return the list

def extract_chromosome(genes_list, chromosome):
    """Extract gene info for a chromosome and return in a list.
    genes_list: list of genes
    chromosome: chromosome to extract gene info of
    Returns sorted list of gene info for chromosome."""
    
    gene_info = []
    chrom_gene_list = []                   
    for gene in genes_list:
        if chromosome in gene:
            gene_end = gene[2]      #List variable at index 2 is gene end
            gene_start = gene[1]    #List variable at index 1 is gene start
            gene_info = (chromosome, gene_start, gene_end)
            chrom_gene_list.append(gene_info)   #append tuple of info
    chrom_gene_list.sort()          #Sort list
    return chrom_gene_list          #Return list

def extract_genome(genes_list):
    """Extract gene info for each chromosome and return in a list.
    genome_list: list of genes
    chromosome: chromosome to extract gene info of
    Returns sorted list of gene info for chromosome."""
    
    genome_list = []
    for chromosome in CHROMOSOMES:
        chrom_gene_list = extract_chromosome(genes_list, chromosome)
        genome_list.append(chrom_gene_list)     #append tuple of info
    genome_list.sort()             #sort list      
    return genome_list
    
def compute_gene_length(chrom_gene_list):
    """Computes the gene length and standard deviation.
    chrom_gene_list: list of genes for a specific chromosome
    Returns average gene length and standard deviation."""
    
    gene_sum = 0
    gene_number = 0
    gene_length = []
    for gene in chrom_gene_list:
        gene_end = gene[2]      #List variable at index 2 is gene end
        gene_start = gene[1]    #List variable at index 1 is gene start
        gene_length.append(gene_end - gene_start +1)  #calculate length
        gene_number += 1    #count of number of genes
        
    gene_mean = sum(gene_length) / len(gene_length)  #calculate average length
    for gene_len in gene_length:
        gene_calc = (gene_len-gene_mean)**2
        gene_sum += gene_calc                   #calculate standard deviation
    gene_stddev = (gene_sum / gene_number) ** (1/2)   
    gene_tuple = (gene_mean, gene_stddev)
    return gene_tuple       #return average gene length and standard deviation
    
 
def display_data(chrom_gene_list, chrom):
    """Displays the chromosome name, the average length of the gene and the 
    standard deviation.
    chrom_gene_list: list of genes for a specific chromosome
    chrom: string name"""
    
    gene_mean, gene_stddev = compute_gene_length(chrom_gene_list)   
    #values from function
    chrom_name = chrom[:3].lower() + chrom[3:].upper()
    print ("{:<11s}{:9.2f}{:9.2f}".format(chrom_name, gene_mean, gene_stddev))
    #print values              
                                                           
def main():
    """Prompts the user for inputs and calls the appropriate functions."""
    
    print ("Gene length computation for C. elegans.\n")
    fp = open_file ()               #open file
    genes_list = read_file(fp)      #read file
    chromosome = ""
    while chromosome != "quit": 
        chromosome = input("\nEnter chromosome or 'all' or 'quit': ")   #input 
        chromosome = chromosome.lower()
        
        if chromosome == "all":   #extract and display data for all chromosomes
            genome = extract_genome(genes_list)
            print ("\nChromosome Length")             
            print ("{:<11s}{:>9s}{:>9s}".format("chromosome", "mean", "std-dev"))
            for data in genome:
                display_data(data, data[0][0])
        elif chromosome in CHROMOSOMES:  
            #extract and display data for specific chromosome
            data = extract_chromosome(genes_list, chromosome)   
            print ("\nChromosome Length")             
            print ("{:<11s}{:>9s}{:>9s}".format("chromosome", "mean", "std-dev"))
            display_data(data, chromosome)     
        elif chromosome == "quit":
            break
        else:           #If input not a chromosome, "all", or "quit"
            print("Error in chromosome.  Please try again.")


if __name__ == "__main__":
    main()
