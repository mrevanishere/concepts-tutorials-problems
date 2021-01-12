
def find_judge(N, trust):
#   n is int of which index in array trust is the town judge
    #   if judge on [0] then -1
    #   how to identify judge
    #   a number on the right not on the left
    left = set()
    right = set()
    for pair in trust:
        if pair[0] not in left:
            left.add(pair[0])
        if pair[1] not in right:
            right.add(pair[1])
    # if k not in left and in right: k = judge
    print()
    print(left)
    print(right)
    z = right.difference(left)
    if len(z) == 0:
        return -1
    for pair in trust:
        # check if a number does not trust the suspected judge
    return z


trust = [[1,3],[2,3]]
trust1 = [[1,3],[2,3],[3,1]]
trust2 = [[1,2],[2,3]]
trust3 = [[1,3],[1,4],[2,3],[2,4],[4,3]]
out = find_judge(3, trust);
print(out)
out = find_judge(3, trust1);
print(out)
out = find_judge(3, trust2);
print(out)
out = find_judge(4, trust3);
print(out)


