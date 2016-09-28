mesr = int(input('Please enter your units of measurement ( 1 for USC or 2 for Metric):  '))
if mesr == 1:
    mi = float(input('Distance in miles? '))
    if mi <= 0: print('Error distance traveled must be larger than 0!')
    gal = float(input('Gallons of gas used? '))
    if gal <= 0: print('Error gallons used must be larger than 0!')
    mpg = mi / gal
    km = mi * 1.60934
    lt = gal * 3.78541
    lkm = 100 * lt / km
elif mesr == 2:
    km = float(input('Distance in kilometers? '))
    if km <= 0: print('Error distance traveled must be larger than 0!')
    lt = float(input( 'Liters of fuel used? '))
    if lt <= 0: print('Error liters used must be larger than 0!')
    lkm = 100 * lt / km
    gal = lt * .264172
    mi = km *.621371
    mpg = mi / gal
elif mesr != 1 or 2:
    print('Error! Entry not recognized as unit of measure!')
if lkm > 20:
 fc = 'Extremely poor'
elif 15 < lkm and lkm <= 20:
 fc = 'Poor'
elif 10 < lkm and lkm <= 15:
 fc = 'Average'
elif 8 < lkm and lkm <= 10:
 fc = 'Good'
elif 0 < lkm <= 8:
 fc = 'Excellent'
else:
 fc = 'Error'
print (mi)
print (gal)
print (mpg)
print (km)
print (lt)
print (lkm)
print (fc)

#print ('\t USC\t Metric')
#print('Distance\t'mi 'miles\t' km 'Km') format(mi, 10.3f) format(km, 10.3f)
#print('Gas\t' gal 'gallons\t' lt 'Liters') format(gal, 10.3f) format (lt, 10.3f)
#print('Consumption\t' mpg 'mpg\t' lkm '1/100Km') format(mpg, 10.3f) format(lkm, 10.3f)
#print('\n Consumption Rating:' fc)