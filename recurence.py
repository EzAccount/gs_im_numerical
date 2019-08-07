import time as time
import numpy as np


e = 0
H = 0
e_new = 0
H_new = 0
h = []
start = time.time()
with open("fields.txt") as f:
    line = None
    for next_line in f:
        if line is not None:
            h = float(line)
            e_new = e - 0.5 * np.fabs(h + H + 1 ) - 0.5 * np.fabs(h + H - 1 )
            H_new = 0.5 * np.fabs(h + H + 1 ) - 0.5 * np.fabs(h + H - 1 )
            e = e_new
            H = H_new
        line = next_line
done = time.time()
print( max (np.fabs(e_new-H_new-float(line)),np.fabs(e_new+H_new+float(line))))
with open("time.txt", "a") as f:
    f.write("Recurrence algorithm:\n")
    f.write("Total: "+str(done-start)+str('\n'))