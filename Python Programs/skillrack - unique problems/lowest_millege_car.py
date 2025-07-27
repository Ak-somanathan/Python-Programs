s=list(map(str, input().split()))
d=dict()
st=""
for i in s:
    st=i
    for j in st:
        if j=="@":
            name=st[0:st.index(j)]
            d[name]=st[st.index(j)+1::]
else:
    minimum=min(d, key=lambda x: float(d[x]))
    print(minimum)
