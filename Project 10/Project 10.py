###########################################################
#  CSE 231 Project 10
#  Initialize the stock tableau foundation and waste for the solitaire game
#  Write functions for each possible move in the game
#  Test to see if the move is valid or invalid 
#  Use the parse option for all error checking
#  Display menu for choosing intended action
#  print the display and follow with an option
#  Execute the inputted move
#  Check if game is won, if not, play the move and keep going
#  When game is won, print message and display and quit
###########################################################
from cards import Card, Deck

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
def initialize():
    '''initialize the stock,waste,tableau, and foundation for the solitaire game
       Value: None
       Return: Initialized values as lists to work with
    '''
    stock=Deck()
    stock.shuffle()
    waste=[]
    foundation=[[],[],[],[]]
    tableau=[[],[],[],[],[],[],[]]
    for i in range(7):
        for x in range(i,7):
            tableau[x].append(stock.deal()) #append cards to the correct places
    for col in tableau:
        for c in col:
            c.flip_card() #flip everycard
    for top_card in tableau:
        top_card[-1].flip_card() #flip desired card
    wcard=stock.deal()
    waste.append(wcard)
    return (tableau, stock, foundation, waste)
    
def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    

def stock_to_waste( stock, waste ):
    '''Move cards from the stock pile to the waste pile
       Value: stock and waste piles
       Return: A boolean(True or False) if the move was success or not
    '''
    if stock.is_empty(): # stock isempty, you cant add cards to the waste
        return False
    try:
        var=stock.deal()
        new_waste=waste.append(var)
        return True
    except:
        return False


def waste_to_foundation( waste, foundation, f_num ): #TA Help
    '''Move a card from the waste pile from 1 of the 4 foundations if possible
       Value: waste card, foundation , and the columns of the foundation
       Return: A boolean(True or False) if the move was a success or not
    '''
    wcard=waste[-1]
    if len(foundation[f_num])==0:
        if wcard.rank()==1: # if len is 0 and rank ace, append to foundation
            foundation[f_num].append(wcard)
            waste.pop() #cut card after its appended
            return True
    else:
        found=foundation[f_num][-1]
        if wcard.rank()==found.rank()+1 and wcard.suit()==found.suit(): # if card same suit and 1 rank higher append
            foundation[f_num].append(wcard)
            waste.pop() #cut card after its appended
            return True
    return False


            
def waste_to_tableau( waste, tableau, t_num ): #TA Help
    '''Move the waste card to 1 of the 7 columns of the tableau
       Value: waste, tableau, and column of the tableau
       Return: A boolean(True or False) if the move was a success or not
    '''
    if len(waste)==0: # if waste empty, you cant append
        return False
    wcard=waste[-1]
    wrank=wcard.rank()
    if len(tableau[t_num])==0:
        if wrank==13:
            tableau[t_num].append(waste.pop()) # append the king if theres an empty tableau column
            return True
        return False
    tcard=tableau[t_num][-1]
    trank=tcard.rank()
    if wcard.suit()== 2 or wcard.suit()==3:
        wsuit='red'
    if tcard.suit()== 2 or tcard.suit()==3:
        tsuit='red'
    if wcard.suit()== 1 or wcard.suit()==4:
        wsuit='black'
    if tcard.suit()== 1 or tcard.suit()==4:
        tsuit='black'
   
    if wsuit != tsuit: 
        if wrank+1==trank:
            tableau[t_num].append(waste.pop()) #append card to tableau if its 1 rank lower and opposite color
            return True
    return False


def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    '''Move a card from 1 of the tableaus to a foundation column
       Value: tableau, foundation, column of the tableau, column of the foundation
       Return: A boolean(False or True) if the move failed or it was a success
    '''
    tcard=tableau[t_num][-1]
    trank=tcard.rank()
    if len(foundation[f_num])==0:
        if trank==1:
            foundation[f_num].append(tableau[t_num].pop()) # append if the rank is an ace
            if len(tableau[t_num])!= 0:
                if tableau[t_num][-1].is_face_up()==False: # flip the card 
                    tableau[t_num][-1].flip_card()
            return True
        return False
    fcard=foundation[f_num][-1]
    frank=fcard.rank()
    
    if tcard.suit()== 2 or tcard.suit()==3:
        tsuit='red'
    if tcard.suit()== 1 or tcard.suit()==4:
        tsuit='black'
    if fcard.suit()== 2 or fcard.suit()==3:
        fsuit='red'
    if fcard.suit()== 1 or fcard.suit()==4:
        fsuit='black'
    
    if tcard.suit() == fcard.suit():
        if trank-1==frank:
            foundation[f_num].append(tableau[t_num].pop()) # append if the rank is 1 higher and the suit is the same
            if len(tableau[t_num])!= 0:
                if tableau[t_num][-1].is_face_up()==False:
                    tableau[t_num][-1].flip_card()

            
            return True
        
    return False





def tableau_to_tableau( tableau, t_num1, t_num2 ):
    '''Move a card from one column of the tableau to a different column
       Value: the tableau, a column where the card is pulled, the destination column of the pulled card
       Return: A boolean(True or False) if the move was success or not
    '''
    tcard=tableau[t_num1][-1]
    trank=tcard.rank()
    if len(tableau[t_num2])==0:
        if trank==13:
            tableau[t_num2].append(tableau[t_num1].pop()) # append a king if there is an empty column in the tableau
            if len(tableau[t_num1])!=0:
                if tableau[t_num1][-1].is_face_up()==False:
                    tableau[t_num1][-1].flip_card()
            return True
        return False
    tresult=tableau[t_num2][-1]
    tresultrank=tresult.rank()
    if tcard.suit()== 2 or tcard.suit()==3:
        tsuit='red'
    if tcard.suit()== 1 or tcard.suit()==4:
        tsuit='black'
    if tresult.suit()== 2 or tresult.suit()==3:
        tsuitresult='red'
    if tresult.suit()== 1 or tresult.suit()==4:
        tsuitresult='black'

    if tsuit != tsuitresult:
        if trank+1==tresultrank:
            tableau[t_num2].append(tableau[t_num1].pop()) #append if the suits are different and the rank is 1 lower
            if len(tableau[t_num1])!=0 :
                if tableau[t_num1][-1].is_face_up()==False:
                    tableau[t_num1][-1].flip_card()
            return True
    return False


    
def check_win (stock, waste, foundation, tableau):
    '''Checks the lengths of each of the data structures and determines if the game is won
       Value: stock, waste, foundation, and tableau data structures
       Return: True if the game is in a winning state, false if it is not.
    '''
    if len(stock)==0 and len(waste)==0 and not any(tableau): # if all data structures are empty, you win (TRUE)
        return True
    else:
        return False

def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above


def main():   
    tableau, stock, foundation, waste = initialize() #initialize the game
    print(MENU) # print the menu
    while True:
        display(tableau, stock, foundation, waste) #display the game board
        inp=input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
        val=parse_option(inp) #parse option for errors, check the return of lists, either of len 1 2 or 3
        if val==None:
            continue
        if len(val)==3:
            if val[0]=='TT':
                x=tableau_to_tableau( tableau, val[1]-1, val[2]-1)
                if x==False:# function false= invalid move
                    print("\nInvalid move!\n")
                    
            if val[0]=='TF':
                x=tableau_to_foundation( tableau,foundation, val[1]-1, val[2]-1 )
                if x==False:# function false= invalid move
                    print("\nInvalid move!\n")
                else:
                    if check_win (stock, waste, foundation, tableau) == True: #if this functon is true, you won
                        print("You won!")
                        break
        elif len(val)==2:
            if val[0]=='WT':
                x=waste_to_tableau( waste, tableau, val[1]-1 )
                if x ==False: # function false= invalid move
                    print("\nInvalid move!\n")
            if val[0]=='WF':
                x=waste_to_foundation( waste, foundation, val[1]-1 )
                if x==False: # function false= invalid move
                    print("\nInvalid move!\n")
                else:
                    if check_win (stock, waste, foundation, tableau) == True: #if this functon is true, you won
                        print("You won!")
                        break

        elif len(val)==1:
            if val[0]=='SW':
                x = stock_to_waste( stock, waste )
                if x==False:
                    print("\nInvalid move!\n") # if move is invalid, print message
                
        
        
            elif val[0]=='R':
                tableau, stock, foundation, waste = initialize()
                print(MENU) #restart game and print menu

            
            
            
            elif val[0]=='H': 
                print(MENU) #reprint the menu

            
            
            
            elif val[0]=='Q': #quit the program
                break
        
    




















if __name__ == '__main__':
     main()
