###########################################################
#  CSE 231 Project 11
#  initialize the Volume class with magnitude and units with constarints
#  Check the validity of the magnitude and the units
#  be able to convert from metric to customary and vice versa
#  equal method to compare volumes
#  add and subtract functions to add Volumes
###########################################################
UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self, mag=0,uni='ml'):   # this line is incomplete: parameters needed
        '''Initializes the magnitude and units , takes in self, magnitude of 0, and unit of ml,
           there is no return but rather checking for valid volumes and setting None for invalids
        '''
        #first, check if uni in UNITS
            #if not, self.__mag = None and self.__uni = None
        #second, check if  magnitude is valid, if not self.__mag = 0 self.__uni = None
        if uni not in UNITS: #checks for invalid units
            self.__mag=None
            self.__uni=None
        elif type(mag)==int or type(mag)==float and mag > 0 : #if the volume is valid
            self.__mag = mag
            self.__uni = uni
            
        else:
            self.__mag=0
            self.__uni=None
        
    def __str__(self):    # this line is incomplete: parameters needed
        '''Returns volumes that are valid and formatted 
           and rejects invalid volumes from the value self
        '''
        if self.is_valid(): #checks if units is not None
            return '{:.3f} {:s}'.format(self.__mag,self.__uni)
        else:
            return 'Not a Volume' #returns negative statement other wise
        
    def __repr__(self) :   # this line is incomplete: parameters needed
        '''Returns volumes that are valid and formatted 
           and rejects invalid volumes from the value self
        '''
        if self.is_valid(): #checks if units is not None
            return '{:.6f} {:s}'.format(self.__mag,self.__uni)
        else:
            return 'Not a Volume'#returns negative statement other wise
        
    def is_valid(self):     # this line is incomplete: parameters needed
        '''if the value of the units equals one, return False for any is_valid calls
           otherwise, the boolean value is True
        '''
        if self.__uni != None: #if units equal None, invalid, elsewise, its valid
            return True
        else:
            return False
        
    def get_units(self):     # this line is incomplete: parameters needed
        '''returns units
        '''
        return self.__uni 
        
    
    def get_magnitude(self):  # this line is incomplete: parameters needed
        '''returns magnitude
        '''
        return self.__mag
    
    def metric(self):      # this line is incomplete: parameters needed
        '''checks validity and converts from ounce to ml if units is oz,
           otherwise, return original volume
        '''
        #converting an oz object in ml
        #if self has a unit value and the unit is oz 
        #if it is in oz
        #returning a volume object with converted magnitude and ml
        #making an object Volume(self.__mag*MLperOZ, 'ml')
        if self.is_valid():
            if self.__uni=='ml': #if its already in ml, dont convert
                return Volume(self.__mag,self.__uni)
            if self.__uni=='oz': #convert elsewise
                return Volume(self.__mag*MLperOZ,'ml')
        else:
            return Volume(-1,'this is not valid')
        
        
    def customary(self):    # this line is incomplete: parameters needed
        '''checks validity and converts from ml to oz if units is ml,
           otherwise, return original volume
        '''
        if self.is_valid():
            if self.__uni=='oz':#if its already in oz, dont convert
                return Volume(self.__mag,self.__uni)
            if self.__uni=='ml':#convert elsewise
                return Volume(self.__mag/MLperOZ,'oz')
        
        else:
            return Volume(-1,'this is not valid')
        
    def __eq__(self, other):  # this line is incomplete: parameters needed
        '''Compares the magnitude of two volumes. If the volumes are from 
           different places, it will be compared. Takes in other as the V2
        '''
        equ=abs(self.get_magnitude()-other.get_magnitude()) #difference of the volumes
        return (equ<DELTA) # checks for 0 returns True/False if its 0
        if type(other)!=type(Volume):
            return False
        
        
       
    def add(self, otherr):  # this line is incomplete: parameters needed
        '''Adds volumes together and adds constants to a volume
           if the following constraints satisfy. Takes in otherr as V2
        '''
        if self.is_valid() == False:
            return Volume(-1,'this is not valid')
        elif type(otherr)== int or type(otherr)==float: #if valid, return added volume
            return Volume(self.__mag+otherr,self.__uni)
        elif type(otherr)!=type(Volume):
            return Volume(-1,'this is not valid')


    
    def sub(self,othe ): # this line is incomplete: parameters needed
        '''Subtracts volumes and subtracts constants from a volume
           if the following constraints satisfy. Takes in othe as V2
        '''
        if self.is_valid() == False:
            return Volume(-1,'this is not valid')
        elif type(othe)== int or type(othe)==float:
            return Volume(self.__mag-othe,self.__uni)#if valid, return subtracted volume
        elif type(othe)!=type(Volume):
            return Volume(-1,'this is not valid')
