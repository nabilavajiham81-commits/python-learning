x=int(input("how many no you hav?"))
nu=[]
print("entre the no one by one")
for i in range(x):
    y=int(input("entre the no:"))
    nu.append(y)
print("your no:",nu)

z=int(input("1.ADDITION\n2.SUB\n3.MULTIPLE\n4.Division\nentre the choice no:"))

a=0

if z==1:
    for j in nu:
        a=a+j
    print("add:",a)

elif z==2:
    a=nu[0]
    for k in nu[1:]:
        a=a-k
    print("sub:",a)

elif z==3:
    b=1
    for m in nu:
        b=b*m
    print("multiple:",b)

elif z==4:
    n=int(input("entre the numarator:"))
    d=int(input("entre the denominator:"))

    if d==0:
        print("Infinity")
    else:
        print("divided ans:",n/d)

else:
    print("invalid choice")