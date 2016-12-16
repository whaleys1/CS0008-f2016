# name       : Sean Whaley
# email      : smw100@pitt.edu
# date       : 2016/12/15
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Final Project

class Runner:
    # Runner class created

    name = "unknown"
    # total distance run by the runner
    distance = 0
    # total number of runs by the runner
    runs = 0

    # methods
    # initializer methods
    def __init__(self, name, distance=0):
        # set name
        self.name = name
        # set distance if non zero
        if distance > 0:
            # set distance
            self.distance = distance
            # set number of runs accordingly
            self.runs = 1
            # end if

    # end def __init__

    # addDistance method
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1
            # end if

    # end def addDistance

    # addDistances method
    def addDistances(self, distances):
        # loops over list
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1
                # end if
                # end for

    # end def addDistances

    # return the name of the participant
    def getName(self):
        return self.name

    # end def getName

    # return the total distance run computed
    def getDistance(self):
        return self.distance

    # end def getDistance

    # return the number of runs
    def getRuns(self):
        return self.runs

    # end def getRuns

    # stringify the object
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')
        # end def __init__

def opfile(filename, d):
    inner_file = open(filename, 'r')
    count = 0
    inner_file.readline()
    for in_line in inner_file:
        count += 1
        in_line = in_line.rstrip('\n').split(',')
        key = str(in_line[0])
        value = float(in_line[1])
        if key in d:
                # MN: append changes the list in place
                # MN: you need to check the syntax of the command, space before ( is not needed
                # d[key] = d[key].append (value)
            d[key] = d[key].append(value)
    else:
        d[key] = [value]
        inner_file.close()
        return [d, count]

run_g = {}
    # MN: I would open the output file when and where I really need it, down below
    # out_file = open('output.txt', 'w')
    # MN: why not asking the user for master list file name?
master = '/Users/seanwhaley/Documents/CS0008/CS0008-f2016/f2016_cs8_smw100_fp/f2016_cs8_fp.data(1)'
file = open(master, 'r')
for line in file:
        line = line.rstrip('\n')
        d, count = opfile(line, run_g)
        run_g.update(d)
    # MN: we need to close the master file
file.close()

max_name = ''
max_dist = 0
min_name = ''
min_dist = 0
tot_dist = 0
    # MN: open output file
    # MN: respect file nameing convention as requested in specifications/assignment
    # out_file = open('output.txt', 'w')
out_file = open('f2016_cs8_smw100_fp.output.txt', 'w')
for key in run_g:
    ldist = run_g[key]
    ind_dist = 0
    num_run = len(ldist)
    for value in ldist:
        ind_dist += value
        if value > max_dist:
            max_dist = value
            max_name = key
        elif value < min_dist:
            min_dist = value
            min_name = key
        # MN: write requires a string in inut
        # out_file.write(key, num_run, ind_dist)
    out_file.write(key + ',' + str(num_run) + ',' + str(ind_dist) + '\n')
    tot_dist += ind_dist
    # MN: we need to close output file
out_file.close()

#
# set format strings
INTEGER = '5d'
FLOAT = '12.5f'
STRING = '20s'

#
# provide requested output
print("")
print(" Number of Input files read   : " + format(numberFiles,INTEGER))
print(" Total number of lines read   : " + format(count,INTEGER))
print("")
print(" Total distance run           : " + format(tot_dist,FLOAT))
print("")
print(" Max distance run             : " + format(max_dist['distance'],FLOAT))
print("   by Runner                  : " + format(max_dist['name'],STRING))
print("")
print(" Min distance run             : " + format(min_dist['distance'],FLOAT))
print("   by Runner                  : " + format(min_dist['name'],STRING))
print("")
print(" Total number of Runners      : " + format(tot_num_part,INTEGER))
print(" Number of runners")
print("  with multiple records       : " + format(tot_num_part_with_mult,INTEGER))
print("")

