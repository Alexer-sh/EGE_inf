print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if not((w<=(not(z<=x)))or y ):
                    print(x,y,z,w)