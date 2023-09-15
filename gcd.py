def GCD(m,n):
  while m%n!=0:
    r=m%n
    m=n
    n=r
  return n
a=int(input('Enter first number:\t'))
b=int(input("Enter second number:\t"))
print("Greatest common Divisor of given Number is:\t",GCD(a,b))