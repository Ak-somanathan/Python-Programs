L=list(map(str,input().split()))
tot_d=0
tot_t=0
for i in L:
    d,t=i.split("@")
    tot_d+=int(d)
    tot_t+=int(t)
print("{:2f} kmph".format(tot_d/tot_t))
