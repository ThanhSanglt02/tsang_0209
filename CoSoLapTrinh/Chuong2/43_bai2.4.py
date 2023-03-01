a=int(input('do dai 1:'))
b=int(input('do dai 2:'))
c=int(input('do dai 3:'))
S=(a+b+c)/2
import math
d=math.sqrt(S*(S-a)*(S-b)*(S-c))
print('Dien tich=',d)