# name          : Sean Whaley
# email         : smw100@pitt.edu
# date          : 9/14/2016
# class         : CS0008-f2016
# instructor    : Max Novelli (man8@pitt.edu)
#
# Description:
# Ch 2 exercise 7.

km = float(input('Enter total miles driven: ')) * 1.60934   # converting miles input to km
l = float(input('Enter the total amount of gallons of fuel consumed: ')) * 3.78541 # converting gal to liters
fuel_cons = 100 * l / km  # fuel consumption per 100 km
print 'Fuel consumption (liters/100km) is: ', fuel_cons  # displaying results