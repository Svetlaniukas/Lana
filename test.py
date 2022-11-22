file = open("master.txt",'r')
time_table = {}
for line in file :
    print (line)
    (key, val) = line.split ( ':' )
    time_table[key] = val
    print (time_table)
