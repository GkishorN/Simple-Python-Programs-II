p=float(input("Enter the principal amount:"))
r=float(input("Enter the interest rate:"))
n=int(input("Enter number of times interest applied per time period:"))
t=int(input("Enter the time period:"))
a=p*pow((1+(r/n)),n*t)
print("Compound interest will be:",a)

