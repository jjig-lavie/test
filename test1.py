import sys 
f = open("../test.csv", "r") or sys.exit()
 

while True:
    line = f.readline()
    if not line :
        break
    #print(line,  end='')
    print(line)
    