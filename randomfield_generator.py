import random
import numpy as np


def low_field_generator(a):
    with open("fields.txt", "w+") as f:
        for i in np.arange(a):
            f.write(str(random.uniform(-0.5,0.5))+'\n')


def high_field_generator(a):
    with open("fields.txt", "w+") as f:
        for i in np.arange(a):
            f.write(str(random.uniform(10,20))+'\n')

def any_valued_generator(a):
    with open("fields.txt", "w+") as f:
        for i in np.arange(a):
            f.write(str(random.uniform(-4,4))+'\n')


#low_field_generator(1E3)
#high_field_generator(1E3) #positive only
any_valued_generator(1E7)