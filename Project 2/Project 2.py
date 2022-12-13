###########################################################
#  CSE 231 Project 2 by Ozan Uyulur
#  Display welcome messages for car rental service
#  Prompt for a capital character
#  Detect to see if character is valid
#  Use algorithms for finding the amount due
#  Solve the over 100000 issue
#  Print the summary
#  Display closing message
###########################################################
BANNER = print("\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" )
 
PROMPT = cont=input('''\nWould you like to continue (A/B)? \n''')
while cont=='A': #either A or B, if not B display closing message
    code= input("\nCustomer code (BD, D, W): \n")
    while code!= "BD" and code!= "D" and code!= 'W':
        print("\n\t*** Invalid customer code. Try again. ***")
        code= input("\nCustomer code (BD, D, W): \n")
    day= int(input("\nNumber of days: \n"))
    ostart= int(input("Odometer reading at the start: \n"))
    oend= int(input("Odometer reading at the end:   \n"))
    totalmiles = float((oend-ostart)/10)
    charge = float(0)
    if (oend<ostart): # code for if the end is less than start
        totalmiles = (oend+10-(ostart%10))/10
    if code=='BD': # algorithm for Budget
        base = 40*day 
        mileage = 0.25*totalmiles
        charge = base + mileage
    if code=='D': # algorithm for Daily
        base= 60*day
        averagemiles = float(totalmiles/day)
        if (averagemiles<=100):
            mileage=0
        if (averagemiles>100):
            mileage=(averagemiles-100)*0.25*day
        charge = base + mileage
    if code=='W': # Algorithm for Weekly
        if(day%7==0):
            weeks=int(day/7)
        else:
            weeks=int(day/7)+1
        base=weeks*190
        averagemiles=float(totalmiles/weeks)
        if averagemiles<=900:
            mileage=0
        elif averagemiles<1500:
            mileage=100*weeks
        else:
            mileage= (200*weeks)+((averagemiles-1500)*0.25*weeks)
        charge= base+mileage

    print("\nCustomer summary:") #printing the summary data
    print('\tclassification code: '+code)
    print('\trental period (days): '+str(day))
    print('\todometer reading at start: '+str(ostart))
    print('\todometer reading at end:   '+str(oend))
    print("\tnumber of miles driven:  "+str(totalmiles))
    print("\tamount due: $ "+str(float(charge)))
    cont =input('''\nWould you like to continue (A/B)? \n''')
print("Thank you for your loyalty.") #print this if B is entered by user

