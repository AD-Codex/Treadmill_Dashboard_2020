# To run program with custom parameters - you can give the parameters in any order
# python E18_G_XXX.py --motor 4 --radius "0.09 m" --height "170 cm" --time "600 s" --weight "100 lb"

import argparse
import math
import time


# Value calculating functions.
def calSpeed(RPM ,radius): # Define a function to return the speed of the tredmill.
    speed = 2 * math.pi * radius * RPM / 60
    return speed

def calDistance(speed ,time): # Define a function to return the distance move by person.
    Distance  = speed * time
    return Distance

def calCaloriesBurnt(speed ,time ,weight ,height): # Define a function to return the calories burned on person.
    Calories_Burnt  = (( 0.035 * weight ) + (( speed**2 / height ) * 0.029 * weight )) * time / 60
    return Calories_Burnt

def calNumOfSteps(height ,Distance): # Define a function to return number of steps keep by person.
    Num_Of_Steps = 2 * (( 5280 / ( height * 0.413 * 39.37/ 12 ) ) * ( Distance / 1609.344 ))
    return Num_Of_Steps


# Unit Converting functions.
def con_Length(string): # Define a function to convert the Length parameters into SI unit.
    nlist = string.split(' ')# Take the value and unit of input separately.
    if nlist[1] == 'm' :# Check which unit is.
        value = float(nlist[0])# Convert and give value in SI unit.
    elif nlist[1] == 'cm' :
        value = float(nlist[0])/ 100
    elif nlist[1] == 'in' :
        value = float(nlist[0]) / 39.37
    else:
        value = 0
    return value

def con_Weight(string): # Define a function to convert the Mass parameters into SI unit.
    nlist = string.split(' ')
    if nlist[1] == 'kg' :
        value = float(nlist[0])
    elif nlist[1] == 'lb' :
        value = float(nlist[0]) / 2.205
    else:
        value = 0 
    return value


# Don't change the the code below this point
if __name__=="__main__":

    args=argparse.ArgumentParser()
    args.add_argument("--motor", type=int, dest="motor_rate", help="EXAMPLE: 3", default=30)
    args.add_argument("--radius", type=str, dest="radius", help="EXAMPLE: 8 cm", default="8 cm")
    args.add_argument("--weight", type=str, dest="weight", help="EXAMPLE: 50 kg", default="50 kg")
    args.add_argument("--height", type=str, dest="height", help="EXAMPLE: 63 in", default="63 in")
    
    args=args.parse_args()
# Don't change the the code above this point

# Assing parameters for variables and callin funtions that convert to SI uints.
args.motor_rate = float(args.motor_rate)
args.radius     = con_Length(args.radius)
args.weight     = con_Weight(args.weight)
args.height     = con_Length(args.height)

t1 = time.localtime()
t1 = time.mktime(t1)
Distance,Calories_Burnt,Num_Of_Steps = 0,0,0
while True:
    t2 = time.localtime()
    t2 = time.mktime(t2)
    if t2-t1 == 1:
        args.time = t2 - t1
        t1 = time.localtime()
        t1 = time.mktime(t1)
        # Calling functions define for calculate values.
        Speed          = calSpeed(args.motor_rate ,args.radius)
        Distance       = Distance + calDistance(Speed ,args.time)
        Calories_Burnt = Calories_Burnt + calCaloriesBurnt(Speed ,args.time,args.weight ,args.height)
        Num_Of_Steps   = Num_Of_Steps + calNumOfSteps(args.height ,calDistance(Speed ,args.time))
        # Display outputs.
        print(int(Speed),'m/s')
        print(int(Distance),'m')
        print(int(Calories_Burnt),'cal')
        print(int(Num_Of_Steps))








    
