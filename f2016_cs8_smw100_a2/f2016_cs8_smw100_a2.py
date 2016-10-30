def main():
    tcount = 0  # intializing total line accumulator
    tmiles = 0  # intializing total miles accumulator
    file = input("Please enter a file name or type q for quit: ")
    fh = open(file, 'r')

    def processfile(fh):  # defining processfile function
      for line in fh:  #for loop through each line in fh
       pcount = 0   #intializing partial accumulator
       pmiles = 0   #intializing partial accumulator
       pcount += 1  # incrementing the line count
       line = line.rstrip("/n")  # stripping the new line character
       temp = line.split(",")  # seperating the name from miles
       miles = float(temp[1])  # casting miles as a float with an index to the correct data
       pmiles += miles  # adding the partial miles to the accumulator
       print ("File to be read: ", file)   #last ditch effort to capture some output
       print ("Partial Total # of lines: ", format(pcount, '10s')
       print ("Partial Distance run    : ", format(pmiles, '10.3f'))


    while file and file != "q" and not 'quit':  # creating a user controlled loop for input
       pcount, pmiles =processfile(fh)  # calling processfile
       processfile(fh)
       file = input("Please enter a file name or type q for quit: ")
       tcount += pcount  # adding the partials to the total
       tmiles += pmiles
       fh.close()
    # def printKV(key, value, klen = 0):
    # kl =  max(len(key), klen)
    # if isinstance (value, str):
    # fs = '20s'
    # elif isinstance (value, float):
    # fs = '10.3f'
    # elif isinstance (value, int):
    # fs = '10s'
    # else:
    # print ('Error! I cannot print this')

main()
