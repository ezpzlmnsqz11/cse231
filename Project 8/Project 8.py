###########################################################
#  CSE 231 Project 8
#  Take the name and friends text file
#  Open the data files
#  Read each of the files of data
#  Display menu for choosing intended action
#  Depending on the chosen item,find the most popular person, 
#  most common friends, most second friends from the written functions
#  Print the data and reprompt the selections (1-5)
#  Check errors with cases and reprompt for errors
###########################################################
MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''
    
def open_file(s):
    ''' Prompts user to enter correct file name
        Value: String in place of the formatting 
        Return: file pointer of file
    '''
    while True: # looped for wrong file name entered
        filename=input("\nInput a {} file: ".format(s))
        try:
            fp= open(filename, 'r') 
            return fp
        except FileNotFoundError: #if file not found print error
            print("\nError in opening file.")

def read_names(fp):
    '''Reads the opened name file for each of the names
       Value: file pointer from the open file
       Return: List of strings of the names 
    '''
    L=[]
    for line in fp:
        line=line.strip() # get rid of junk
        L.append(line) # add each name of file to list
    return L

def read_friends(fp,names_lst):
    '''Reads the opened friends file for friends of each name
       Value: file pointer from open file and list of names for friend list
       Return: List of List of strings of names with corresponding friends
    '''
    L=[]
    L2=[]
    for line in fp:
        line=line.strip().strip(',').split(',') # get rid of end punctuation and make list 
        for i in line:
            i=int(i)
            L2.append(names_lst[i]) #append each name of index to list 2
        L.append(L2) #append the friends list into the main list then clear
        L2=[]
    return L

def create_friends_dict(names_lst,friends_lst):
    '''Build a dictionary of the names along with each of their friends
       Value: list of names and list of list of friends 
       Return: Dictionary of key name and value friends of name
    '''
    dictionary=dict(zip(names_lst,friends_lst))
    return dictionary
            
def find_common_friends(name1, name2, friends_dict):
    '''find common friends of 2 names in the dictionary
       Value: 2 names and the dictionary of friends to compare 
       Return: Set of strings of the common friends between the 2 names
    '''
    f1=set(friends_dict[name1]) 
    f2=set(friends_dict[name2])
    return f1.intersection(f2) # finds the common friends between the 2 names 
    
    
def find_max_friends(names_lst, friends_lst):
    '''Using the names and friends to find the person with the most friends
       Value: list of names and list of list of names and friends
       Return: List of strings of the person with the most friends as well as the number
       as an integer
    '''
    L=[]
    maxx= -5454554373585345
    for o, z in enumerate(names_lst):
        if len(friends_lst[o])>maxx: # compare max to length of friends at index
            maxx=len(friends_lst[o])
            L=[]
            L.append(z) #append the max
        elif maxx==len(friends_lst[o]):
            L.append(z)
    L.sort()
    return L,maxx 
    

def find_max_common_friends(friends_dict): # Helped by TA
    '''Use the dict to find which pairs of people have the most friends in common
       Value: dictionary of name and friends
       Return: list of tuples of pairs with the most common friends as well as the number(int)
    '''
    D={}
    maxx=-7995846
    for name1,listt in friends_dict.items():
        for name2,listt2 in friends_dict.items():
            if (name2,name1) not in D: # constraints check
                if name2==name1:
                    continue
                if name2 in listt or name1 in listt2:
                    continue
                x=find_common_friends(name1, name2, friends_dict) #call the function common friends
                D[(name1,name2)]=x
    for key, value in D.items(): #finding the maximum from the length and the list
        if len(value)>maxx:
            maxx= len(value)
    L=[]        
    for key, value in D.items():
        if maxx==len(value):
            L.append(key) #make the list from the key
    L.sort()
    return L, maxx

            
def find_second_friends(friends_dict): # Help by TA
    '''Use the friends dictioanry to find friends of friends
       Value: friends dictionary to similarly check the constraints
       Return: a dictionary of the second friends ,key/value (name/second friends)
     '''
    dic={}
    for key,value in friends_dict.items():
        S=set()
        for x in value:
            for i in friends_dict[x]:
                S.add(i)
                if i==key or i in value:
                    
                    S.remove(i)
        dic[key]=S
    return dic
        




def find_max_second_friends(seconds_dict):
    '''Find the max of second order friends from the second friends dictionary
       Value: second order friends dictionary to solve for max second friends
       Return: List of strings of the max second order friends as well as the number (int)
    '''
    maxx=-1283725
    for key, value in seconds_dict.items(): #same as max common friends but dictionary given
        if len(value)>maxx:
            maxx= len(value)
    L=[]        
    for key, value in seconds_dict.items():
        if maxx==len(value):
            L.append(key)
    L.sort()
    return L, maxx

        


def main():
    print("\nFriend Network\n")
    fp = open_file("names")
    names_lst = read_names(fp)
    fp = open_file("friends")
    friends_lst = read_friends(fp,names_lst)
    friends_dict = create_friends_dict(names_lst,friends_lst)

    print(MENU)
    choice = input("\nChoose an option: ")
    while choice not in "12345":
        print("Error in choice. Try again.")
        choice = input("Choose an option: ")
        
    while choice != '5':

        if choice == "1":
            max_friends, max_val = find_max_friends(names_lst, friends_lst)
            print("\nThe maximum number of friends:", max_val)
            print("People with most friends:")
            for name in max_friends:
                print(name)
                
        elif choice == "2":
            max_names, max_val = find_max_common_friends(friends_dict)
            print("\nThe maximum number of commmon friends:", max_val)
            print("Pairs of non-friends with the most friends in common:")
            for name in max_names:
                print(name)
                
        elif choice == "3":
            seconds_dict = find_second_friends(friends_dict)
            max_seconds, max_val = find_max_second_friends(seconds_dict)
            print("\nThe maximum number of second-order friends:", max_val)
            print("People with the most second_order friends:")
            for name in max_seconds:
                print(name)
                
        elif choice == "4":
            while True:
                inp=input("\nEnter a name: ")
                if inp in friends_dict: #if name is in the dictionary
                    print("\nFriends of {}:".format(inp)) 
                    for i in friends_dict[inp]:
                        print(i) #print the friends of the indicated(inputted) name
                    break # repeat the loop
                else:
                    print("\nThe name {} is not in the list.".format(inp)) #error if not on list
            

        else: 
            print("Shouldn't get here.")
            
        choice = input("\nChoose an option: ")
        while choice not in "12345":
            print("Error in choice. Try again.")
            choice = input("Choose an option: ")

if __name__ == "__main__":
    main()
