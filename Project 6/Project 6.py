###########################################################
#  CSE 231 Project 6 
#  Open a file of data 
#  Read the file of data
#  User input 1-4 selections to display desired information
#  display the specific data created by the functions
#  keep reprompting from the menu until 4 is selected
#  then quit program
#  close the file
###########################################################
import csv
from operator import itemgetter #itemgetter for sorting

NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "

ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"


def open_file():
    '''Prompts for a file name from 2 choices
       Value: the data being processes as (str)
       Return: returns the file pointer to be read
    '''
    while True: # looped for wrong file name entered
        data=input("Enter file name: ")
        try:
            fp= open(data, 'r') #open data read
            return fp
        except FileNotFoundError: #if file not found print error
            print("\nError opening file. Please try again.")
    

def read_file(fp):
    '''Reads file from open function
       Value: the file pointer being read
       Return: List of tuples'''
    reader=csv.reader(fp)
    h=next(reader,None)
    char=[]
    #print(h)
    for line in reader: #loop to read whole data file
        #print(line)
        name= line[0]
        rarity= int(line[1])
        element= line[2]
        weapon= line[3]
        region= line[4]
        if region == '':
            region= None
        tup=(name, element, weapon, rarity, region) #formed tuple
        char.append(tup)
    return char #return list of tuples

    


def get_characters_by_criterion (list_of_tuples, criteria, value):
    '''Get characters into a list by criterion
       Value: List of tuples, integer inputs, string inputs
       Return: Organized list of tuples
    '''
    L=[]
    criteria=int(criteria)
    for value in list_of_tuples:
        if value=='':
            return L
        if value==None:
            continue
        if criteria==1:
            if value[1].lower()== value.lower():
                value=value[1]
                return L.append(value)
        if criteria==2:
            if value[2].lower()== value.lower():
                value=value[2]
                return L.append(value)
        if criteria==3:
            if value == int :
                return L.append(value)
            else:
                return None
        if criteria==4:
            if value[4].lower()== value.lower():
                value=value[4]
                return L.append(value)
        #help
        
        
    

def get_characters_by_criteria(master_list, element, weapon, rarity):
    '''Get characters into a list for each criteria
       Value: Master list each criteria(str),rarity(int)
       Return: Organized list of tuples'''
       #help
   

def get_region_list(master_list):
    '''Extracts every region in the list
       Value: list of strings from master list
       Return: Sorted list of strings of regions
    '''
    L=[i[4] for i in master_list] #list of all 4th indexes of master
    new=[]
    for i in L:
        if i not in new:
            new.append(i) #adding regions IF not already added
    L=new
    for i in new:
        if i==None: #remove index with No regions
            new.remove(i)
    new.sort() #sort at the end
    return new


def sort_characters (list_of_tuples):
    '''Sorts a list of tuples
       Value: given a list of tuples
       Return: the sorted list of tuples
    '''
    L=[] # sort the list of tuples
         # sort the sorted list at index 3 reverse order
    L = sorted((sorted(list_of_tuples)), key=itemgetter(3),reverse=True)
    return L
   
def display_characters (list_of_tuples):
    '''Displays the characters of the tuple list
       Value: A list of tuples
       Return: The printed character attributes
    '''
    print("\n{:20s}{:10s}{:10s}{:<10s}{:25s}".format("Character",
    "Element","Weapon","Rarity","Region"))
    for tup in list_of_tuples:
        if len(list_of_tuples)==0: #if tuple is empty nothing to print
            print("Nothing to print.")
        elif tup[4]==None: #if 4th index is none print N/A for that spot
            print("{:20s}{:10s}{:10s}{:<10d}{:25s}".format(tup[0],tup[1]
            ,tup[2],tup[3],'N/A'))
        else:
            print("{:20s}{:10s}{:10s}{:<10d}{:25s}".format(tup[0],tup[1]
            ,tup[2],tup[3],tup[4]))


def get_option():
    '''Displays menu for 1-4 to be chosen
       Value: integer value being processed
       Return: inputted integer or and error
    '''
    valid=int(input(MENU)) #user input from menu
    if int(1)<=valid<=int(4):
        return valid #return the inputted int
    else:
        print(INVALID_INPUT) #if 1-4 not selected, invalid

 
  
def main():
    fp=open_file() #open the file
    master_list= read_file(fp) #read the file
    ch=get_option() #display the options
    while True:
        if ch==int(1): 
            print( "\nRegions:")
            print(", ".join(get_region_list(master_list))) #list into strings using join
            ch=get_option()
            continue
        if ch==int(2):
            print()

            continue
        if ch==int(3):
            print()

            continue
        if ch==int(4):
            exit() #exit program for 4
    
    
    
   

    
   


    
    

# DO NOT CHANGE THESE TWO LINES
#These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__":
    main()
    
