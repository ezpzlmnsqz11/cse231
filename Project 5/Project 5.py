###########################################################
#  CSE 231 Project 5 
#  Read a file of data
#  apply formulas from functions
#  apply correct conversions with the given constants
#  use results to attempt to predict the possibility of life-supporting conditions
#  close the file
#  Display the cummulative data
###########################################################
import math # math.pi being used

#Constants
PI = math.pi   
EARTH_MASS =  5.972E+24    # kg
EARTH_RADIUS = 6.371E+6    # meters
SOLAR_RADIUS = 6.975E+8    # radius of star in meters
AU = 1.496E+11             # distance earth to sun in meters
PARSEC_LY = 3.262

def open_file():
    ''' Repeatedly prompt for a file name
        value: data file being processed(str)
        return: returns the file
    '''
    data=input("Input data to open: ") #user inputs data
    data+='.csv'
    try:
        open(data)
    except FileNotFoundError:
        print('\nError: file not found. Please try again.')
        again=input('Input a filename: ')




def make_float(s):
    ''' Try to convert a string to a float
        value: string into float
        return: if valid return the float, else -1
    '''
    try:
        s=float(s) #if string can be float return the string
        return s
    except ValueError: # if it cant be converted return -1
        return -1
    
  
def get_density(mass, radius):
    ''' Getting the density with mass and radius
        value: float value of mass and radius
        return: density float value from 2 values
    '''
    mass=mass*EARTH_MASS #use mass constant to convert to metric
    radius=radius*EARTH_RADIUS # use radius constant to convert to metric
    if mass<0: #cant have negative mass
        return -1
    elif radius<0: #cant have a negative radius
        return -1
    else:
        density= mass/((4/3)*(math.pi)*(radius**3)) #formula for density
    return density

def temp_in_range(axis, star_temp, star_radius, albedo, low_bound, upp_bound):
    ''' Getting planet temperature in range using planet temp formula
        value: float of each value
        return: boolean either T/F if temp in range 
    '''
    star_radius=star_radius*SOLAR_RADIUS # use radius constant to convert to metric
    axis=axis*AU #use Au to convert to metric
    if axis <0 or star_temp<0 or star_radius<0 or albedo<0 or low_bound<0 or upp_bound<0: 
        return False #if any value is less than 0, return false
    planet_temp= star_temp*((star_radius/(2*axis))**(0.5))*((1-albedo)**(0.25))
    if low_bound<=planet_temp<=upp_bound: # if formula above between the bounds return True
        return True
    else:
        return False # if not ,return false
      

    

def get_dist_range():
    ''' finding the farthest distance from Earth
        value: nothing(user input)
        return: distance in float
    '''
    distance=input("\nEnter maximum distance from Earth (light years): ")
    while True:
        try:
            distance = float(distance) #convert to a float
            if distance < 0: # cant have a negative distance
                print("\nError: Distance needs to be greater than 0.")
                distance=input("\nEnter maximum distance from Earth (light years): ")
                continue
            else:
                return distance
        except ValueError: # if distance not a float, theres a value error
            print("\nError: Distance needs to be a float.")
            distance=input("\nEnter maximum distance from Earth (light years): ") 
            continue #recall for a valid distance^
    
    

def main():
         
    print('''Welcome to program that finds nearby exoplanets '''\
          '''in circumstellar habitable zone.''')
          

if __name__ == "__main__":
    main()