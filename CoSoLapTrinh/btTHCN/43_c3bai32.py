a=int(input("M1="))
b=int(input("M2="))
c=int(input("M3="))
d=int(input("S="))
if (0 <= d < 100):
    print("Phai tra=",d*a,sep="")
elif(101 <= d < 150):
    print("Phai tra=",a*100+b*(d-100),sep="")
elif (151 <= d):
    print("Phai tra=",a*100+b*50+c*(d-150),sep="")    