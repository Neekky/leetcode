def numJewelsInStones(J, S):
    m = J
    e = S
    n = 0
    for i in range(len(m)):
        a = e.count(m[i])
        n = n + a
    return n

print(numJewelsInStones('sa', 'ssawefsas'))