a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if(a>b):
    if (b>c):
        print("SLN=",a)
        print("SNN=",c)
    else:
        print("SLN=",a)
        print("SNN=",b)
if(a>c):
    if (c>b):
        print("SLN=",a)
        print("SNN=",b)
    else:
        print("SLN=",a)
        print("SNN=",c)
if (b>c):
    if (c>a):
        print("SLN=",b)
        print("SNN=",a)
    else:
        print("SLN=",b)
        print("SNN=",c)
if (c>b):
    if (b>a):
        print("SLN=",c)
        print("SNN=",a)
    else:
        print("SLN=",c)
        print("SNN=",b)
        

       

        
    

    


        
    
    
    
    
    
