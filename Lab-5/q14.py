# WAP to sum the following series S=1+(1+2)+(1+2+3)+...+(1+2+3+...+n)

def series_func(n):
    sum = n*(n+1)*(2*n+4)/12
    return sum

num = int(input("Enter value of n: "))
print(series_func(num))