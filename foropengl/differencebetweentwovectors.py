load_list = [2, 3, 4, 5]
indices = []
chunks = [1, 2, 4, 5]

for i in range(len(load_list)):
    indices.append(i)
print(indices)

i = 0
while (i < len(chunks)):
    print(i)
    print(load_list)
    print(indices)
    print(chunks)
    chunk_in_list = False
    j = 0
    while (j < len(load_list)):
        print("j: ", j)
        if (chunks[i] == load_list[j]):
            # remove from indices
            chunk_in_list = True
            break
        j += 1;
    if not chunk_in_list:
        print("remove")
        chunks.pop(i)
        i -= 1
    else:
        indices.remove(j)
        print("Load")
        print("Draw")
    print()
    i += 1

print("Res: ")
print(load_list)
print(indices)
print(chunks)
