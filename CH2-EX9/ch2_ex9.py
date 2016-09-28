# name          : Sean Whaley
# email         : smw100@pitt.edu
# date          : 9/14/2016
# class         : CS0008-f2016
# instructor    : Max Novelli (man8@pitt.edu)
#
# Description:
# Ch 2 exercise 9. Program to convert F degrees to Celsius with 2 decimal places.

f = float(input('Enter the temprature in Farenheit (degrees): '))
c = 5 * (f -32) / 9  #converting deg F to deg C
print 'The temperature in Celsius (degrees) is: ', format(c, '.2f')
# displaying the output with 2 decimal places