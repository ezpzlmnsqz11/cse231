###########################################################
#  CSE 231 Project 1 
#
#  Algorithm
#  User inputs floating point value
#  Write code to reprint converted values using formulas 
#  Calculate time to walk to Portage
#  Display all conversions and time
########################################################### 
rods = input("Input rods: \n") #user inputs a value for rods
rods_float = float(rods) #convert this input into a float
print("You input", rods_float, "rods.")
print()
RodInMeters = 5.0292 #declare given values
WalkingSpeed = 3.1
Meters =  RodInMeters * rods_float #use rods and meters to find each conversion
Furlongs = rods_float / 40
Miles = RodInMeters * rods_float / 1609.34
Feet = Meters / 0.3048
Time = Miles / (WalkingSpeed / 60)
print("Conversions") #now print each of the values for their assigned conversion
print("Meters:", round(Meters, 3))
print("Feet:", round(Feet, 3))
print("Miles:", round(Miles, 3))
print("Furlongs:", round(Furlongs, 3))
print("Minutes to walk", rods_float, "rods:", round(Time, 3))
