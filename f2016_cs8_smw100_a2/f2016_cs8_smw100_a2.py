#
# MN: header with user, instructor and course info is missing
#
# Notes:
# MN: printKV function is missing
#


# MN: what does this function do?
def main():
    tcount = 0  # intializing total line accumulator
    tmiles = 0  # intializing total miles accumulator
    file = input("Please enter a file name or type q for quit: ")
    # MN: why do you open the file for reading here? Check the comments below in the while loop.
    fh = open(file, 'r')

    # MN: what does this function do?
    # MN: why do you define a function inside another function?
    def processfile(fh):  # defining processfile function
      for line in fh:  #for loop through each line in fh
       # 
       # MN: if you initialize accumulatos inside the loop where you use them
       #     at every iteration they are rest to 0, and you loose the count
       pcount = 0   #intializing partial accumulator
       pmiles = 0   #intializing partial accumulator
       pcount += 1  # incrementing the line count
       line = line.rstrip("/n")  # stripping the new line character
       temp = line.split(",")  # seperating the name from miles
       miles = float(temp[1])  # casting miles as a float with an index to the correct data
       pmiles += miles  # adding the partial miles to the accumulator
       # 
       # MN: when you are suppose to provide feedback on the partial accumulators?
       #     the following 2 print statements will be executed at every iteration 
       #     of the loop that reads the lines from the file
       #     they should be outside this loop
       print ("File to be read: ", file)   #last ditch effort to capture some output
       print ("Partial Total # of lines: ", format(pcount, '10s'))
       print ("Partial Distance run    : ", format(pmiles, '10.3f'))


    # MN: please do not use inline comments
    while file and file != "q" and not 'quit':  # creating a user controlled loop for input
       # MN: you should open the file for reading here. What happens the second iteration?
       # 
       # MN: why do you call processfile 2 times? 
       #     One correclty and the second one without input or output arguments?
       pcount, pmiles =processfile(fh)  # calling processfile
       processfile(fh)
       #
       # MN: why do you ask for the next file to be processed, before closing the current one?
       file = input("Please enter a file name or type q for quit: ")
       tcount += pcount  # adding the partials to the total
       tmiles += pmiles
       #
       # MN: closing the file should go before the input statement above
       fh.close()

    # MN: why did you commented the printKV function?
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
