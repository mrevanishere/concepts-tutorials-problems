c = 0

f = open("vertices2.txt", "w")
f.write(
    "#ifndef BLOCKSANDSTICKS_CHUNKVERTICES_H\n#define BLOCKSANDSTICKS_CHUNKVERTICES_H\nconst float vertices[] = {\n")
for i in range(0, 17):
    for j in range(0, 17):
        for k in range(0, 17):
            # back?
            # print("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f," % (i - 1, j - 1, k - 1, 0, 0))
            # print("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f," % (i, j - 1, k - 1, 1, 0))
            # print("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f," % (i, j, k - 1, 1, 1))
            # print("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f," % (i, j, k - 1, 1, 1))
            # print("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f," % (i - 1, j, k - 1, 0, 1))
            # print("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f," % (i - 1, j - 1, k - 1, 0, 0))
            # print()

            # back
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j - 1, k - 1, 0, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j - 1, k - 1, 1, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j, k - 1, 1, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j, k - 1, 1, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j, k - 1, 0, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j - 1, k - 1, 0, 0))
            f.write("\n")

            # front?
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j - 1, k, 0, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j - 1, k, 1, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j, k, 1, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j, k, 1, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j, k, 0, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j - 1, k, 0, 0))
            f.write("\n")

            # left?
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j, k, 1, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j, k - 1, 1, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j - 1, k - 1, 0, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j - 1, k - 1, 0, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j - 1, k, 0, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j, k, 1, 0))
            f.write("\n")

            # right
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j, k, 1, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j, k - 1, 1, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j - 1, k - 1, 0, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j - 1, k - 1, 0, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j - 1, k, 0, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j, k, 1, 0))
            f.write("\n")

            # bottom
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j - 1, k - 1, 0, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j - 1, k - 1, 1, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j - 1, k, 1, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j - 1, k, 1, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j - 1, k, 0, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j - 1, k - 1, 0, 1))
            f.write("\n")

            # top
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j, k - 1, 0, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j, k - 1, 1, 1))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j, k, 1, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i, j, k, 1, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j, k, 0, 0))
            f.write("%s.0f, %s.0f, %s.0f, %s.0f, %s.0f,\n" % (i - 1, j, k - 1, 0, 1))
            f.write("\n")

            c += 36


f.write("};\n#endif //BLOCKSANDSTICKS_CHUNKVERTICES_H")
print(c*5)
# 176868 * 5
# 884340
