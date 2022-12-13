###########################################################
#  CSE 231 Project 9
#  Take the Prices and Securities text file
#  Open the data files
#  Read the securities file
#  Add the prices into the empty list of the read securities file
#  Display menu for choosing intended action
#  Execute the intended action from the MENU below 
#  Print the data and reprompt the selections (1-6)
#  Check errors with security codes and prices and reprompt for errors
###########################################################
import csv

MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
WELCOME = "Welcome to the New York Stock Exchange.\n"
    
def open_file():
    '''Open 2 files at one time, prices and securities of companies
       Value: No parameters
       Return: Prices file pointer and Secutiries file pointer
    '''
    price=input("\nEnter the price's filename: ")
    while True: # looped for wrong file name entered
        try:
            fp= open(price, 'r') #read type
            security=input("\nEnter the security's filename: ")
            try:
                sp=open(security, 'r') #read type
                return fp, sp
            except FileNotFoundError:#if file not found print error and reprompt
                print("\nFile not found. Please try again.")
                security=input("\nEnter the security's filename: ")

        except FileNotFoundError: #if file not found print error and reprompt
            print("\nFile not found. Please try again.")
            price=input("\nEnter the price's filename: ")


def read_file(securities_fp):
    '''takes and reads the security file pointer that has the names and codes
       Value: Security file pointer opened in the open file function
       Return: A set of all the company names, and a dictionary with key as code
    '''
    D={}
    S=set()
    reader=csv.reader(securities_fp)
    next(reader,None)
    for line in reader:
        name=line[1]
        S.add(name) # making the set of all company names
        code=line[0]
        sec=line[3]
        subsec=line[4]
        address=line[5]
        date=line[6]
        L=[name,sec,subsec,address,date,[]] # make the list with the empty list for add prices
        D[code]=L # code as the key in the dictionary
    return S,D
        
def add_prices (master_dictionary, prices_file_pointer):
    '''Adds the prices file into the empty list of dictionary from the read security file
       Value: The the_dict dictionary from the previous function and the prices file
       Return: Nothing, but adds the prices file into the existing securities the_dict dictionary
    '''
    reader=csv.reader(prices_file_pointer)
    next(reader,None)
    for line in reader:
        if line[1] in master_dictionary:
            date=line[0]
            openinfo=float(line[2])
            closeinfo=float(line[3])
            lowinfo=float(line[4])
            highinfo=float(line[5])
            L=[date,openinfo,closeinfo,lowinfo,highinfo] # made the list of prices
            master_dictionary[line[1]][5].append(L) # append the price list into the empty initial list


        
def get_max_price_of_company (master_dictionary, company_symbol): #TA HELP
    '''Takes the the_dict dictionary and code to return highest company price and the date
       Value: the_dict dictionary and company code
       return: a tuple of first the max price of the company and then the date
    '''
    L=[]
    maxx=-65793285
    if company_symbol not in master_dictionary:
        return None, None
    price = master_dictionary[company_symbol][5]
    if price == []:
        return None, None
    else:
        for i in price:
            date=i[0]
            high=i[4]
            tup=(high,date)
            L.append(tup) # create a list of tuples of the companies high price and the date
        return max(L) # find the max and return the tuple with the price and date
        

            

def find_max_company_price (master_dictionary):
    '''Takes the dictionary and similarly finds the max company price of the key(code)
       Value: the mater dictionary of companies
       Return: The tuple of the company code first followed by the maxp price of that company code
    '''
    L=[]
    for code in master_dictionary:
        company=get_max_price_of_company (master_dictionary, code)
        x=company[0]
        if x == None:
            continue
        t=(x,code) # make a tuple of the high and the code
        L.append(t)
        value,code=max(L) # mind the max of the value not code
    return (code,value) # change it back to normal to return in right order
        
        
def get_avg_price_of_company (master_dictionary, company_symbol): 
    '''get the average price of the companty from the main dict and the code
       Value: main dictionary and the key of that dictionary being the company code(symbol)
       Return: A float of the average price of the company code entered.
    '''
    L=[]
    if company_symbol not in master_dictionary:
        return 0.0
    price = master_dictionary[company_symbol][5]
    if price == []:
        return 0.0
    else:
        for i in price:
            high=i[4]
            L.append(high) # make a list of all the high prices of the company
        return round((sum(L)/len(L)),2) # return the average of the max prices
    
def display_list (lst):  # "{:^35s}" #TA HELP
    ''' Organizes and prints the company names 3 to a line
        Value: a list of all the company names
        Return: Nothing, but prints names 3 to a line going down the columns
    '''
    count=0
    for i in lst:
        print("{:^35s}".format(i),end='') #print each company with the formatting
        count+=1
        if count==3: #when the third(3) company is printed for the row, next line
            print()
            count=0
    print("\n")



    
def main():
    print(WELCOME)
    fp,sp=open_file()
    names,the_dict=read_file(sp) #dictionary and set 
    add_prices(the_dict, fp) #add prices to the dictionary
    print(MENU)
    option=int(input("\nOption: "))
    while True:
        if option==1:
            print("\n{:^105s}".format("Companies in the New York Stock Market from 2010 to 2016"))
            display_list (sorted(names)) #print all the names sorted using display list func
            print(MENU)
            option=int(input("\nOption: ")) # reprompt for new selection after every option executes
            continue
        elif option==2:
            print("\ncompanies' symbols:")
            display_list (sorted(the_dict)) # all the companies symbols sorted and using display list func
            print(MENU)
            option=int(input("\nOption: "))
            continue
        elif option==3:
            maxcomp=input("\nEnter company symbol for max price: ")
            x,y=get_max_price_of_company (the_dict, maxcomp) # float and date returned
            if maxcomp in the_dict: #does the code exist?
                if x: #is there a price?
                    print("\nThe maximum stock price was ${:.2f} on the date {:s}/\n".format(x,y)) # print with correct formatting
                else: 
                    print("\nThere were no prices.")
            else:
                print("\nError: not a company symbol. Please try again.")
                continue
            print(MENU)
            option=int(input("\nOption: "))
            continue
        elif option==4:
            x=find_max_company_price (the_dict)
            print("\nThe company with the highest stock price is {:s} with a value of ${:.2f}\n".format(*x)) #(x[0],x[1])
            print(MENU)
            option=int(input("\nOption: "))
            continue
        elif option==5:
            avgcomp=input("\nEnter company symbol for average price: ")
            x=get_avg_price_of_company (the_dict, avgcomp) #only a float is returned being the avg price
            if avgcomp in the_dict: # does the code exist in the dictionary?
                if x: #is there a price?
                    print("\nThe average stock price was ${:.2f}.\n".format(x)) #print avg stock price with correct formatting
                else: #if there isn't ...
                    print("\nThere were no prices.")
            else:
                print("\nError: not a company symbol. Please try again.")
                continue
            print(MENU)
            option=int(input("\nOption: "))
            continue
        elif option==6: # if option 6 is selected, break and quit out of the program
            break
        


    

       
if __name__ == "__main__": 
    main() 
