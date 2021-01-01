import random
f = open("rchunk.data", "w")
f.write("-1, 2, -1,\n")
# flatten a 3d array to 2d
'''
y:
z x x x x ... 
z 
z
z
z
.
.
.
y2:

'''
for y in range(1,17):
    for z in range(1,17):
        for x in range(1,17):
            f.write("%s," % random.randint(0, 1))
        f.write("\n")
    # f.write("\n")
