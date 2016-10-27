while file and file != 'quit' or != 'q'
    fh = open (file, 'r')
def processf(fh):
pcount = 0
pmiles = 0
file = open (file_name, 'r')
for line in file:
    pcount += 1
    line = line.rstrip("/n")
    temp = line.split(",")
    miles = float(temp [1])
    pmiles += miles
