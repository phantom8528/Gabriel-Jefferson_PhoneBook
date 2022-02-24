#Name: Gabriel Jefferson
#Assignment: Module 2, Day 5, PhoneBook.py

#from operator import is_


terminate_prog = False
instruction_menu = '''\nGabriel's Electronic Phone Book\n
==================================\n
Please Type The Number Corresponding with the following options\n
1. Look up and entry\n
2. Set an entry\n
3. Delete an entry\n
4. List all entries\n
5. Quit\n
==================================='''
#________________FUNCTIONS_______________________________
def verify_option_input(input): #<-- created a function that verifies that the option inputted is the option available
    #pass
    is_between = 1 <= input <= 5 #<-- This returns a boolean
    if is_between == False:
        print("\nSorry,\n\nThis is not an option") #<-- Catches any "int" that isn't an option
    

def add_an_entry():
    global entName
    entName = input("\nEnter Name: ") #<-- Just added some spacing
    entNumb = input("\nEnter Number: ")#<-- Just added some spacing
    phone_book_entries[entName] = entNumb
    print ("\nEntry Added") #<-- Just added some spacing
    
    # SELF HOMEWORK -->iterate through dictionary to confirm, and return a confirmation message
def list_all_entries():
    print(phone_book_entries)

def contact_search():
    lookup = input("Who Are You Looking For: ")
    print("Here You Are", phone_book_entries[lookup], "\n")

def delete_contact():
    global removeInput
    removeInput = input("Who Are We Removing: ")
    phone_book_entries.pop(removeInput)
    print("Contact Successfully Removed.\n")
#_________________WHILE AND IF STATEMENTS__________________________
phone_book_entries = {} #<---Dictionary for phone book
while not(terminate_prog):

    print (instruction_menu)
    #global user_input #<-- made user_input a global variable so that it could be used by functions
    user_input = int(input("What would you like to do\n\nChoose an option (1-5): "))
    verify_option_input(user_input)

    if user_input == 1: # <-- Looking up and entry
        #pass
        #print("test of option 1")
        contact_search()

    elif user_input == 2: #<-- Inserting an entry
        #pass
        add_an_entry()
    elif user_input == 3: #<-- Deleting an entry
        #pass
        delete_contact()
    elif user_input == 4: #<-- Listing all the entries
        #pass
        list_all_entries()
    elif user_input == 5: #<-- Terminating the program
        #pass
        #terminate_prog = True
        exit() #<-- More efficient than using boolean approach
