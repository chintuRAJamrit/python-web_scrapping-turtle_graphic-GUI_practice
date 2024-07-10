fname = "f1.txt"
nl=0
nw=0
nc=0
with open(fname, "r") as f:
    for l in f:
        w = l.split()
        nl+=1
        nw+=len(w)
        nc+=len(l)
        print(w)

print(nl, nw ,nc)
    
