#
# MN: required header with user, instructor and course info is missing
#
# Notes:
# MN: a little bit more comments
# MN: print info to screen is missing
# 


# MN: description of this function
def opfile (filename, d):
    inner_file = open(filename, 'r')
    count = 0
    inner_file.readline()
    for in_line in inner_file:
        count+= 1
        in_line = in_line.rstrip('\n'). split(',')
        key = str(in_line [0])
        value = float (in_line [1])
        if key in d:
            # MN: append changes the list in place
            # MN: you need to check the syntax of the command, space before ( is not needed
            #d[key] = d[key].append (value)
            d[key].append(value)
        else:
            d[key] = [value]
    inner_file.close()
    return [d, count]

run_g = {}
# MN: I would open the output file when and where I really need it, down below
#out_file = open('output.txt', 'w')
# MN: why not asking the user for master list file name?
master = 'f2016_cs8_a3.data.txt'
file = open (master, 'r')
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
#out_file = open('output.txt', 'w')
out_file = open('f2016_cs8_smw100_a3.output.txt', 'w')
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
    #out_file.write(key, num_run, ind_dist)
    out_file.write(key + ',' +  str(num_run) + ',' + str(ind_dist) + '\n')
    tot_dist += ind_dist
# MN: we need to close output file
out_file.close()

