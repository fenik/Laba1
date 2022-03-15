print ('Введите коэффициенты квадратного уравнения a,b,c ->')
a=float(input('a='))
b=float(input('b='))
c=float(input('c5='))
D=b**2-4*a*c
print ('Дискриминант = ',D)
if D<0:
    print ('Корней нет')
elif D==0:
    x=-b/(a*2)
    print ('x=',x)
else:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print('x₁ = ', x1)
    print('x₂ = ', x2)