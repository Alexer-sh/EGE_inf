s=open('24_21717.txt').readline()

m=10000
for l in range(len(s)):
    for r in range(l+m,l,-1):
        c=s[l:r+1]
        if c.count('RSQ')<130:
            break
        elif c.count('RSQ')==130 and c[-1]!="Q":
            m=min(m,len(c))
    if l%1000==0:
        print(l,len(s),m)