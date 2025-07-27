s=input()
if "_" in s:
    rev,bal=s.split("_")
    print(rev[::-1]+"_"+bal)
else:
    print(s[::-1])
