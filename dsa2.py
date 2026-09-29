def power(p,n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(p, -n)
    else:
        return p * power(p, n-1)

principal = 1000
rate = 0.05
years = 5
amount = principal * power(1 + rate, years)

print(f"The amount after {years} years is: {amount:.2f}")
