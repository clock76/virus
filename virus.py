import os, sys
var = sys.argv[1]

for i in range(int(var)):
    os.mkdir(str(i+1))