n=int(input())
l=[]
an_l=[]
max_score=0
for i in range(0,n):
    ele=input()
    l.append(ele)

for i in l:
    st=i
    for j in i:
        if j==",":
            an_l.append(st[0:st.index(j)])
            an_l.append(st[st.index(j)+1::])
            
for i in range(1,(n*2)+1,2):
    if int(an_l[i])>max_score:
        max_score=int(an_l[i])
        name=an_l[i-1]
print(name)
