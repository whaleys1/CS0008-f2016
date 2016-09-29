mesr = int(input('Please enter your units of measurement ( 1 for USC or 2 for Metric):  '))
if mesr == 1:  #if USC calculating vars based on mi & gal
    mi = float(input('Distance in miles? ')) #formatting input as float
    if mi <= 0:
        print('Error distance traveled must be larger than 0!') #printing error if improper values
        mi = 1
    gal = float(input('Gallons of gas used? '))
    if gal <= 0:
        print('Error gallons used must be larger than 0!')
        gal = 1
    mpg = mi / gal  #calculating mpg
    km = mi * 1.60934 #converting mi to km
    lt = gal * 3.78541 # gals to liters
    lkm = 100 * lt / km
elif mesr == 2: #if Metric calculating vars based on km & liters
    km = float(input('Distance in kilometers? '))
    if km <= 0:
        print('Error distance traveled must be larger than 0!')
        km = 1
    lt = float(input( 'Liters of fuel used? '))
    if lt <= 0:
        print('Error liters used must be larger than 0!')
        lt = 1
    lkm = 100 * lt / km
    gal = lt * .264172 #liters to gals
    mi = km *.621371 #km to miles
    mpg = mi / gal
elif mesr != 1 or 2: #creating error pathway
    print('Error! Entry not recognized as unit of measure!')
    mi  = 0  # setting values for vars in event of entry error
    gal = 0
    mpg = 0
    km = 0
    lt = 0
    lkm = 0
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

print '\t\t\t\t\tUSC' #spacing and formating
print 'Distance\t', format(mi, '10.3f'),'miles' #formatting to 10 spaces and 3 dec
print 'Gas\t\t\t', format(gal, '10.3f'),'gallons'
print 'Consupmtion\t', format(mpg, '10.3f'),'mpg'
print '\t\t\t\t   Metric'
print 'Distance\t', format(km, '10.3f'),'Km'
print 'Gas\t\t\t', format(lt, '10.3f'),'liters'
print 'Consumption\t', format(lkm, '10.3f'), 'l/100Km'
print '\nGas Consumption Rating:', fc
