s=input()
h,m=s.split(":")
if int(h)>=12 and int(h)<24 and (int(m)==00 or int(m)>00):
    print("pm")
elif int(h)<12 :
    print("am")
else:
    print('invalid input')
