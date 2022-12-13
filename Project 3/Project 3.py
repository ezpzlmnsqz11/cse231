###########################################################
#  CSE 231 Project 3 by Ozan Uyulur
#  Display Project Banner
#  Prompt for a Triangle
#  Detect to see if character is valid
#  Display the lengths of the triangle
#  Use algorithms to find the angles, area, perimeter, and type
#  Print the summary
#  Ask if the user wants to test another triangle
#  Display closing message
###########################################################
import math

BANNER = '''

╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃
╰╯┃┃┣┻┳┳━━┳━╮╭━━┫┃╭━━╮
╱╱┃┃┃╭╋┫╭╮┃╭╮┫╭╮┃┃┃┃━┫
╱╱┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰┫┃━┫
╱╱╰╯╰╯╰┻╯╰┻╯╰┻━╮┣━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
'''
print(BANNER)
print()
triangle=0
pi=math.pi
tri=input("Do you wish to process a triangle (Y or N)?  " )
while tri == 'Y' or tri == 'y': # while loop for  recalling another test

    a= float(input('\nEnter length of side AB: '))
    b = float(input('\nEnter length of side BC: '))
    c= float(input('\nEnter length of side CA: '))
    if a+b==c or b+c==a or c+a==b: #sum of 2 angles equals third its degenerate
        print("\n\n  Degenerate Triangle" )
        again= input("\nDo you wish to process another triangle? (Y or N) ") # 
        if again == 'y' or again== 'Y': #recall for antoher triangle
            continue
        else:
            break
    elif a+b<c or b+c<a or c+a<b: #sum of 2 angles less than third its not a tri
        print("\n\n  Not a Triangle" )
        again= input("\nDo you wish to process another triangle? (Y or N) ")
        if again == 'y' or again== 'Y': #recall for another triangle
            continue
        else:
            break
    elif a+b>c and b+c>a and c+a>b: #sum of 2 angles greater, its valid
        print("\n\n  Valid Triangle" )
        print("\n  Triangle sides:")
        print("    Length of side AB: "+str(a))
        print("    Length of side BC: "+str(b))
        print("    Length of side CA: "+str(c))
        #use law of cosines to find the angle (180/pi) for degree measure
        degA=round(math.acos(((c**2)+(a**2)-(b**2))/(2*a*c))*(180/math.pi), 1)        
        degB=round(math.acos(((a**2)+(b**2)-(c**2))/(2*b*a))*(180/math.pi), 1)    
        degC=round(math.acos(((b**2)+(c**2)-(a**2))/(2*b*c))*(180/math.pi), 1)
        print("\n  Degree measure of interior angles:")
        print("    Angle A: "+str(degA))
        print("    Angle B: "+str(degB))
        print("    Angle C: "+str(degC))
        #use law of cosines to find the angle
        radA=round(math.acos(((c**2)+(a**2)-(b**2))/(2*a*c)),1)
        radB=round(math.acos(((a**2)+(b**2)-(c**2))/(2*b*a)),1)
        radC=round(math.acos(((b**2)+(c**2)-(a**2))/(2*b*c)),1)
        print("\n  Radian measure of interior angles:")
        print("    Angle A: "+str(radA))
        print("    Angle B: "+str(radB))
        print("    Angle C: "+str(radC))
        perimeter= a+b+c #add all sides for perimeter
        s= perimeter/2 #use semiperimeter to find area
        area= (math.sqrt((s*(s-a)*(s-b)*(s-c)))) #easier area formula
        print("\n  Perimeter and Area of triangle:")
        print("    Perimeter of triangle: "+str(perimeter))
        print("    Area of triangle: " + str(round(area,1)))
        print("\n  Types of triangle:")
        if a==b and a==c: # law of syllogism
            print("    Isosceles Triangle")
            print("    Equilateral Triangle")
        elif a==b or a==c or b==c: #or is used to only test isoceles
            print("    Isosceles Triangle")
        else:
            print("    Scalene Triangle" )        
        if degA==90.0 or degB==90.0 or degC==90.0: # 90deg= right triangle
            print("    Right Triangle")
        elif (degA>90.0) or (degB>90.0) or (degC>90.0): #>90 is scalene
            print("    Oblique Triangle")
            print("    Obtuse Triangle")
        else:
            print("    Oblique Triangle")
        triangle= triangle+1
        again = input("\nDo you wish to process another triangle? (Y or N) ")
        if again == 'y' or again == 'Y': #recall triangle
            continue
        else:
            break
print("\nNumber of valid triangles: "+str(round(triangle,1))) #final statement
        
    