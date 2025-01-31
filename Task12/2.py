s = '7'* 40+'4'*50+ '9'*40
while "49" in s or "97" in s or "47" in s:
    if "47" in s:
        s=s.replace("47","74",1)
    elif "97" in s:
        s = s.replace("97","79",1)
    else:
        s = s.replace("49", "94",1)
    print(s)
print(s)
print(s[25],s[71],s[105])