import sys 
f = open("../test.csv", "r") or sys.exit()
import os
os.system("color 9")

while True:
    line = f.readline()
    if not line :
        break
    #print(line,  end='')
    print(line)
    