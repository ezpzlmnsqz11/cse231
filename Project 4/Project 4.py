###########################################################
#  CSE 231 Project 4 
#  Display Options
#  Prompt for a selection (F,E,P,S,M,X)
#  Detect to see if character is valid
#  Call the function 
#  Find the asked values for each input
#  Output function
#  Rerun the program(While True)
#  Display closing message if the program is broken
###########################################################
import math
EPSILON = 0.0000001 
MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.'''
def factorial(N): 
    ''' Function for printing the factorial of a given N integer
        if N is 1, reprint N, if its not 1 use the factorial
        formula
    '''
    tot = 1
    x = 1
    N = int(N) 
    if N== 0:
        return 1
    if N<0 :
        return None
    if N>0:
        while x <= N:
            tot = tot * x
            x = x + 1
    return tot


def e(): 
    ''' Function for printing the euler identity
        round to tenth at end ''' 
    sum=0
    N=1
    t=1/(factorial(N))
    while t >= EPSILON:
        if t < EPSILON:
            break
        sum=sum+t
        t=1/(factorial(N))
        N=N+1
    return round(sum,10)

        

def pi():
    ''' Function for printing the approximated value of pi 
        round to tenth at end''' 
    sum=0
    x=0
    t=((-1)**x)/((2*x)+1)
    while abs(t) >= EPSILON:
        sum = sum + t
        x=x+1
        t=((-1)**x)/((2*x)+1)
        
    return round(sum *4,10) 



def sinh(X): 
    ''' function for the hyperbolic sine of a given radian value
        if the given X is a float or integer 
        round to tenth at end''' 
    try:
        X = float(X)
    except ValueError:
        return None
    sum=0
    n=0
    t=(X**(2*n+1))/factorial(2*n+1)
    while abs(t)>= EPSILON:
        sum=sum+t
        n=n+1
        t=(X**(2*n+1))/factorial(2*n+1)
        
    return round(sum, 10)

def main():
    print(MENU)
    print()
    while True: #runs the program until there is a break
        
        print("\nChoose an option: ")
        x=input()
        if 'm'==x.lower():
            print('''Options below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.''')
            print()
            continue
        elif 'x'==x.lower(): # detects caps and lower
            print("Thank you for playing.")
            break
        elif 'f'==x.lower(): # detects caps and lower
            print("Factorial")
            N=int(input("Input non-negative integer N: "))
            if N<0:
                print("\nInvalid N.") #N is negative cant fact it
            else:
                print("\nCalculated:",factorial(N))
                print("Math:",math.factorial(N))
                print("Diff:",(factorial(N)-math.factorial(N))) #difference of facts
            continue
        elif 'e'==x.lower(): # detects caps and lower
            print("e")
            print("Calculated: {:.10f}".format(e()))
            print("Math: {:.10f}".format(math.e))
            print("Diff: {:.10f}".format((math.e-e()))) #difference of e's
            continue
        elif 'p'==x.lower(): # detects caps and lower
            print("pi")
            print("Calculated: {:.10f}".format(pi()))
            print("Math: {:.10f}".format(round(math.pi,10)))
            print("Diff: {:.10f}".format(round((math.pi-pi()),10))) #difference of pis
            continue
        elif 's'==x.lower(): # detects caps and lower
            print("sinh")
            X=float(input("X in radians: "))
            print("\nCalculated:",sinh(X))
            print("Math:",round(math.sinh(X),10))
            print("Diff: {:.10f}".format((math.sinh(X)-sinh(X)),10)) #difference of sinh
            continue
        else:
            print("Invalid option:", x.upper()) #changes to upper
            print(MENU)
            print()
            continue

            
       
    
        
        
 
       
           

          

       

    

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == '__main__': 
    main()


