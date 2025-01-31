s ='0' +'2'* 6 + '4'*10 +'6'*12
while "02" in s or "04" in s or "06" in s:
    if "02" in s:
        s=s.replace("02","620",1)
    elif "04" in s:
        s = s.replace("04","4206",1)
    else:
        s = s.replace("06", "402",1)
    print(s)
print(s)
print(s.count('2'),s.count('4'),s.count('6'))