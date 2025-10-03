a,b,c=map(float,input().split())
if a+b>c and b+c>a and a+c>b and a>0 and b>0 and c>0:
    p=(a+b+c)/2
    result=(p*(p-a)*(p-b)*(p-c))**0.5
    print(f'{result:.1f}')
else:
    print('Khong phai 3 canh cua tam giac')


