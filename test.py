file = open("staff.weekend.txt",'r')
time_ = {}
for line in file :
    print (line)
    (key, val) = line.split(':')
    time_[key] = val
    print (time_)
