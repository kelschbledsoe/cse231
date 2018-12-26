    ###########################################################################
    #  Computer Project #4
    #
    #  Algorithm
    #    function to find the multiplicative inverse for A given M
    #    function to check if two numbers are co-primes
    #    function to find the smallest co-prime for a number
    #    functions to encrypt and decrypt Caesar Cipher and Affine Cipher
    #    function to encrypt or decrypt a string using Caesar and Affine Cipher
    ###########################################################################
    
import math,string
PUNCTUATION = string.punctuation
ALPHA_NUM = string.ascii_lowercase + string.digits

def multiplicative_inverse(A,M):
    '''Return the multiplicative inverse for A given M.
       Find it by trying possibilities until one is found.'''
       
    for x in range(M):
        if (A*x)%M == 1:
            return x
  
def check_co_prime(num, M):
    '''Check if two numbers are co-primes. 
    num: integer to evaluate
    M: upper integer to evaluate
    Returns: True if num and M are co-primes.'''
    GCD = math.gcd(num,M)   #define GCD as math.gcd
    if GCD == 1:            #co-primes are two numbers whose GCD is 1
        return True
    else:
        return False
        
def get_smallest_co_prime(M):
    '''Finds the smallest co-prime number of M. 
    M: integer to find the smallest co-prime of
    Returns: The smallest co-prime of M.'''
    num = 2     #1 cannot be a co-prime
    while num != M:     #co-prime cannot be the same number
        if check_co_prime(num,M) == False:  #see if the numbers are co-primes
            num += 1    #find the smallest co-prime, starting from 2
        else:
            return num  #return the smallest co-prime
        
def caesar_cipher_encryption(ch,N,alphabet):
    '''Caesar Cipher encryption of a character.
    ch: character to encrypt
    N:rotation
    alphabet: string containing ch
    Returns: the encrypted character.'''
    x = alphabet.find(ch)   #x is the index of ch in the alphabet
    M = len(alphabet)       #M is the length of the alphabet
    index = (x+N) % M       #formula for the index of the cipher char
    cipher_char = alphabet[index]   
    #use the index to get the cipher char from the alphabet
    return cipher_char      #return the encrypted char

def caesar_cipher_decryption(ch,N,alphabet):
    '''Caesar Cipher decryption of a character. 
    ch: character to encrypt
    N:rotation
    alphabet: string containing ch
    Returns: the decrypted character.'''
    x = alphabet.find(ch)   #x is the index of ch in the alphabet
    M = len(alphabet)       #M is the length of the alphabet
    index = (x-N) % M       #formula for the index of the cipher char
    plain_char = alphabet[index]
    #use the index to get the cipher char from the alphabet
    return plain_char       #return the decrypted char
        
def affine_cipher_encryption(ch,N,alphabet):
    '''Affine Cipher encryption of a character.
    ch: character to encrypt
    N:rotation
    alphabet: string containing ch
    Returns: the encrypted character.'''
    x = alphabet.find(ch)   #x is the index of ch in the alphabet
    M = len(alphabet)       #M is the length of the alphabet
    A = get_smallest_co_prime(M)    #A is the smallest co-prime of M
    index = (A*x+N) % M     #formula for the index of the cipher char
    cipher_char = alphabet[index]
    #use the index to get the cipher char from the alphabet
    return cipher_char      #return the encrypted char

def affine_cipher_decryption(ch,N,alphabet):
    '''Affine Cipher decryption of a character.
    ch: character to encrypt
    N:rotation
    alphabet: string containing ch
    Returns: the decrypted character.'''
    x = alphabet.find(ch)   #x is the index of ch in the alphabet
    M = len(alphabet)       #M is the length of the alphabet
    A = get_smallest_co_prime(M)    #A is the smallest co-prime of M
    B = multiplicative_inverse(A,M) #B is the multiplicative inverse of A and M
    index = B*(x-N) % M     #formula for the index of the cipher char
    plain_char = alphabet[index]
    #use the index to get the cipher char from the alphabet
    return plain_char       #return the decrypted char
    
def main():    
    '''Utilize the functions to encrypt or decrypt an inputted string.'''
    command = ""
    
        
    N = input("Input a rotation (int): ")
    while not N.isdigit():  #N cannot be a string
        print ("Error; rotation must be an integer.")
        N = input("Input a rotation (int): ")
        
    N = int(N)  #N must be an integer, not a float
    
    while command != "q":   
        #the input is not "quit"
        
        command = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
       
        cipher_text_e = ""
        plain_text_d = ""
        
        if command == "e":  #encryption
            string_e = input("Input a string to encrypt: ")
            
            for char in string_e.lower():
                if char.isalpha() or char.isdigit():    
                #use affine if char is a letter or digit
                    cipher_text_e += affine_cipher_encryption(char,N,ALPHA_NUM) 
                elif char == " ":
                #cannot encrypt spaces
                    print ("Error with character:")
                    print ("Cannot encrypt this string.")
                    break 
                else:
                #use caesar if char is punctuation
                    cipher_text_e += caesar_cipher_encryption(char,N,PUNCTUATION)
            else:
                print ("Plain text:", string_e)     #print input
                print ("Cipher text:", cipher_text_e)   #print encryption

        elif command == "d":    #decryption
            string_d = input("Input a string to decrypt: ")
            
            for char in string_d.lower():
                if char.isalpha() or char.isdigit():
                #use affine if char is a letter or digit
                    plain_text_d += affine_cipher_decryption(char,N,ALPHA_NUM) 
                elif char == " ":
                #cannot decrypt spaces
                    print ("Error with character:")
                    print ("Cannot decrypt this string.")
                    break 
                else:
                #use caesar if char is punctuation
                    plain_text_d += caesar_cipher_decryption(char,N,PUNCTUATION)
            else:
                print ("Cipher text:", string_d)    #print input
                print ("Plain text:", plain_text_d) #print decryption
        
        elif command == "q":    #exit loop since inputted "quit"
            break
        else:
            print ("Command not recognized.")   #if e, d, or q is not inputted
            command = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
                
if __name__ == "__main__":
    main()

