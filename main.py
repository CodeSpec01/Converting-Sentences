# Function to start the program from console -----------------------------------------------------------------------------------------------------------------------
def start(start_over):
  while start_over != "a" and start_over != "n" and start_over != "h" and start_over != "e" and start_over != "i":
    start_over = input("Please Enter either (A) or (N) to convert messages. Enter (H) for help and (E) to exit: ").lower()
  return start_over

  
# The Help Menu -----------------------------------------------------------------------------------------------------------------------------------------------------
def help(start_over):
  if start_over == "h" :
    print("\nThe Help Menu -----------------------------------------------------------------")
    print("Type (A) to convert sentence from alphabet to numbers \nType (N) to convert numbers into alphabet \nType (H) for help and information \nType (E) if you want to exit the code \n▶ The letters can be written as capital or small.")
    print("\nWhile converting sentence from alphabet to numbers you just have to write the sentence like (Hello There) ")
    print("While converting sentence from numbers to alphabet put (-) after each letter as number and (*-) as space between 2 words as number. For example (Hello There => 8-5-12-12-15-*-20-8-5-18-5)")
    print("\nFor information on how the program works press (I)\n")
  
    # Asking the user to continue , change or stop converting -------------------------------------------------------------------------------------------------------
    start_over = input("Enter (A) or (N) to convert. Enter (H) for help and (E) to exit: ").lower()

    # Makes the question to be asked again if user input wrong letter ----------------------------------------------------------------------------------------------------
    if start_over != "a" and start_over != "n" and start_over != "h" and start_over != "e" and start_over != "i":
      start_over = start(start_over)
    
    # Main sending to help menu ---------------------------------------------------------------------------------------------------------
    if start_over == "h":
      start_over = help(start_over)
    
    # Main sending to information menu ---------------------------------------------------------------------------------------------------------------
    if start_over == "i":
      start_over = information(start_over)
    
    # Main sending from Alphabet to numbers menu -------------------------------------------------------------------------------------------
    if start_over == "a":
      start_over = alphabet_to_number(start_over)
    
    # Main sending from numbers to alphabets menu -------------------------------------------------------------------------------------------
    if start_over == "n":
      start_over = number_to_alphabet(start_over)

# The Information Menu ----------------------------------------------------------------------------------------------------------------------------------------------
def information(start_over):
  if start_over == "i":
    print("\nThis is a basic program used to convert numbers into alphabets and alphabets into numbers via a simple dictionary.")
    print('The program converts alphabets and numbers conversion is done like this -')
    print('"a" is converted into "1" and "1" is converted into "a" and similarly in alphabetical order from a as 1 to z as 26.')
    print("\nFor more information , doubts or suggestions feel free to mail me at online.codespec@gmail.com\n")
  
    # Asking the user to continue , change or stop converting -------------------------------------------------------------------------------------------------------
    start_over = input("Enter (A) or (N) to convert. Enter (H) for help and (E) to exit: ").lower()
  
    # Makes the question to be asked again if user input wrong letter ----------------------------------------------------------------------------------------------------
    if start_over != "a" and start_over != "n" and start_over != "h" and start_over != "e" and start_over != "i":
      start_over = start(start_over)
    
    # Main sending to help menu ---------------------------------------------------------------------------------------------------------
    if start_over == "h":
      start_over = help(start_over)
    
    # Main sending to information menu ---------------------------------------------------------------------------------------------------------------
    if start_over == "i":
      start_over = information(start_over)
    
    # Main sending from Alphabet to numbers menu -------------------------------------------------------------------------------------------
    if start_over == "a":
      start_over = alphabet_to_number(start_over)
    
    # Main sending from numbers to alphabets menu -------------------------------------------------------------------------------------------
    if start_over == "n":
      start_over = number_to_alphabet(start_over)


# Actual Code of changing alphabets to Numbers -----------------------------------------------------------------------------------------------------------------------
def alphabet_to_number(start_over):
  
  #  Using try and except to counter key error -----------------------------------------------------------------------------------------------------------------------
  try:

    # The Alphabet to numbers Dictionary -----------------------------------------------------------------------------------------------------------------------------
    alphabet_to_number_dictionary = {
      "a" : "1-",
      "b" : "2-",
      "c" : "3-",
      "d" : "4-",
      "e" : "5-",
      "f" : "6-",
      "g" : "7-",
      "h" : "8-",
      "i" : "9-",
      "j" : "10-",
      "k" : "11-",
      "l" : "12-",
      "m" : "13-",
      "n" : "14-",
      "o" : "15-",
      "p" : "16-",
      "q" : "17-",
      "r" : "18-",
      "s" : "19-",
      "t" : "20-",
      "u" : "21-",
      "v" : "22-",
      "w" : "23-",
      "x" : "24-",
      "y" : "25-",
      "z" : "26-",
      " " : "*-",
    }

    # Asking for user input (The message to be converted in alphabet form) ------------------------------------------------------------------------------------------
    user_input = input("Please Enter a message: ").lower()
  
    output = ""

    # Using the dictionary to find the key value pair of the letter from the user input above ------------------------------------------------------------------------
    for letter in user_input:
      output += alphabet_to_number_dictionary[letter]

    # Printing the result (output is printed from 0 : -1 so that the last "-" does not come) -------------------------------------------------------------------------
    print("\n",output[:-1],"\n")

    # Asking the user to continue , change or stop converting -------------------------------------------------------------------------------------------------------
    start_over = input("Enter (A) or (N) to convert. Enter (H) for help and (E) to exit: ").lower()

    # Making it go to help menu
    if start_over == "h" :
      start_over = help(start_over)

    # Making it go to information menu
    if start_over == "i" :
      start_over = information(start_over)

    # Making sure that the answer is either "y" or "n" if not then we send the user input to the first function to get the correct answer ----------------------------
    if start_over != "a" and start_over != "n" and start_over != "h" and start_over != "e" and start_over != "i":
      start_over = start(start_over)

    # Main sending from numbers to alphabets menu -------------------------------------------------------------------------------------------
    if start_over == "n":
      start_over = number_to_alphabet(start_over)

    # Main sending from numbers to alphabets menu -------------------------------------------------------------------------------------------
    if start_over == "a":
      start_over = alphabet_to_number(start_over)

  # Tackling the key error (basically if a number is written instead of a letter) ------------------------------------------------------------------------------------
  except KeyError:
    print("\nOnly English Alphabets from a - z are allowed.\n")
    start_over = alphabet_to_number(start_over)

  # A just in case exception handler to maintain the flow of program -------------------------------------------------------------------------------------------------
  except Exception as e:
    print(e)
    start_over = alphabet_to_number(start_over)

# Actual Code of changing Numbers to Alphabets -----------------------------------------------------------------------------------------------------------------------
def number_to_alphabet(start_over):

  #  Using try and except to counter key error -----------------------------------------------------------------------------------------------------------------------
  try: 

    # The Numbers to Alphabet Dictionary ----------------------------------------------------------------------------------------------------------------------------
    number_to_alphabet_dictionary = {
    "26" : "z",
    "25" : "y",
    "24" : "x",
    "23" : "w",
    "22" : "v",
    "21" : "u",
    "20" : "t",
    "19" : "s",
    "18" : "r",
    "17" : "q",
    "16" : "p",
    "15" : "o",
    "14" : "n",
    "13" : "m",
    "12" : "l",
    "11" : "k",
    "10" :"j",
    "1" : "a",
    "2" : "b",
    "3" : "c",
    "4" : "d",
    "5" : "e",
    "6" : "f",
    "7" : "g",
    "8" : "h",
    "9" : "i",
    "*" : " "
    }
    
    # Asking for user input (The message to be converted in alphabet form) ------------------------------------------------------------------------------------------
    user_input = input("Please Enter a message: ")
    individual_number = user_input.split("-")
    
    output = ""

    # Using the dictionary to find the key value pair of the letter from the user input above ------------------------------------------------------------------------
    for number in individual_number:
      output += number_to_alphabet_dictionary[number]
    
    # Printing the result --------------------------------------------------------------------------------------------------------------------------------------------
    print("\n",output,"\n")

    # Asking the user to continue , change or stop converting -------------------------------------------------------------------------------------------------------
    start_over = input("Enter (A) or (N) to convert. Enter (H) for help and (E) to exit: ").lower()

    # Making it go to help menu
    if start_over == "h" :
      start_over = help(start_over)

    # Making it go to information menu
    if start_over == "i" :
      start_over = information(start_over)

    # Making sure that the answer is either "y" or "n" if not then we send the user input to the first function to get the correct answer ----------------------------
    if start_over != "a" and start_over != "n" and start_over != "h" and start_over != "e" and start_over != "i":
      start_over = start(start_over)

    # Main sending from numbers to alphabets menu -------------------------------------------------------------------------------------------
    if start_over == "n":
      start_over = number_to_alphabet(start_over)

    # Main sending from Alphabet to numbers menu -------------------------------------------------------------------------------------------
    if start_over == "a":
      start_over = alphabet_to_number(start_over)

      
  # Tackling the key error (basically if a alphabet is written instead of a number) ------------------------------------------------------------------------------------
  except KeyError:
    print("\nNumbers should be between 1 and 26 only\n")
    start_over = number_to_alphabet(start_over)
  
  # A just in case exception handler to maintain the flow of program -------------------------------------------------------------------------------------------------
  except Exception as e :
    print(e)
    start_over = number_to_alphabet(start_over)
  
# starting first time input ------------------------------------------------------------------------------------------------------------------------------------------
start_over = input("Type (A) to convert sentence from alphabet to numbers, Type (N) to convert numbers into alphabet, Type (H) for help and information and Type (E) if you want to exit the code: ").lower()

# Makes the question to be asked again if user input wrong letter ----------------------------------------------------------------------------------------------------
if start_over != "a" and start_over != "n" and start_over != "h" and start_over != "e" and start_over != "i":
  start_over = start(start_over)

# Main sending to help menu ---------------------------------------------------------------------------------------------------------
if start_over == "h":
  start_over = help(start_over)

# Main sending to information menu ---------------------------------------------------------------------------------------------------------------
if start_over == "i":
  start_over = information(start_over)

# Main sending from Alphabet to numbers menu -------------------------------------------------------------------------------------------
if start_over == "a":
  start_over = alphabet_to_number(start_over)

# Main sending from numbers to alphabets menu -------------------------------------------------------------------------------------------
if start_over == "n":
  start_over = number_to_alphabet(start_over)

# Stoping the program when asked by user to stop -------------------------------------------------------------------------------------------------------------------- 
while start_over == "e" :
  print(f"\nThanks for using the Program.\nThis Program is written by CodeSpec :) \nFor any questions feel free to email me at online.codespec@gmail.com\nCheers\n")
  break
