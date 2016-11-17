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
            d[key] = d[key].append (value)
        else:
            d[key] = [value]
    inner_file.close()
    return [d, count]
run_g = {}
out_file = open('output.txt', 'w')
master = 'f2016_cs8_a3.data.txt'
file = open (master, 'r')
for line in file:
    line = line.rstrip('\n')
    d, count = opfile(line, run_g)
    run_g.update(d)

max_name = ''
max_dist = 0
min_name = ''
min_dist = 0
tot_dist = 0
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
    out_file.write(key, num_run, ind_dist)
    tot_dist += ind_dist

