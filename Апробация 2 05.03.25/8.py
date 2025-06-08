from itertools import product
a=product("012345678",repeat=5)
c=0
for t in a:
    st=''.join(t)
    if st[0]!='0' and st.count('0')==1 and "01" not in st and "03" not in st and "05" not in st and "07" not in st and "09" not in st and "10" not in st and "30" not in st and "50" not in st and "70" not in st and "90" not in st:
        print(st)
        c+=1
print(c)