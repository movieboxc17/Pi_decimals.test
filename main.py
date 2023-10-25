import decimal

def pi_bbp(n):
    decimal.getcontext().prec = n + 2  # Set precision to generate n decimal places
    pi = decimal.Decimal(0)
    for k in range(n):
        pi += (decimal.Decimal(1) / 16 ** k) * (
            (decimal.Decimal(4) / (8 * k + 1)) -
            (decimal.Decimal(2) / (8 * k + 4)) -
            (decimal.Decimal(1) / (8 * k + 5)) -
            (decimal.Decimal(1) / (8 * k + 6))
        )
    return str(pi)[:-2]  # Remove the trailing '00' caused by increased precision

# Generate 500 decimal places of pi
n_decimals = 10000
pi_digits = pi_bbp(n_decimals)
print(pi_digits)
