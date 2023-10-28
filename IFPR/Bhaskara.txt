n1 = str(input(" informe a equação: "))

n1 = n1.split("x²")
a = float(n1[0])

n2 = n1[1].split('x')
b = float(n2[0][1:])

if n2[0][0]=='-':
    b = b * -1

c = float(n2[1][1:])
if n2[1][0]=='-':
    c = c * -1

bhaskara = (b**2) - (4*a*c)

if bhaskara < 0:
    print(bhaskara)
   
else:
    bhaskara2 = bhaskara ** 0.5

    x1 = ((-b) - bhaskara2) / 2*a
    x2 = ((-b) + bhaskara2) / 2*a

    print(" x¹ =" , x1)
    print(" x² =" , x2)