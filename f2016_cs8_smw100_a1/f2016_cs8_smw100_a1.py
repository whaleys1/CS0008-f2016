measr = str(input('Please enter your units of measurement (usc or met):  '))
if measr == 'usc':
    mi = float(input('Distance in miles? '))
    if mi <= 0: print('Error distance traveled must be larger than 0!')
    gal = float(input('Gallons of gas used? '))
    if gal <= 0: print('Error gallons used must be larger than 0!')
    km = mi * 1.60934
    lt = gal * 3.78541
    print (mi, gal, km, lt)