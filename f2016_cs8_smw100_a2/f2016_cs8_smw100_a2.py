def main():
    tcount = 0  # intializing total line accumulator
    tmiles = 0  # intializing total miles accumulator
    file = input("Please enter a file name or type q for quit: ")
    pcount = 0  # intializing partial line accumulator
    pmiles = 0  # intializing partial miles accumulator
    while file and file != 'quit' != 'q':  # creating a user controlled loop for input
        fh = open(file, 'r')
        file = input("Please enter a file name or type q for quit: ")


        def processfile(fh):  # defining processfile function
         for line in fh:
            pcount += 1  # incrementing the line count
            line = line.rstrip("/n")  # stripping the new line character
            temp = line.split(",")  # seperating the name from miles
            miles = float(temp[1])  # casting miles as a float with an index to the correct data
            pmiles += miles  # adding the partial miles to the accumulator

        processfile(fh)  # calling processfile
    tcount += pcount  # adding the partials to the total
    tmiles += pmiles


    print (tcount, tmiles)
main()