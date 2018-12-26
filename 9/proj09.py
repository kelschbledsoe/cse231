    ###########################################################
    #  Computer Project #9
    #
    #  Algorithm
    #    function to open file and return a file pointer
    #       try and except to open correct file
    #    function to decrypt text
    #       creates list of keys for dictionary from ciphertext
    #       try and except to add key and value to dictionary
    #           value from plaintext
    #       IndexError when no more characters in plaintext to add to dict
    #       try and except to decrypt text using dictionary
    #           for loop to split textodecrypt using bifurcation
    #               decrypted text is value from dict with texttodecrypt as key
    #       KeyError if text not in dictionary, prints error
    #    function to create dictionary of data, prints the most frequent quadgrams
    #       for loop to get quadgrams and their counts from the data
    #           determine sum of all quad counts
    #           add quadgrams and their counts to dictionary
    #       for loop to extract data from dict to calculate log probability
    #           calculate log probability
    #           add log probability to value of quadgram in dictionary
    #       for loop to extract data from dict to create tuple for sorting
    #           append tuple of data to list
    #       sort list of data tuples
    #       prints top ten most frequent quadgrams
    #       returns dictionary of quadgrams and their counts
    #    function to decrypt ciphertext and determine solution with log fitness
    #       loop for each key
    #           loop through ciphertext
    #               add decoded character to plain text solution
    #           calculate fitness score of plaintext from fitness_calculator
    #           append tuple of fitness score, decryption, key to list
    #       sort list on fitness score to get most accurate decryption attempt
    #       print key, first 35 char of decryption, fitness score of top 5
    #       print most accurate decryption based on fitness score
    #    function to calculate sum of fitness values of quadgrams
    #       while loop for correct quadgram length
    #           get quadgrams from plaintext, determine length
    #               get log probability for quadgram from dictionary
    #               sum of log probabilities is fitness value of plaintext
    #           if quadgram length is not 4, break
    #       return fitness value of plaintext
    #    function to prompt the user for inputs and call the other functions
    #       input for which functions to use
    #       while loop to check for valid input
    #           if input is "1", chosen plaintext attack
    #               input needed parameters
    #               calls chosen_plaintext_attack to decrypt text
    #           if input is "2", Ngram frequency analysis attack
    #               dictionary from log_probability_dictionary
    #               input for ciphertext
    #               remove punctuation, spaces, and make ciphertext uppercase
    #               call on bruteforce_shift_cipher to decrypt ciphertext
    ###########################################################

from math import log10
import string

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


def chosen_plaintext_attack(plaintext, ciphertext, bifurcation, texttodecrypt):
    """Decrypts text using a dictionary built with other inputs.
    plaintext: text that is the correct translation
    ciphertext: corresponding ciphertext to plaintext
    bifurcation: size of each key in dictionary from ciphertext 
    texttodecrypt: text to decrypt using other inputs
    """
    
    map_dict = {}
    n=0
    #creates list of keys for dictionary from ciphertext. 
    #bifurcation is length of each key
    key_list = [ciphertext[i:i+bifurcation] for i in range(0, len(ciphertext),\
                bifurcation)]
    
    #try and except to add key and value to dictionary. 
    try:
        for value in key_list:      #each key in the list             
            dict_key = value
            dict_value = plaintext[n]  #value is each character from plaintext. 
            n+=1
            #assign each key and value to dictionary
            map_dict[dict_key] = dict_value   
    except IndexError:    #IndexError when assigned each character of plaintext
        pass
    
    decryptedtext = ""
        
        #print decrypted in the try statement
    try:
        for i in range(0,len(texttodecrypt),bifurcation):
            #getting length of text based on bifurcation
            text = texttodecrypt[i:i+bifurcation]
            #decrypted text is value from dictionary corresponding to text
            decryptedtext += map_dict[text]
        
        print ("\nDecrypted text:", decryptedtext)               

    except KeyError:    #if key not in dictionary
        print ("Decryption interrupted. Key not found: ", text )
    
def log_probability_dictionary(fp):
    """Read a file, creates dictionary of data, prints the most frequent quadgrams.
    fp: file pointer
    Returns a dictionary of quadgrams and their counts.
    """

    #letters are quadgram, numbers are count, use equation for prob
    quadgram_dict = {}
    data_list = []
    total_quad = 0
    for line in fp:                 
        line_list = line.strip().split()
        quad = line_list[0]             
        count = int(line_list[1])
        total_quad += count             #determine sum of all quad counts
        quadgram_dict[quad] = [count]    
        #key is quadgram, count is value

    #loop through dict, extract key and value to calculate log probability
    for key,value in quadgram_dict.items():
        #key is quadgram, value is count
        log_prob = log10(int(value[0]) / total_quad) #calculate log probability
        
        new_value = [int(value[0]), log_prob] #quadgram count, log probability
        quadgram_dict[key] = new_value  #new_value is now the value in the dict

    #loop through dict, extract data to create tuple of data for sorting
    for key,value in quadgram_dict.items():
        data_tuple = (value[0], key, value[1])    #count, quad, log probability
        data_list.append(data_tuple)        #creates list of tuples
    
    #sorts list to give top ten most frequent quadgrams
    data_list = sorted(data_list, reverse = True)[:10]  
    
    print("\n{:<8s}{:>13s}{:>22s}".format('Quadgram','Count','Log Probability'))
    print("-------------------------------------------")     
    
    for tup in data_list:       
        #prints quadgram, count, log probability of top ten quadgrams
        print("{:<8s}{:>13d}{:>22.6f}".format(tup[1],tup[0],tup[2]))
        
    return quadgram_dict     #returns dictionary of quadgrams and their counts
    
def bruteforce_shift_cipher(ciphertext, ngrams_dictionary):
    """Attempts to decrypt ciphertext at each key and determines potential \
    solution with the log fitness of each attempt.
    ciphertext: text to decipher
    ngrams_dictionary: dict of quadgrams and their counts and log probabilities
    """
    
    fitness_list = []
    alphabet = string.ascii_uppercase
    for i in range (26):        #loop for each key
        plain_text = ''
        for ch in ciphertext:           #loop through ciphertext
            index = alphabet.find(ch)   #index is location of ciphertext in alphabet
            decoded_ch = alphabet[(index + i) % 26]
            #add decoded character to plain_text solution
            plain_text += decoded_ch      
        #calculate fitness_score of plaintext from fitness_calculator
        fitness_score = fitness_calculator(plain_text, ngrams_dictionary) 
        #tuple of fitness score, decryption, key
        tup = (fitness_score, plain_text, i)
        fitness_list.append(tup)
    #sort list on fitness score to get most accurate
    fitness_list.sort(reverse = True) 
            
    print("{:<5s}{:^35s}   {:>10s}".format("\nKey", "Plaintext", "Fitness")) 
    print("------------------------------------------------------") 

    for i in range(5):      #top 5
        #print key, first 35 characters of decryption, fitness score
        print("{:<5d}{:^35s}   {:>10.4f}".format(fitness_list[i][2], \
              fitness_list[i][1][:35], fitness_list[i][0]))
    key_input = input("\npress any key to continue...")
    
    #print most accurate decryption based on fitness score
    print ("\nDecrypted ciphertext: ", fitness_list[0][1])
        
def fitness_calculator(potential_plaintext, quadgram_dictionary): 
    """Calculates sum of the fitness values of quadgrams in plaintext.
    potential_plaintext: a string that is the possible plaintext of ciphertext
    quadgram_dictionoary: dict of quadgrams and their counts and log probability
    Returns the overall log fitness value of the plaintext
    """
    quad_length = 4
    n = 0
    log_prob = 0
    prob_sum = 0
    while quad_length == 4:
        quadgram = potential_plaintext[n:n+4]  #get quadgrams from plaintext
        quad_length = len(quadgram)
        if quad_length == 4:    #quadgram is four characters
            n += 1
            if quadgram in quadgram_dictionary.keys():  #quadgram in dict
                #log probability from dictionary
                log_prob = quadgram_dictionary[quadgram][1] 
                #sum of log probabilities is fitness value of plaintext
                prob_sum += log_prob
        else:   #no more quadgrams in plaintext
            break
        
    return prob_sum     #fitness value of the plaintext

def main():
    """Prompts the user for inputs and calls the appropriate functions."""
    
    BANNER = """\
    ------------------------------------------------------------------------
    Welcome to the world of code breaking. This program is meant to help
    decipher encrypted ciphertext in absence of knowledge of algorithm/key.
    ------------------------------------------------------------------------
    """
    MENU = """\
    1. Chosen plaintext attack
    2. Ngram frequency analysis
    """
    
    print (BANNER)
    print(MENU)
    choice_input = input("Choice: ")    #choose which functions to use
    
    while choice_input != "1" and choice_input != "2":
        #ensure proper input
        print("Invalid input.")
        choice_input = input("Choice: ")
        
    if choice_input == "1":     #chosen plaintext attack
        #input needed parameters
        plaintext_input = input("Plaintext: ")
        ciphertext_input = input("Ciphertext: ")
        b_size_input = int(input ("Bifurcation: "))
        text_to_decrypt_input = input("Text to decrypt: ")
        #calls chosen_plaintext_attack to decrypt text
        chosen_plaintext_attack(plaintext_input, \
            ciphertext_input, b_size_input, text_to_decrypt_input)
    
    elif choice_input == "2":   #Ngram frequency analysis attack
        fp = open_file()
        #dictionary from log_probability_dictionary
        quadgram_dict = log_probability_dictionary(fp)
        ciphertext_input = input("Ciphertext: ")
        #remove punctuation
        for ch in string.punctuation:
            ciphertext_input = ciphertext_input.replace(ch,"")
        #remove spaces
        ciphertext_input = ciphertext_input.replace(' ', '') 
        #make ciphertext uppercase
        ciphertext_input = ciphertext_input.upper()
        #call on bruteforce_shift_cipher to decrypt ciphertext
        bruteforce_shift_cipher(ciphertext_input, quadgram_dict)
        
if __name__ == "__main__":
    main()
