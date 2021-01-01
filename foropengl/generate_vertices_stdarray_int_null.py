c = 0

f = open("vertices3.txt", "w")
f.write(
    "#ifndef BLOCKSANDSTICKS_CHUNKVERTICES_H\n#define BLOCKSANDSTICKS_CHUNKVERTICES_H\n"
    "#include <vector>\n\nconst std::vector<int> defchunk = {\n")
for i in range(1, 18):
    for j in range(1, 18):
        for k in range(1, 18):

            # back
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j - 1, k - 1, 0, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j - 1, k - 1, 1, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j, k - 1, 1, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j, k - 1, 1, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j, k - 1, 0, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j - 1, k - 1, 0, 0))
            f.write("\n")

            # front?
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j - 1, k, 0, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j - 1, k, 1, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j, k, 1, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j, k, 1, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j, k, 0, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j - 1, k, 0, 0))
            f.write("\n")

            # left?
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j, k, 1, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j, k - 1, 1, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j - 1, k - 1, 0, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j - 1, k - 1, 0, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j - 1, k, 0, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j, k, 1, 0))
            f.write("\n")

            # right
            f.write("%s, %s, %s, %s, %s,\n" % (i, j, k, 1, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j, k - 1, 1, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j - 1, k - 1, 0, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j - 1, k - 1, 0, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j - 1, k, 0, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j, k, 1, 0))
            f.write("\n")

            # bottom
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j - 1, k - 1, 0, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j - 1, k - 1, 1, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j - 1, k, 1, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j - 1, k, 1, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j - 1, k, 0, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j - 1, k - 1, 0, 1))
            f.write("\n")

            # top
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j, k - 1, 0, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j, k - 1, 1, 1))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j, k, 1, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i, j, k, 1, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j, k, 0, 0))
            f.write("%s, %s, %s, %s, %s,\n" % (i - 1, j, k - 1, 0, 1))
            f.write("\n")

            c += 36


f.write("};\n#endif //BLOCKSANDSTICKS_CHUNKVERTICES_H")
print(c*5)
# 176868 * 5
# 884340
