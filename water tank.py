h=int(input("enter the height:"))
r=int(input("enter the radius:"))
f=int(input("enter the flow of water:"))
t=(int(input("enter the time :"))
vtank=3.14*r*r*h
vwtr=f*t
if vwtr>vtank:
	print("OVER FLOW CONDITION!!")
	print("Volume overflow is=",vwtr-vtank)
elif vwtr==vtank:
	print('TANK FULL!!')
else:
	print("UNDER FLOW CONDITION!!")
	ht=vwtr/(3.14*r*r)
	hr=h-ht
	print(f"                   Filled height {ht} \n remaining height {hr}		")

