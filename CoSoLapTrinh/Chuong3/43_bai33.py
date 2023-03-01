a=int(input("Tieu thu="))
Vat=0.1
if (1 <= a < 100):
    print("Phai tra=",a*550+(Vat*a*550),sep="")
elif (101 <= a < 150):
    print("Phai tra=",(100*550+Vat*100*550)+(750*(a-100)+Vat*750*(a-100)),sep="")
elif (151 <= a < 200):
    print("Phai tra=",(100*550+Vat*100*550)+(50*750+Vat*50*750)+(950*(a-150)+Vat*950*(a-150)),sep="")
elif 201 <= a:
    print("Phai tra=",(100*550+Vat*100*550)+(50*750+Vat*50*750)+(950*50+Vat*950*50)+1350*(a-200)+Vat*1350*(a-200),sep="")


    
