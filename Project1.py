import math
def calSpeed(RPM ,radius):
    speed = 2 * math.pi * int(radius) * RPM / 60
    return speed

def calDistance(speed ,time):
    Distance  = speed * time
    return Distance

def calCaloriesBurnt(speed ,time ,weight ,height):
    Calories_Burnt  = (( 0.035 * weight ) + (( speed**2 / height ) * 0.029 * weight )) * time / 60
    return Calories_Burnt

def calNumOfSteps(height ,Distance):
    Num_Of_Steps = round(( 5280 / ( height * 0.413 / 12 ) ) * ( Distance / 1609.344 ))
    return Num_Of_Steps

# print('================= Treadmill Calculator =================')

# RPM    = float(input('Enter the rate at with the motor is rotating (RPM)               : '))
# radius = float(input('Enter the radius of the motor shaft in Meter                     : '))
# weight = float(input('Enter Weight of the person in Kilogram                           : '))
# height = float(input('Enter Height of the person in Inches                             : '))
# time   = float(input('Enter the Time duration the person was walking/running in Second : '))

# print()
# print('***************** Results *******************')
# speed = calSpeed(RPM ,radius)
# Distance = calDistance(speed ,time)
# Calories_Burnt = calCaloriesBurnt(speed ,time ,weight ,height)
# Num_Of_Steps = calNumOfSteps(height ,Distance)
# print('speed = ', speed)
# print('Distance = ',Distance)
# print('Calories Burnt = ',Calories_Burnt)
# print('Number Of Steps = ',Num_Of_Steps)


