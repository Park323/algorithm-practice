T = int(input())

denoms = [300, 60, 10]
cnts = []

for denom in denoms:
    ret = T // denom
    T %= denom
    cnts.append(str(ret))
    
if T > 0:
    print(-1)
else:
    print(" ".join(cnts))